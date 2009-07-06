# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmStatist.ui'
#
# Created: Mon Jul 06 14:52:37 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgStatistics(object):
    def setupUi(self, dlgStatistics):
        dlgStatistics.setObjectName("dlgStatistics")
        dlgStatistics.resize(705, 349)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(dlgStatistics)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widgetStats = QtGui.QWidget(dlgStatistics)
        self.widgetStats.setMinimumSize(QtCore.QSize(341, 331))
        self.widgetStats.setObjectName("widgetStats")
        self.gridLayout = QtGui.QGridLayout(self.widgetStats)
        self.gridLayout.setObjectName("gridLayout")
        self.lblLayer = QtGui.QLabel(self.widgetStats)
        self.lblLayer.setObjectName("lblLayer")
        self.gridLayout.addWidget(self.lblLayer, 0, 0, 1, 1)
        self.cmbLayers = QtGui.QComboBox(self.widgetStats)
        self.cmbLayers.setObjectName("cmbLayers")
        self.gridLayout.addWidget(self.cmbLayers, 1, 0, 1, 2)
        self.lblField = QtGui.QLabel(self.widgetStats)
        self.lblField.setObjectName("lblField")
        self.gridLayout.addWidget(self.lblField, 2, 0, 1, 2)
        self.cmbFields = QtGui.QComboBox(self.widgetStats)
        self.cmbFields.setObjectName("cmbFields")
        self.gridLayout.addWidget(self.cmbFields, 3, 0, 1, 2)
        self.chkUseTextFields = QtGui.QCheckBox(self.widgetStats)
        self.chkUseTextFields.setObjectName("chkUseTextFields")
        self.gridLayout.addWidget(self.chkUseTextFields, 4, 0, 1, 2)
        self.lblResult = QtGui.QLabel(self.widgetStats)
        self.lblResult.setObjectName("lblResult")
        self.gridLayout.addWidget(self.lblResult, 5, 0, 1, 2)
        self.lstStatistics = QtGui.QListWidget(self.widgetStats)
        self.lstStatistics.setMaximumSize(QtCore.QSize(16777215, 136))
        self.lstStatistics.setAlternatingRowColors(True)
        self.lstStatistics.setObjectName("lstStatistics")
        self.gridLayout.addWidget(self.lstStatistics, 6, 0, 1, 2)
        self.progressBar = QtGui.QProgressBar(self.widgetStats)
        self.progressBar.setProperty("value", QtCore.QVariant(24))
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 7, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStop = QtGui.QPushButton(self.widgetStats)
        self.btnStop.setEnabled(False)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.buttonBox = QtGui.QDialogButtonBox(self.widgetStats)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.widgetStats)
        self.widgetPlot = QtGui.QWidget(dlgStatistics)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPlot.sizePolicy().hasHeightForWidth())
        self.widgetPlot.setSizePolicy(sizePolicy)
        self.widgetPlot.setMinimumSize(QtCore.QSize(340, 330))
        self.widgetPlot.setObjectName("widgetPlot")
        self.horizontalLayout_2.addWidget(self.widgetPlot)

        self.retranslateUi(dlgStatistics)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgStatistics.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgStatistics.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgStatistics)

    def retranslateUi(self, dlgStatistics):
        dlgStatistics.setWindowTitle(QtGui.QApplication.translate("dlgStatistics", "Statist: Field statistics", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLayer.setText(QtGui.QApplication.translate("dlgStatistics", "Input vector layer:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblField.setText(QtGui.QApplication.translate("dlgStatistics", "Target field:", None, QtGui.QApplication.UnicodeUTF8))
        self.chkUseTextFields.setText(QtGui.QApplication.translate("dlgStatistics", "Enable statistics for text fields", None, QtGui.QApplication.UnicodeUTF8))
        self.lblResult.setText(QtGui.QApplication.translate("dlgStatistics", "Statistics output:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnStop.setText(QtGui.QApplication.translate("dlgStatistics", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

