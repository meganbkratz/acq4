# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/util/FileLoader/template.ui'
#
# Created: Fri Mar  9 11:10:28 2012
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
        Form.resize(361, 557)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.setDirBtn = QtGui.QPushButton(self.layoutWidget)
        self.setDirBtn.setObjectName(_fromUtf8("setDirBtn"))
        self.verticalLayout.addWidget(self.setDirBtn)
        self.dirTree = DirTreeWidget(self.layoutWidget)
        self.dirTree.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.dirTree.setHeaderHidden(True)
        self.dirTree.setObjectName(_fromUtf8("dirTree"))
        self.dirTree.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout.addWidget(self.dirTree)
        self.layoutWidget1 = QtGui.QWidget(self.splitter)
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.loadBtn = QtGui.QPushButton(self.layoutWidget1)
        self.loadBtn.setObjectName(_fromUtf8("loadBtn"))
        self.verticalLayout_2.addWidget(self.loadBtn)
        self.fileTree = QtGui.QTreeWidget(self.layoutWidget1)
        self.fileTree.setHeaderHidden(True)
        self.fileTree.setObjectName(_fromUtf8("fileTree"))
        self.fileTree.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_2.addWidget(self.fileTree)
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.notesTextEdit = QtGui.QTextEdit(self.layoutWidget1)
        self.notesTextEdit.setObjectName(_fromUtf8("notesTextEdit"))
        self.verticalLayout_2.addWidget(self.notesTextEdit)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.setDirBtn.setText(QtGui.QApplication.translate("Form", "Set Base Dir ->", None, QtGui.QApplication.UnicodeUTF8))
        self.loadBtn.setText(QtGui.QApplication.translate("Form", "Load File ->", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Notes:", None, QtGui.QApplication.UnicodeUTF8))

from DirTreeWidget import DirTreeWidget
