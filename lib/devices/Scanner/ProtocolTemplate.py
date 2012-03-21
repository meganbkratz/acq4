# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProtocolTemplate.ui'
#
# Created: Mon Mar 19 15:07:42 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1053, 444)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QtGui.QGridLayout(Form)
        self.gridLayout_4.setMargin(3)
        self.gridLayout_4.setHorizontalSpacing(9)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.simulateShutterCheck = QtGui.QCheckBox(Form)
        self.simulateShutterCheck.setObjectName(_fromUtf8("simulateShutterCheck"))
        self.gridLayout.addWidget(self.simulateShutterCheck, 2, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(190, 210))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tdPlotWidget = PlotWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tdPlotWidget.sizePolicy().hasHeightForWidth())
        self.tdPlotWidget.setSizePolicy(sizePolicy)
        self.tdPlotWidget.setObjectName(_fromUtf8("tdPlotWidget"))
        self.gridLayout_3.addWidget(self.tdPlotWidget, 0, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.minTimeSpin = SpinBox(self.groupBox)
        self.minTimeSpin.setSuffix(_fromUtf8(""))
        self.minTimeSpin.setDecimals(2)
        self.minTimeSpin.setMaximum(1000000.0)
        self.minTimeSpin.setObjectName(_fromUtf8("minTimeSpin"))
        self.gridLayout_3.addWidget(self.minTimeSpin, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.minDistSpin = SpinBox(self.groupBox)
        self.minDistSpin.setSuffix(_fromUtf8(""))
        self.minDistSpin.setMaximum(1000000.0)
        self.minDistSpin.setObjectName(_fromUtf8("minDistSpin"))
        self.gridLayout_3.addWidget(self.minDistSpin, 2, 1, 1, 1)
        self.recomputeBtn = QtGui.QPushButton(self.groupBox)
        self.recomputeBtn.setObjectName(_fromUtf8("recomputeBtn"))
        self.gridLayout_3.addWidget(self.recomputeBtn, 5, 0, 1, 2)
        self.timeLabel = QtGui.QLabel(self.groupBox)
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.gridLayout_3.addWidget(self.timeLabel, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 5, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setMargin(3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sizeFromCalibrationRadio = QtGui.QRadioButton(self.groupBox_2)
        self.sizeFromCalibrationRadio.setChecked(True)
        self.sizeFromCalibrationRadio.setObjectName(_fromUtf8("sizeFromCalibrationRadio"))
        self.gridLayout_2.addWidget(self.sizeFromCalibrationRadio, 0, 0, 1, 2)
        self.sizeCustomRadio = QtGui.QRadioButton(self.groupBox_2)
        self.sizeCustomRadio.setObjectName(_fromUtf8("sizeCustomRadio"))
        self.gridLayout_2.addWidget(self.sizeCustomRadio, 1, 0, 1, 1)
        self.sizeSpin = SpinBox(self.groupBox_2)
        self.sizeSpin.setSuffix(_fromUtf8(""))
        self.sizeSpin.setMinimum(0.0)
        self.sizeSpin.setMaximum(100000.0)
        self.sizeSpin.setSingleStep(1e-06)
        self.sizeSpin.setProperty("value", 0.0)
        self.sizeSpin.setObjectName(_fromUtf8("sizeSpin"))
        self.gridLayout_2.addWidget(self.sizeSpin, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 4, 0, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.laserCombo = InterfaceCombo(Form)
        self.laserCombo.setObjectName(_fromUtf8("laserCombo"))
        self.gridLayout.addWidget(self.laserCombo, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cameraCombo = InterfaceCombo(Form)
        self.cameraCombo.setObjectName(_fromUtf8("cameraCombo"))
        self.gridLayout.addWidget(self.cameraCombo, 0, 1, 1, 1)
        self.loadConfigBtn = QtGui.QPushButton(Form)
        self.loadConfigBtn.setObjectName(_fromUtf8("loadConfigBtn"))
        self.gridLayout.addWidget(self.loadConfigBtn, 7, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setMargin(5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.itemTree = ParameterTree(self.groupBox_3)
        self.itemTree.setObjectName(_fromUtf8("itemTree"))
        self.itemTree.header().setVisible(False)
        self.gridLayout_5.addWidget(self.itemTree, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.hideCheck = QtGui.QCheckBox(self.groupBox_3)
        self.hideCheck.setEnabled(True)
        self.hideCheck.setChecked(False)
        self.hideCheck.setObjectName(_fromUtf8("hideCheck"))
        self.horizontalLayout_5.addWidget(self.hideCheck)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.hideMarkerBtn = QtGui.QPushButton(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hideMarkerBtn.sizePolicy().hasHeightForWidth())
        self.hideMarkerBtn.setSizePolicy(sizePolicy)
        self.hideMarkerBtn.setObjectName(_fromUtf8("hideMarkerBtn"))
        self.horizontalLayout_5.addWidget(self.hideMarkerBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 1, 2, 1)
        self.groupBox_4 = QtGui.QGroupBox(Form)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_6.setMargin(5)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.programTable = QtGui.QTableWidget(self.groupBox_4)
        self.programTable.setObjectName(_fromUtf8("programTable"))
        self.programTable.setColumnCount(0)
        self.programTable.setRowCount(0)
        self.gridLayout_6.addWidget(self.programTable, 1, 0, 1, 1)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.addLineScanBtn = QtGui.QPushButton(self.groupBox_4)
        self.addLineScanBtn.setEnabled(False)
        self.addLineScanBtn.setObjectName(_fromUtf8("addLineScanBtn"))
        self.gridLayout_7.addWidget(self.addLineScanBtn, 0, 0, 1, 1)
        self.addCircleScanBtn = QtGui.QPushButton(self.groupBox_4)
        self.addCircleScanBtn.setEnabled(False)
        self.addCircleScanBtn.setObjectName(_fromUtf8("addCircleScanBtn"))
        self.gridLayout_7.addWidget(self.addCircleScanBtn, 0, 1, 1, 1)
        self.addSpiralScanBtn = QtGui.QPushButton(self.groupBox_4)
        self.addSpiralScanBtn.setEnabled(False)
        self.addSpiralScanBtn.setObjectName(_fromUtf8("addSpiralScanBtn"))
        self.gridLayout_7.addWidget(self.addSpiralScanBtn, 1, 0, 1, 1)
        self.deleteStepBtn = QtGui.QPushButton(self.groupBox_4)
        self.deleteStepBtn.setEnabled(False)
        self.deleteStepBtn.setObjectName(_fromUtf8("deleteStepBtn"))
        self.gridLayout_7.addWidget(self.deleteStepBtn, 1, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_9 = QtGui.QGridLayout()
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 0, 1, 1, 1)
        self.previewBtn = QtGui.QPushButton(self.groupBox_4)
        self.previewBtn.setEnabled(False)
        self.previewBtn.setObjectName(_fromUtf8("previewBtn"))
        self.gridLayout_9.addWidget(self.previewBtn, 0, 2, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_9, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_4, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.simulateShutterCheck.setText(QtGui.QApplication.translate("Form", "Simulate Shutter", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Spot Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Minimum time", None, QtGui.QApplication.UnicodeUTF8))
        self.minTimeSpin.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When stimulating a sequence of points, this is the minimum amount of time that must pass before stimulating the same spot a second time. Points farther away will require smaller delays. Points farther than the minimum distance (specified below) will require no delay.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Minimum distance", None, QtGui.QApplication.UnicodeUTF8))
        self.minDistSpin.setToolTip(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">When stimulating a sequence of points, this is the minimum distance between two spots such that no time delay is required between stimulating them. Points closer than this distance will require some delay, which is determined in part by the minimum time specified above.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.recomputeBtn.setText(QtGui.QApplication.translate("Form", "Recompute Order", None, QtGui.QApplication.UnicodeUTF8))
        self.timeLabel.setText(QtGui.QApplication.translate("Form", "Total Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Spot Display Size", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeFromCalibrationRadio.setToolTip(QtGui.QApplication.translate("Form", "Causes target spots to be displayed at the size determined by the calibration file. Does not affect how data is collected.", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeFromCalibrationRadio.setText(QtGui.QApplication.translate("Form", "Use size from calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeCustomRadio.setToolTip(QtGui.QApplication.translate("Form", "Lets the user change the display size of target spots. Does not change the way data is collected.", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeCustomRadio.setText(QtGui.QApplication.translate("Form", "Use custom size:", None, QtGui.QApplication.UnicodeUTF8))
        self.sizeSpin.setToolTip(QtGui.QApplication.translate("Form", "Specifies the display size of the target spots. Does not change the way data is collected.", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Camera Module:", None, QtGui.QApplication.UnicodeUTF8))
        self.laserCombo.setToolTip(QtGui.QApplication.translate("Form", "Selects the laser to be used.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Laser Device:", None, QtGui.QApplication.UnicodeUTF8))
        self.cameraCombo.setToolTip(QtGui.QApplication.translate("Form", "Selects the camera module to use with the scanner. This, along with the laser device, determines which calibration files will be used.", None, QtGui.QApplication.UnicodeUTF8))
        self.loadConfigBtn.setText(QtGui.QApplication.translate("Form", "Load Last Config", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Position Control Items", None, QtGui.QApplication.UnicodeUTF8))
        self.hideCheck.setToolTip(QtGui.QApplication.translate("Form", "Hide all items from view.", None, QtGui.QApplication.UnicodeUTF8))
        self.hideCheck.setText(QtGui.QApplication.translate("Form", "Hide items", None, QtGui.QApplication.UnicodeUTF8))
        self.hideMarkerBtn.setText(QtGui.QApplication.translate("Form", "Hide Spot Marker", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Program Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.programTable.setSortingEnabled(True)
        self.addLineScanBtn.setText(QtGui.QApplication.translate("Form", "Add Line Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.addCircleScanBtn.setText(QtGui.QApplication.translate("Form", "Add Circle Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.addSpiralScanBtn.setText(QtGui.QApplication.translate("Form", "Add Spiral Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteStepBtn.setText(QtGui.QApplication.translate("Form", "Delete Step", None, QtGui.QApplication.UnicodeUTF8))
        self.previewBtn.setText(QtGui.QApplication.translate("Form", "Preview", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import SpinBox, PlotWidget
from pyqtgraph.parametertree import ParameterTree
from InterfaceCombo import InterfaceCombo
