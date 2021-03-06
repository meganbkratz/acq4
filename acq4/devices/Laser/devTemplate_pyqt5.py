# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/devices/Laser/devTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(695, 563)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.powerGroup = QtWidgets.QGroupBox(Form)
        self.powerGroup.setTitle("")
        self.powerGroup.setObjectName("powerGroup")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.powerGroup)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_5 = QtWidgets.QLabel(self.powerGroup)
        self.label_5.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 2, 1, 1)
        self.expectedPowerSpin = SpinBox(self.powerGroup)
        self.expectedPowerSpin.setMinimumSize(Qt.QSize(75, 0))
        self.expectedPowerSpin.setObjectName("expectedPowerSpin")
        self.gridLayout_4.addWidget(self.expectedPowerSpin, 0, 3, 1, 1)
        self.toleranceSpin = SpinBox(self.powerGroup)
        self.toleranceSpin.setMinimumSize(Qt.QSize(75, 0))
        self.toleranceSpin.setObjectName("toleranceSpin")
        self.gridLayout_4.addWidget(self.toleranceSpin, 1, 3, 1, 1)
        self.energyCalcGroup = QtWidgets.QGroupBox(self.powerGroup)
        self.energyCalcGroup.setObjectName("energyCalcGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.energyCalcGroup)
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.currentPowerRadio = QtWidgets.QRadioButton(self.energyCalcGroup)
        self.currentPowerRadio.setObjectName("currentPowerRadio")
        self.verticalLayout.addWidget(self.currentPowerRadio)
        self.expectedPowerRadio = QtWidgets.QRadioButton(self.energyCalcGroup)
        self.expectedPowerRadio.setChecked(True)
        self.expectedPowerRadio.setObjectName("expectedPowerRadio")
        self.verticalLayout.addWidget(self.expectedPowerRadio)
        self.gridLayout_4.addWidget(self.energyCalcGroup, 0, 4, 2, 1)
        self.label_4 = QtWidgets.QLabel(self.powerGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.outputPowerLabel = QtWidgets.QLabel(self.powerGroup)
        font = Qt.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.outputPowerLabel.setFont(font)
        self.outputPowerLabel.setText("")
        self.outputPowerLabel.setObjectName("outputPowerLabel")
        self.gridLayout_4.addWidget(self.outputPowerLabel, 0, 1, 1, 1)
        self.samplePowerLabel = QtWidgets.QLabel(self.powerGroup)
        font = Qt.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.samplePowerLabel.setFont(font)
        self.samplePowerLabel.setText("")
        self.samplePowerLabel.setObjectName("samplePowerLabel")
        self.gridLayout_4.addWidget(self.samplePowerLabel, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.powerGroup)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.powerAlertCheck = QtWidgets.QCheckBox(self.powerGroup)
        self.powerAlertCheck.setChecked(True)
        self.powerAlertCheck.setObjectName("powerAlertCheck")
        self.gridLayout_4.addWidget(self.powerAlertCheck, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.powerGroup, 0, 0, 1, 3)
        self.wavelengthGroup = QtWidgets.QGroupBox(Form)
        self.wavelengthGroup.setTitle("")
        self.wavelengthGroup.setObjectName("wavelengthGroup")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.wavelengthGroup)
        self.gridLayout_5.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.wavelengthGroup)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.wavelengthSpin = SpinBox(self.wavelengthGroup)
        self.wavelengthSpin.setSuffix("")
        self.wavelengthSpin.setObjectName("wavelengthSpin")
        self.gridLayout_5.addWidget(self.wavelengthSpin, 0, 1, 1, 1)
        self.wavelengthCombo = QtWidgets.QComboBox(self.wavelengthGroup)
        self.wavelengthCombo.setObjectName("wavelengthCombo")
        self.wavelengthCombo.addItem("")
        self.gridLayout_5.addWidget(self.wavelengthCombo, 0, 2, 1, 1)
        self.GDDEnableCheck = QtWidgets.QCheckBox(self.wavelengthGroup)
        self.GDDEnableCheck.setObjectName("GDDEnableCheck")
        self.gridLayout_5.addWidget(self.GDDEnableCheck, 1, 0, 1, 1)
        self.GDDSpin = QtWidgets.QSpinBox(self.wavelengthGroup)
        self.GDDSpin.setMaximum(32000)
        self.GDDSpin.setObjectName("GDDSpin")
        self.gridLayout_5.addWidget(self.GDDSpin, 1, 1, 1, 1)
        self.GDDLimits = QtWidgets.QLabel(self.wavelengthGroup)
        self.GDDLimits.setObjectName("GDDLimits")
        self.gridLayout_5.addWidget(self.GDDLimits, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.wavelengthGroup, 3, 0, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setAlignment(Qt.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.calibrationList = QtWidgets.QTreeWidget(self.groupBox_2)
        font = Qt.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.calibrationList.setFont(font)
        self.calibrationList.setRootIsDecorated(False)
        self.calibrationList.setItemsExpandable(False)
        self.calibrationList.setObjectName("calibrationList")
        self.calibrationList.header().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.calibrationList, 0, 0, 1, 5)
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setAlignment(Qt.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scanLabel = QtWidgets.QLabel(self.groupBox)
        self.scanLabel.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.scanLabel.setObjectName("scanLabel")
        self.gridLayout_2.addWidget(self.scanLabel, 1, 3, 1, 1)
        self.measurementSpin = SpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measurementSpin.sizePolicy().hasHeightForWidth())
        self.measurementSpin.setSizePolicy(sizePolicy)
        self.measurementSpin.setMinimum(0.0)
        self.measurementSpin.setMaximum(100.0)
        self.measurementSpin.setProperty("value", 1.0)
        self.measurementSpin.setObjectName("measurementSpin")
        self.gridLayout_2.addWidget(self.measurementSpin, 1, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 3, 1, 1)
        self.settlingSpin = SpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settlingSpin.sizePolicy().hasHeightForWidth())
        self.settlingSpin.setSizePolicy(sizePolicy)
        self.settlingSpin.setObjectName("settlingSpin")
        self.gridLayout_2.addWidget(self.settlingSpin, 2, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.meterCombo = InterfaceCombo(self.groupBox)
        self.meterCombo.setObjectName("meterCombo")
        self.gridLayout_2.addWidget(self.meterCombo, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)
        self.channelCombo = QtWidgets.QComboBox(self.groupBox)
        self.channelCombo.setObjectName("channelCombo")
        self.gridLayout_2.addWidget(self.channelCombo, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.pCellGroup = QtWidgets.QGroupBox(self.groupBox)
        self.pCellGroup.setAlignment(Qt.Qt.AlignCenter)
        self.pCellGroup.setObjectName("pCellGroup")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.pCellGroup)
        self.gridLayout_8.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(self.pCellGroup)
        self.label_9.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.minVSpin = SpinBox(self.pCellGroup)
        self.minVSpin.setMinimum(-99.0)
        self.minVSpin.setSingleStep(0.01)
        self.minVSpin.setProperty("value", -0.2)
        self.minVSpin.setObjectName("minVSpin")
        self.gridLayout_7.addWidget(self.minVSpin, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.pCellGroup)
        self.label_11.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 0, 2, 1, 1)
        self.stepsSpin = SpinBox(self.pCellGroup)
        self.stepsSpin.setDecimals(0)
        self.stepsSpin.setMinimum(10.0)
        self.stepsSpin.setMaximum(1000.0)
        self.stepsSpin.setProperty("value", 20.0)
        self.stepsSpin.setObjectName("stepsSpin")
        self.gridLayout_7.addWidget(self.stepsSpin, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.pCellGroup)
        self.label_10.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)
        self.maxVSpin = SpinBox(self.pCellGroup)
        self.maxVSpin.setSingleStep(0.01)
        self.maxVSpin.setProperty("value", 1.2)
        self.maxVSpin.setObjectName("maxVSpin")
        self.gridLayout_7.addWidget(self.maxVSpin, 2, 1, 1, 1)
        self.recalibratePCellCheck = QtWidgets.QCheckBox(self.pCellGroup)
        self.recalibratePCellCheck.setObjectName("recalibratePCellCheck")
        self.gridLayout_7.addWidget(self.recalibratePCellCheck, 2, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.pCellGroup, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 2, 0, 1, 5)
        self.deleteBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.deleteBtn.setObjectName("deleteBtn")
        self.gridLayout_6.addWidget(self.deleteBtn, 1, 4, 1, 1)
        self.calibrateBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.calibrateBtn.setObjectName("calibrateBtn")
        self.gridLayout_6.addWidget(self.calibrateBtn, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 4, 0, 1, 3)
        self.checkPowerBtn = QtWidgets.QPushButton(Form)
        self.checkPowerBtn.setObjectName("checkPowerBtn")
        self.gridLayout.addWidget(self.checkPowerBtn, 2, 0, 1, 1)
        self.shutterBtn = QtWidgets.QPushButton(Form)
        self.shutterBtn.setCheckable(True)
        self.shutterBtn.setObjectName("shutterBtn")
        self.gridLayout.addWidget(self.shutterBtn, 2, 1, 1, 1)
        self.qSwitchBtn = QtWidgets.QPushButton(Form)
        self.qSwitchBtn.setCheckable(True)
        self.qSwitchBtn.setObjectName("qSwitchBtn")
        self.gridLayout.addWidget(self.qSwitchBtn, 2, 2, 1, 1)

        self.retranslateUi(Form)
        Qt.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = Qt.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Expected Output Power:"))
        self.energyCalcGroup.setTitle(_translate("Form", "For energy calculations use:"))
        self.currentPowerRadio.setText(_translate("Form", "Current Power"))
        self.expectedPowerRadio.setText(_translate("Form", "Expected Power"))
        self.label_4.setText(_translate("Form", "Current Output Power:"))
        self.label_8.setText(_translate("Form", "Power at sample (calc.):"))
        self.powerAlertCheck.setText(_translate("Form", "Alert me to power changes larger than:"))
        self.label_7.setText(_translate("Form", "Current Wavelength: "))
        self.wavelengthCombo.setItemText(0, _translate("Form", "Set wavelength for:"))
        self.GDDEnableCheck.setText(_translate("Form", "GDD Enable"))
        self.GDDLimits.setText(_translate("Form", "GDD Limits"))
        self.groupBox_2.setTitle(_translate("Form", "Power Calibration"))
        self.calibrationList.headerItem().setText(0, _translate("Form", "Optics"))
        self.calibrationList.headerItem().setText(1, _translate("Form", "Wavelength"))
        self.calibrationList.headerItem().setText(2, _translate("Form", "Transmission"))
        self.calibrationList.headerItem().setText(3, _translate("Form", "Power at Sample"))
        self.calibrationList.headerItem().setText(4, _translate("Form", "Date"))
        self.groupBox.setTitle(_translate("Form", "Calibration Parameters"))
        self.scanLabel.setText(_translate("Form", "Measurement Duration"))
        self.measurementSpin.setSuffix(_translate("Form", " s"))
        self.label.setText(_translate("Form", "Settling Duration:"))
        self.settlingSpin.setToolTip(_translate("Form", "Specify the time it takes for the selected power meter to settle on a value."))
        self.label_3.setText(_translate("Form", "Power Meter:"))
        self.label_12.setText(_translate("Form", "Channel:"))
        self.pCellGroup.setTitle(_translate("Form", "Pockel Cell Parameters"))
        self.label_9.setText(_translate("Form", "Minimum Voltage:"))
        self.minVSpin.setSuffix(_translate("Form", "V"))
        self.label_11.setText(_translate("Form", "Number of Steps: "))
        self.label_10.setText(_translate("Form", "Maximum Voltage:"))
        self.maxVSpin.setSuffix(_translate("Form", "V"))
        self.recalibratePCellCheck.setText(_translate("Form", "Re-Calibrate Pockel Cell"))
        self.deleteBtn.setText(_translate("Form", "Delete"))
        self.calibrateBtn.setText(_translate("Form", "Calibrate"))
        self.checkPowerBtn.setText(_translate("Form", "Check Power"))
        self.shutterBtn.setText(_translate("Form", "Open Shutter"))
        self.qSwitchBtn.setText(_translate("Form", "Turn On QSwitch"))

from acq4.pyqtgraph import SpinBox
from acq4.util.InterfaceCombo import InterfaceCombo
