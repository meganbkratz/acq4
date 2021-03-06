# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acq4/analysis/modules/CellHealthTracker/CellHealthCtrlTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(232, 259)
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.methodCombo = QtWidgets.QComboBox(widget)
        self.methodCombo.setMinimumSize(Qt.QSize(158, 0))
        self.methodCombo.setObjectName("methodCombo")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.methodCombo.addItem("")
        self.horizontalLayout.addWidget(self.methodCombo)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_3.setSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.startSpin = SpinBox(self.groupBox_2)
        self.startSpin.setObjectName("startSpin")
        self.gridLayout_3.addWidget(self.startSpin, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(Qt.Qt.AlignRight|Qt.Qt.AlignTrailing|Qt.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.stopSpin = SpinBox(self.groupBox_2)
        self.stopSpin.setObjectName("stopSpin")
        self.gridLayout_3.addWidget(self.stopSpin, 2, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setSpacing(3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.RsCheck = QtWidgets.QCheckBox(self.groupBox)
        self.RsCheck.setObjectName("RsCheck")
        self.gridLayout_2.addWidget(self.RsCheck, 2, 0, 1, 1)
        self.IhCheck = QtWidgets.QCheckBox(self.groupBox)
        self.IhCheck.setObjectName("IhCheck")
        self.gridLayout_2.addWidget(self.IhCheck, 1, 0, 1, 1)
        self.RmCheck = QtWidgets.QCheckBox(self.groupBox)
        self.RmCheck.setObjectName("RmCheck")
        self.gridLayout_2.addWidget(self.RmCheck, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)
        self.processBtn = QtWidgets.QPushButton(widget)
        self.processBtn.setObjectName("processBtn")
        self.gridLayout.addWidget(self.processBtn, 3, 0, 1, 1)
        self.saveBtn = QtWidgets.QPushButton(widget)
        self.saveBtn.setObjectName("saveBtn")
        self.gridLayout.addWidget(self.saveBtn, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 2)

        self.retranslateUi(widget)
        Qt.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = Qt.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label_4.setText(_translate("widget", "Method:"))
        self.methodCombo.setItemText(0, _translate("widget", "Simple Ohm\'s law"))
        self.methodCombo.setItemText(1, _translate("widget", "Santos-Sacchi raw"))
        self.methodCombo.setItemText(2, _translate("widget", "Santos-Sacchi fit"))
        self.groupBox_2.setTitle(_translate("widget", "Measurement region:"))
        self.label_2.setText(_translate("widget", "Start:"))
        self.label_3.setText(_translate("widget", "Stop: "))
        self.groupBox.setTitle(_translate("widget", "Parameters to measure:"))
        self.RsCheck.setText(_translate("widget", "Series Resistance"))
        self.IhCheck.setText(_translate("widget", "Holding Current"))
        self.RmCheck.setText(_translate("widget", "Membrane Resistance"))
        self.processBtn.setToolTip(_translate("widget", "Measure parameters for the currently selected file."))
        self.processBtn.setText(_translate("widget", "Process"))
        self.saveBtn.setToolTip(_translate("widget", "Save the data currently displayed in the Ih, Rs, and Rm plots."))
        self.saveBtn.setText(_translate("widget", "Save plots"))

from acq4.pyqtgraph.widgets.SpinBox import SpinBox
