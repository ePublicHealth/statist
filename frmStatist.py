# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmStatist.ui'
#
# Created: Wed Aug 05 18:15:59 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgStatistics(object):
    def setupUi(self, dlgStatistics):
        dlgStatistics.setObjectName("dlgStatistics")
        dlgStatistics.resize(814, 434)
        dlgStatistics.setSizeGripEnabled(True)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(dlgStatistics)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widgetStats = QtGui.QWidget(dlgStatistics)
        self.widgetStats.setMinimumSize(QtCore.QSize(341, 331))
        self.widgetStats.setMaximumSize(QtCore.QSize(360, 16777215))
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
        self.tblStatistics = QtGui.QTableWidget(self.widgetStats)
        self.tblStatistics.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tblStatistics.setAlternatingRowColors(True)
        self.tblStatistics.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.tblStatistics.setCornerButtonEnabled(False)
        self.tblStatistics.setObjectName("tblStatistics")
        self.tblStatistics.setColumnCount(2)
        self.tblStatistics.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tblStatistics.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tblStatistics.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tblStatistics, 6, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.widgetStats)
        self.widgetPlot = QtGui.QWidget(dlgStatistics)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetPlot.sizePolicy().hasHeightForWidth())
        self.widgetPlot.setSizePolicy(sizePolicy)
        self.widgetPlot.setMinimumSize(QtCore.QSize(340, 330))
        self.widgetPlot.setObjectName("widgetPlot")
        self.verticalLayout = QtGui.QVBoxLayout(self.widgetPlot)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layoutPlot = QtGui.QVBoxLayout()
        self.layoutPlot.setObjectName("layoutPlot")
        self.verticalLayout.addLayout(self.layoutPlot)
        self.groupBox = QtGui.QGroupBox(self.widgetPlot)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(361, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.edMinX = QtGui.QDoubleSpinBox(self.groupBox)
        self.edMinX.setMinimumSize(QtCore.QSize(0, 0))
        self.edMinX.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edMinX.setMaximum(999999999.99)
        self.edMinX.setObjectName("edMinX")
        self.gridLayout_3.addWidget(self.edMinX, 0, 1, 1, 1)
        self.btnRefresh = QtGui.QPushButton(self.groupBox)
        self.btnRefresh.setObjectName("btnRefresh")
        self.gridLayout_3.addWidget(self.btnRefresh, 0, 3, 2, 1)
        self.chkGrid = QtGui.QCheckBox(self.groupBox)
        self.chkGrid.setObjectName("chkGrid")
        self.gridLayout_3.addWidget(self.chkGrid, 0, 5, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.edMaxX = QtGui.QDoubleSpinBox(self.groupBox)
        self.edMaxX.setMinimumSize(QtCore.QSize(0, 0))
        self.edMaxX.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edMaxX.setMaximum(999999999.99)
        self.edMaxX.setObjectName("edMaxX")
        self.gridLayout_3.addWidget(self.edMaxX, 1, 1, 1, 1)
        self.chkPlot = QtGui.QCheckBox(self.groupBox)
        self.chkPlot.setObjectName("chkPlot")
        self.gridLayout_3.addWidget(self.chkPlot, 1, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 4, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
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
        self.tblStatistics.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("dlgStatistics", "Parameter", None, QtGui.QApplication.UnicodeUTF8))
        self.tblStatistics.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("dlgStatistics", "Value", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgStatistics", "Xmin", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRefresh.setText(QtGui.QApplication.translate("dlgStatistics", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.chkGrid.setText(QtGui.QApplication.translate("dlgStatistics", "Show grid", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlgStatistics", "Xmax", None, QtGui.QApplication.UnicodeUTF8))
        self.chkPlot.setText(QtGui.QApplication.translate("dlgStatistics", "As plot", None, QtGui.QApplication.UnicodeUTF8))

