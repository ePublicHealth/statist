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
from qgis.gui import * 

# return list of names of all layers (vector, raster or both types) in QgsMapLayerRegistry 
def getLayersNames( layerType ):
	layermap = QgsMapLayerRegistry.instance().mapLayers()
	layerlist = []
	if layerType == "all":
		for name, layer in layermap.iteritems():
			layerlist.append( unicode( layer.name() ) )
	elif layerType == "vector":
		for name, layer in layermap.iteritems():
			if layer.type() == QgsMapLayer.VectorLayer:
				layerlist.append( unicode( layer.name() ) )
	else:
		for name, layer in layermap.iteritems():
			if layer.type() == QgsMapLayer.RasterLayer:
				layerlist.append( unicode( layer.name() ) )
	return layerlist

# return list of names of all fields from input QgsVectorLayer
def getFieldNames( vlayer ):
	fieldmap = getFieldList( vlayer )
	fieldlist = []
	for name, field in fieldmap.iteritems():
		if not field.name() in fieldlist:
			fieldlist.append( unicode( field.name() ) )
	return fieldlist

# return QgsVectorLayer from a layer name (as string)
def getVectorLayerByName( myName ):
	layermap = QgsMapLayerRegistry.instance().mapLayers()
	for name, layer in layermap.iteritems():
		if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
			if layer.isValid():
				return layer
			else:
				return None

# return the field list of a vector layer
def getFieldList( vlayer ):
	vprovider = vlayer.dataProvider()
	#feat = QgsFeature()
	allAttrs = vprovider.attributeIndexes()
	vprovider.select( allAttrs )
	myFields = vprovider.fields()
	return myFields

# return field type from it's name
def getFieldType( vlayer, fieldName ):
	fields = vlayer.dataProvider().fields()
	for name, field in fields.iteritems():
		if field.name() == fieldName:
			return field.typeName()

# return number of unique values in field
def getUniqueValsCount( vlayer, fieldIndex, useSelection ):
	vprovider = vlayer.dataProvider()
	allAttrs = vprovider.attributeIndexes()
	vprovider.select( allAttrs )
	count = 0
	values = []
	if useSelection:
		selection = vlayer.selectedFeatures()
		for f in selection:
			if f.attributeMap()[ fieldIndex ].toString() not in values:
				values.append( f.attributeMap()[ fieldIndex ].toString() )
				count += 1
	else:
		feat = QgsFeature()
		while vprovider.nextFeature( feat ):
			if feat.attributeMap()[ fieldIndex ].toString() not in values:
				values.append( feat.attributeMap()[ fieldIndex ].toString() )
				count += 1
	return count
