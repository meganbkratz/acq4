# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/util/pyqtgraph/graphicsItems/PlotItem/plotConfigTemplate.ui'
#
# Created: Fri Mar  9 11:10:29 2012
#      by: PyQt4 UI code generator 4.8.3
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
        Form.resize(258, 605)
        self.averageGroup = QtGui.QGroupBox(Form)
        self.averageGroup.setGeometry(QtCore.QRect(10, 200, 242, 182))
        self.averageGroup.setCheckable(True)
        self.averageGroup.setChecked(False)
        self.averageGroup.setObjectName(_fromUtf8("averageGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.averageGroup)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.avgParamList = QtGui.QListWidget(self.averageGroup)
        self.avgParamList.setObjectName(_fromUtf8("avgParamList"))
        self.gridLayout_5.addWidget(self.avgParamList, 0, 0, 1, 1)
        self.decimateGroup = QtGui.QGroupBox(Form)
        self.decimateGroup.setGeometry(QtCore.QRect(0, 30, 242, 160))
        self.decimateGroup.setCheckable(True)
        self.decimateGroup.setObjectName(_fromUtf8("decimateGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.decimateGroup)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.manualDecimateRadio = QtGui.QRadioButton(self.decimateGroup)
        self.manualDecimateRadio.setChecked(True)
        self.manualDecimateRadio.setObjectName(_fromUtf8("manualDecimateRadio"))
        self.gridLayout_4.addWidget(self.manualDecimateRadio, 0, 0, 1, 1)
        self.downsampleSpin = QtGui.QSpinBox(self.decimateGroup)
        self.downsampleSpin.setMinimum(1)
        self.downsampleSpin.setMaximum(100000)
        self.downsampleSpin.setProperty(_fromUtf8("value"), 1)
        self.downsampleSpin.setObjectName(_fromUtf8("downsampleSpin"))
        self.gridLayout_4.addWidget(self.downsampleSpin, 0, 1, 1, 1)
        self.autoDecimateRadio = QtGui.QRadioButton(self.decimateGroup)
        self.autoDecimateRadio.setChecked(False)
        self.autoDecimateRadio.setObjectName(_fromUtf8("autoDecimateRadio"))
        self.gridLayout_4.addWidget(self.autoDecimateRadio, 1, 0, 1, 1)
        self.maxTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.maxTracesCheck.setObjectName(_fromUtf8("maxTracesCheck"))
        self.gridLayout_4.addWidget(self.maxTracesCheck, 2, 0, 1, 1)
        self.maxTracesSpin = QtGui.QSpinBox(self.decimateGroup)
        self.maxTracesSpin.setObjectName(_fromUtf8("maxTracesSpin"))
        self.gridLayout_4.addWidget(self.maxTracesSpin, 2, 1, 1, 1)
        self.forgetTracesCheck = QtGui.QCheckBox(self.decimateGroup)
        self.forgetTracesCheck.setObjectName(_fromUtf8("forgetTracesCheck"))
        self.gridLayout_4.addWidget(self.forgetTracesCheck, 3, 0, 1, 2)
        self.powerSpectrumGroup = QtGui.QGroupBox(Form)
        self.powerSpectrumGroup.setGeometry(QtCore.QRect(0, 0, 242, 41))
        self.powerSpectrumGroup.setCheckable(True)
        self.powerSpectrumGroup.setChecked(False)
        self.powerSpectrumGroup.setObjectName(_fromUtf8("powerSpectrumGroup"))
        self.pointsGroup = QtGui.QGroupBox(Form)
        self.pointsGroup.setGeometry(QtCore.QRect(10, 520, 234, 58))
        self.pointsGroup.setCheckable(True)
        self.pointsGroup.setObjectName(_fromUtf8("pointsGroup"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.pointsGroup)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.autoPointsCheck = QtGui.QCheckBox(self.pointsGroup)
        self.autoPointsCheck.setChecked(True)
        self.autoPointsCheck.setObjectName(_fromUtf8("autoPointsCheck"))
        self.verticalLayout_5.addWidget(self.autoPointsCheck)
        self.gridGroup = QtGui.QGroupBox(Form)
        self.gridGroup.setGeometry(QtCore.QRect(10, 460, 234, 60))
        self.gridGroup.setCheckable(True)
        self.gridGroup.setChecked(False)
        self.gridGroup.setObjectName(_fromUtf8("gridGroup"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gridGroup)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridAlphaSlider = QtGui.QSlider(self.gridGroup)
        self.gridAlphaSlider.setMaximum(255)
        self.gridAlphaSlider.setProperty(_fromUtf8("value"), 70)
        self.gridAlphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.gridAlphaSlider.setObjectName(_fromUtf8("gridAlphaSlider"))
        self.verticalLayout_4.addWidget(self.gridAlphaSlider)
        self.alphaGroup = QtGui.QGroupBox(Form)
        self.alphaGroup.setGeometry(QtCore.QRect(10, 390, 234, 60))
        self.alphaGroup.setCheckable(True)
        self.alphaGroup.setObjectName(_fromUtf8("alphaGroup"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.alphaGroup)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.autoAlphaCheck = QtGui.QCheckBox(self.alphaGroup)
        self.autoAlphaCheck.setChecked(False)
        self.autoAlphaCheck.setObjectName(_fromUtf8("autoAlphaCheck"))
        self.horizontalLayout.addWidget(self.autoAlphaCheck)
        self.alphaSlider = QtGui.QSlider(self.alphaGroup)
        self.alphaSlider.setMaximum(1000)
        self.alphaSlider.setProperty(_fromUtf8("value"), 1000)
        self.alphaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.alphaSlider.setObjectName(_fromUtf8("alphaSlider"))
        self.horizontalLayout.addWidget(self.alphaSlider)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.averageGroup.setToolTip(QtGui.QApplication.translate("Form", "Display averages of the curves displayed in this plot. The parameter list allows you to choose parameters to average over (if any are available).", None, QtGui.QApplication.UnicodeUTF8))
        self.averageGroup.setTitle(QtGui.QApplication.translate("Form", "Average", None, QtGui.QApplication.UnicodeUTF8))
        self.decimateGroup.setTitle(QtGui.QApplication.translate("Form", "Downsample", None, QtGui.QApplication.UnicodeUTF8))
        self.manualDecimateRadio.setText(QtGui.QApplication.translate("Form", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.autoDecimateRadio.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesCheck.setToolTip(QtGui.QApplication.translate("Form", "If multiple curves are displayed in this plot, check this box to limit the number of traces that are displayed.", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesCheck.setText(QtGui.QApplication.translate("Form", "Max Traces:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxTracesSpin.setToolTip(QtGui.QApplication.translate("Form", "If multiple curves are displayed in this plot, check \"Max Traces\" and set this value to limit the number of traces that are displayed.", None, QtGui.QApplication.UnicodeUTF8))
        self.forgetTracesCheck.setToolTip(QtGui.QApplication.translate("Form", "If MaxTraces is checked, remove curves from memory after they are hidden (saves memory, but traces can not be un-hidden).", None, QtGui.QApplication.UnicodeUTF8))
        self.forgetTracesCheck.setText(QtGui.QApplication.translate("Form", "Forget hidden traces", None, QtGui.QApplication.UnicodeUTF8))
        self.powerSpectrumGroup.setTitle(QtGui.QApplication.translate("Form", "Power Spectrum", None, QtGui.QApplication.UnicodeUTF8))
        self.pointsGroup.setTitle(QtGui.QApplication.translate("Form", "Points", None, QtGui.QApplication.UnicodeUTF8))
        self.autoPointsCheck.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))
        self.gridGroup.setTitle(QtGui.QApplication.translate("Form", "Grid", None, QtGui.QApplication.UnicodeUTF8))
        self.alphaGroup.setTitle(QtGui.QApplication.translate("Form", "Alpha", None, QtGui.QApplication.UnicodeUTF8))
        self.autoAlphaCheck.setText(QtGui.QApplication.translate("Form", "Auto", None, QtGui.QApplication.UnicodeUTF8))

