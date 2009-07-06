# -*- coding: utf-8 -*-

#*****************************************************************************************************************
# Statist
# --------------------------------------------------
# A python plugin for QGIS. Provides basic statistics information
# on any (numeric or string) field of vector layer. Works fine
# with selected objects and whole layer.
# 
# Based on partially rewritten 'Basic statistics' from fTools,
# (C) 2009 Carson Farmer.
#
#  Copyright (C) 2009 Alexander Bruy (alexander.bruy@gmail.com)
#
#  This source is free software; you can redistribute it and/or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This code is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  A copy of the GNU General Public License is available on the World Wide Web
#  at <http://www.gnu.org/copyleft/gpl.html>. You can also obtain it by writing
#  to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston,
#  MA 02111-1307, USA.
#
#*****************************************************************************************************************

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import os, math

from frmStatist import Ui_dlgStatistics

import utils

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import resources

class dlgStatist( QDialog, Ui_dlgStatistics ):
	def __init__( self, iface ):
		QDialog.__init__( self )
		self.iface = iface
		self.setupUi( self )
		
		# prepare figure
		self.figure = Figure()
		self.figure.set_figsize_inches( ( 4.3, 4.2 ) )
		self.axes = self.figure.add_subplot( 111 )
		self.figure.suptitle( "Frequency distribution", fontsize = 12 )
		self.axes.grid( True )
		self.canvas = FigureCanvas( self.figure )
		self.canvas.setParent( self.widgetPlot )
		
		# for tracking layers change
		QObject.connect( self.cmbLayers, SIGNAL( "currentIndexChanged(QString)" ), self.updateFields )
		# fill layers combobox
		self.cmbLayers.clear()
		lstLayers = utils.getLayersNames( "vector" )
		self.cmbLayers.addItems( lstLayers )
		# reset some controls to default values
		self.cmbFields.setCurrentIndex(-1)
		self.progressBar.setValue( 0 )
		QObject.connect( self.cmbFields, SIGNAL( "activated(QString)" ), self.startCalculation )
		QObject.connect( self.chkUseTextFields, SIGNAL( "stateChanged(int)" ), self.updateFields )
	
	def updateFields( self ):
		self.cmbFields.clear()
		layName = unicode( self.cmbLayers.currentText() )
		if layName != "":
			vLayer = utils.getVectorLayerByName( layName )
			lstFields = vLayer.dataProvider().fields()
			if self.chkUseTextFields.checkState(): # only numeric fields
				for i in lstFields:
					if lstFields[i].type() == QVariant.String:
						self.cmbFields.addItem( unicode( lstFields[i].name() ) )
			else: # only text fields
				for i in lstFields:
					if lstFields[i].type() == QVariant.Int or lstFields[i].type() == QVariant.Double:
						self.cmbFields.addItem( unicode( lstFields[i].name() ) )
			self.cmbFields.setCurrentIndex(-1)
	
	def startCalculation( self ):
		if self.cmbLayers.currentText() == "":
			QMessageBox.information( self, "Error!", self.tr( "Please specify target vector layer first" ) )
		elif self.cmbFields.currentText() == "":
			QMessageBox.information( self, "Error!", self.tr( "Please specify target field first" ) )
		else:
			vlayer = utils.getVectorLayerByName( self.cmbLayers.currentText() )
			self.calculate( self.cmbLayers.currentText(), self.cmbFields.currentText() )
	
	def calculate( self, layerName, fieldName ):
		vLayer = utils.getVectorLayerByName( layerName )
		self.lstStatistics.clear()
		self.threadCalc = workThread( self.iface.mainWindow(), self, vLayer, fieldName )
		QObject.connect( self.threadCalc, SIGNAL( "runFinished(PyQt_PyObject)" ), self.runFinishedFromThread )
		QObject.connect( self.threadCalc, SIGNAL( "runStatus(PyQt_PyObject)" ), self.runStatusFromThread )
		QObject.connect( self.threadCalc, SIGNAL( "runRange(PyQt_PyObject)" ), self.runRangeFromThread )
		
		QObject.disconnect( self.btnStop, SIGNAL( "clicked()" ), self.toClipboard )
		self.btnStop.setText( self.tr( "Cancel" ) )
		QObject.connect( self.btnStop, SIGNAL("clicked()" ), self.cancelThread )
		self.btnStop.setEnabled( True )
		
		self.threadCalc.start()
		return True
	
	def toClipboard( self ):
		txt = ""
		for i in range( self.lstStatistics.count() ):
			txt += self.lstStatistics.item( i ).text() + "\n"
		clipboard = QApplication.clipboard()
		clipboard.setText( txt )
	
	def cancelThread( self ):
		self.threadCalc.stop()
	
	def runFinishedFromThread( self, output ):
		self.threadCalc.stop()
		self.lstStatistics.addItems( output[ 0 ] )
		QObject.disconnect( self.btnStop, SIGNAL( "clicked()" ), self.cancelThread )
		self.btnStop.setText( self.tr ("Copy" ) )
		QObject.connect( self.btnStop, SIGNAL( "clicked()" ), self.toClipboard )
		#self.btnStop.setEnabled( False )
		
		self.axes.clear()
		self.axes.grid( True )
		self.figure.suptitle( "Frequency distribution", fontsize = 12 )
		self.axes.set_ylabel( "Count", fontsize = 8 )
		self.axes.set_xlabel( "Values", fontsize = 8 )
		x = output[ 2 ]
		self.axes.hist( x, 50, alpha=0.5, histtype = "bar" )
		self.canvas.draw()
		
		return True
	
	def runStatusFromThread( self, status ):
		self.progressBar.setValue( status )
	
	def runRangeFromThread( self, range_vals ):
		self.progressBar.setRange( range_vals[ 0 ], range_vals[ 1 ] )
	
