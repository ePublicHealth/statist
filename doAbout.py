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

import webbrowser, os

from frmAbout import Ui_dlgAbout

class dlgAbout( QDialog, Ui_dlgAbout ):
	def __init__( self, iface ):
		QDialog.__init__( self )
		self.iface = iface
		self.setupUi( self )
		
		self.tabWidget.setCurrentIndex( 0 )
		self.btnHelp = self.buttonBox.button( QDialogButtonBox.Help )
		QObject.connect( self.btnHelp, SIGNAL( "clicked()" ), self.showHelp )
		
		# setup labels
		ver = "0.2.3"
		dt = "2009-08-05"
		rev = "11"
		self.lblVersion.setText( self.tr( "Version: %1" ).arg( ver ) )
		self.lblDate.setText( self.tr( "Date: %1" ).arg( dt ) )
		self.lblRevision.setText( self.tr( "SVN revision: %1" ).arg( rev ) )
		#self.lblLogo.setPixmap( QPixmap( ":/icons/default/statist_logo.png" ) )
		
		# setup texts
		aboutString = QString( "The goal of Statist is to provide some basic statistic information for " )
		aboutString.append( "the selected field of vector layer, in text and graphical (frequency " )
		aboutString.append( "distribution histogram) form.\n\n" )
		aboutString.append( "Both numeric (integer, real, date) and  text (string) fields are supported. " )
		aboutString.append( "You can work with whole layer and only with selected records.\n\n" )
		aboutString.append( "If you found a bug, want to make suggestions for improving Statist, or " )
		aboutString.append( "have a question about this plugin, please email me: alexander.bruy@gmail.com\n\n" )
		aboutString.append( "LICENSING INFORMATION\n" )
		aboutString.append( "Statist is copyright (C) 2009 Alexander Bruy (alexander.bruy@gmail.com)\n" )
		aboutString.append( "Some code was adapted from 'fTools', (C) 2008-2009 by Carson J.Q. Farmer\n" )
		aboutString.append( "Translation and i18n code was adapted from 'Geoprocessing Plugin', (C) 2008 ")
		aboutString.append( "by Dr. Horst Duester, Stefan Ziegler.\n\n" )
		aboutString.append( "Licensed under the terms of GNU GPL 2.\n")
		aboutString.append( "This program is free software; you can redistribute it and/or modify it under ")
		aboutString.append( "the terms of the GNU General Public License as published by the Free ")
		aboutString.append( "Software Foundation; either version 2 of the License, or (at your option) ")
		aboutString.append( "any later version.\n")
		aboutString.append( "This code is distributed in the hope that it will be useful, but WITHOUT ANY ")
		aboutString.append( "WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS ")
		aboutString.append( "FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more ")
		aboutString.append( "details.\n")
		aboutString.append( "A copy of the GNU General Public License is available on the World Wide Web ")
		aboutString.append( "at http://www.gnu.org/copyleft/gpl.html. You can also obtain it by writing ")
		aboutString.append( "to the Free Software Foundation, Inc., 59 Temple Place - Suite 330, Boston, ")
		aboutString.append( "MA 02111-1307, USA.")
		
		contribString = QString( "<p><center><b>The following people contributed to Statist:</b></center></p>" )
		contribString.append( "<p>Carson J. Q. Farmer<br>" )
		contribString.append( "Horst Duester and Stefan Ziegler<br>" )
		contribString.append( "Maxim Dubinin<br>" )
		contribString.append( "Oleg Seliverstov<br>" )
		contribString.append( "Denis Rykov<br><br>" )
		contribString.append( "<b>and special thanks to the QGIS team and GIS-Lab</b></p>" )
		
		acknowlString = QString( "<p><center><b>Statist is using following third party libraries and tools</b></center></p>" )
		acknowlString.append( "<p><b>Component libraries:</b><p>" )
		acknowlString.append( "<p>matplotlib - Python 2D plotting library<br>" )
		acknowlString.append( '<a href="http://matplotlib.sourceforge.net">http://matplotlib.sourceforge.net</a></p>' )
		acknowlString.append( "<p><b>Icon sets:</b><p>" )
		acknowlString.append( "<p>Silk icon set 1.3 by Mark James<br>" )
		acknowlString.append( '<a href="http://www.famfamfam.com/lab/icons/silk/">http://www.famfamfam.com/lab/icons/silk/</a></p>' )
		acknowlString.append( "<p><b>Fonts:</b><p>" )
		acknowlString.append( "<p>Charis SIL font family<br>" )
		acknowlString.append( '<a href="http://scripts.sil.org/">http://scripts.sil.org/</a></p>' )
		
		# write texts
		self.memAbout.setText( aboutString )
		self.memContrib.setText( contribString )
		self.memAcknowl.setText( acknowlString )
	
	def showHelp( self ):
		localeFullName = QLocale.system().name()
		localeShortName = localeFullName[ 0:2 ]
		if localeShortName in [ 'ru', 'ua' ]:
			webbrowser.open( "http://gis-lab.info/qa/statist.html " )
		else:
			webbrowser.open( "http://gis-lab.info/qa/statist-en.html " )
		# determine help path
		#userPluginPath = QFileInfo( QgsApplication.qgisUserDbFilePath() ).path() + "/python/plugins/statist"
		#systemPluginPath = QgsApplication.prefixPath() + "/python/plugins/statist"
		#if QFileInfo( userPluginPath ).exists():
		#	helpPath = userPluginPath + "/doc/help_" + localeShortName + ".html"
		#else:
		#	helpPath = systemPluginPath + "/doc/help_" + localeShortName + ".html"
		
		#webbrowser.open( fontPath )