class workThread( QThread ):
	def __init__( self, parentThread, parentObject, vlayer, fieldName ):
		QThread.__init__( self, parentThread )
		self.parent = parentObject
		self.running = False
		self.vlayer = vlayer
		self.fieldName = fieldName
	
	def run( self ):
		self.running = True
		( lst, cnt, val ) = self.statistics( self.vlayer, self.fieldName )
		self.emit( SIGNAL( "runFinished(PyQt_PyObject)" ), ( lst, cnt, val ) )
		self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), 0 )
	
	def stop( self ):
		self.running = False
	
	def statistics( self, vlayer, fieldName ):
		vprovider = vlayer.dataProvider()
		allAttrs = vprovider.attributeIndexes()
		vprovider.select( allAttrs )
		fields = vprovider.fields()
		index = vprovider.fieldNameIndex( fieldName )
		feat = QgsFeature()
		nVal = 0
		values = []
		first = True
		nElement = 0
		meanVal = 0
		sumVal = 0
		if utils.getFieldType( vlayer, fieldName ) == 'String':
			fillVal = 0
			emptyVal = 0
			if vlayer.selectedFeatureCount() != 0:
				selFeat = vlayer.selectedFeatures()
				nFeat = vlayer.selectedFeatureCount()
				self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), 0 )
				self.emit( SIGNAL( "runRange(PyQt_PyObject)" ), ( 0, nFeat ) )
				for f in selFeat:
					atMap = f.attributeMap()
					lenVal = float( len( atMap[ index ].toString() ) )
					if first:
						minVal = lenVal
						maxVal = lenVal
						first = False
					else:
						if lenVal < minVal: minVal = lenVal
						if lenVal > maxVal: maxVal = lenVal
					if lenVal != 0.00:
						fillVal += 1
					else:
						emptyVal += 1
					values.append( lenVal )
					sumVal = sumVal + lenVal
					nElement += 1
					self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), nElement )
			else:
				nFeat = vprovider.featureCount()
				self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), 0 )
				self.emit( SIGNAL( "runRange(PyQt_PyObject)" ), ( 0, nFeat ) )
				while vprovider.nextFeature( feat ):
					atMap = feat.attributeMap()
					lenVal = float( len( atMap[ index ].toString() ) )
					if first:
						minVal = lenVal
						maxVal = lenVal
						first = False
					else:
						if lenVal < minVal: minVal = lenVal
						if lenVal > maxVal: maxVal = lenVal
					if lenVal != 0.00:
						fillVal += 1
					else:
						emptyVal += 1
					values.append( lenVal )
					sumVal = sumVal + lenVal
					nElement += 1
					self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), nElement )
			nVal= len( values )
			if nVal > 0.00:
				meanVal = sumVal / nVal
			lstStats = []
			lstStats.append( QCoreApplication.translate( "statResult", "Count:" ) + "\t" + unicode( nVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Minimum length:" ) + "\t" + unicode( minVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Maximum length:" ) + "\t" + unicode( maxVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Mean lengtn:" ) + "\t" + unicode( meanVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Filled:" ) + "\t" + unicode( fillVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Empty:" ) + "\t" + unicode( emptyVal ) )
			return ( lstStats, [], values )
		else:
			stdVal = 0
			cvVal = 0
			# selection
			if vlayer.selectedFeatureCount() != 0:
				selFeat = vlayer.selectedFeatures()
				nFeat = vlayer.selectedFeatureCount()
				self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), 0 )
				self.emit( SIGNAL( "runRange(PyQt_PyObject)" ), ( 0, nFeat ) )
				for f in selFeat:
					atMap = f.attributeMap()
					value = float( atMap[ index ].toDouble() [ 0 ] )
					if first:
						minVal = value
						maxVal = value
						first = False
					else:
						if value < minVal: minVal = value
						if value > maxVal: maxVal = value
					values.append( value )
					sumVal = sumVal + value
					nElement += 1
					self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), nElement )
			else: # whole layer
				nFeat = vprovider.featureCount()
				self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), 0 )
				self.emit( SIGNAL( "runRange(PyQt_PyObject)" ), ( 0, nFeat ) )
				while vprovider.nextFeature( feat ):
					atMap = feat.attributeMap()
					value = float( atMap[ index ].toDouble() [ 0 ] )
					if first:
						minVal = value
						maxVal = value
						first = False
					else:
						if value < minVal: minVal = value
						if value > maxVal: maxVal = value
					values.append( value )
					sumVal = sumVal + value
					nElement += 1
					self.emit( SIGNAL( "runStatus(PyQt_PyObject)" ), nElement )
			nVal= len( values )
			if nVal > 0.00:
				meanVal = sumVal / nVal
				if meanVal != 0.00:
					for val in values:
						stdVal += ( ( val - meanVal ) * ( val - meanVal ) )
					stdVal = math.sqrt( stdVal / nVal )
					cvVal = stdVal / meanVal
			lstStats = []
			lstStats.append( QCoreApplication.translate( "statResult", "Count:" ) + "\t" + unicode( nVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Minimum value:" ) + "\t" + unicode( minVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Maximum value:" ) + "\t" + unicode( maxVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Sum:" ) + "\t" + unicode( sumVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Mean value:" ) + "\t" + unicode( meanVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "Standard deviation:" ) + "\t" + unicode( stdVal ) )
			lstStats.append( QCoreApplication.translate( "statResult", "CV:" ) + "\t" + unicode( cvVal ))
			return ( lstStats, [], values )
