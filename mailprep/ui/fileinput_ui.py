# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'P:\Projects\MailPrep\ui\fileinput.ui',
# licensing of 'P:\Projects\MailPrep\ui\fileinput.ui' applies.
#
# Created: Wed May 22 22:55:18 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_FileInput(object):
    def setupUi(self, FileInput):
        FileInput.setObjectName("FileInput")
        FileInput.resize(294, 107)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FileInput.sizePolicy().hasHeightForWidth())
        FileInput.setSizePolicy(sizePolicy)
        FileInput.setMinimumSize(QtCore.QSize(294, 107))
        FileInput.setMaximumSize(QtCore.QSize(16777215, 107))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FileInput)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(FileInput)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_priority = QtWidgets.QLabel(self.frame)
        self.label_priority.setObjectName("label_priority")
        self.gridLayout.addWidget(self.label_priority, 1, 3, 1, 1)
        self.lineEdit_listId = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_listId.setObjectName("lineEdit_listId")
        self.gridLayout.addWidget(self.lineEdit_listId, 1, 2, 1, 1)
        self.label_listId = QtWidgets.QLabel(self.frame)
        self.label_listId.setObjectName("label_listId")
        self.gridLayout.addWidget(self.label_listId, 1, 1, 1, 1)
        self.comboBox_listType = QtWidgets.QComboBox(self.frame)
        self.comboBox_listType.setObjectName("comboBox_listType")
        self.comboBox_listType.addItem("")
        self.comboBox_listType.addItem("")
        self.comboBox_listType.addItem("")
        self.comboBox_listType.addItem("")
        self.gridLayout.addWidget(self.comboBox_listType, 0, 3, 1, 2)
        self.lineEdit_priority = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_priority.setObjectName("lineEdit_priority")
        self.gridLayout.addWidget(self.lineEdit_priority, 1, 4, 1, 2)
        self.pushButton_removeFile = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_removeFile.sizePolicy().hasHeightForWidth())
        self.pushButton_removeFile.setSizePolicy(sizePolicy)
        self.pushButton_removeFile.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_removeFile.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_removeFile.setBaseSize(QtCore.QSize(20, 20))
        self.pushButton_removeFile.setObjectName("pushButton_removeFile")
        self.gridLayout.addWidget(self.pushButton_removeFile, 0, 5, 1, 1)
        self.lineEdit_fileName = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.lineEdit_fileName.setFont(font)
        self.lineEdit_fileName.setReadOnly(True)
        self.lineEdit_fileName.setObjectName("lineEdit_fileName")
        self.gridLayout.addWidget(self.lineEdit_fileName, 0, 1, 1, 2)
        self.verticalLayout_2.addWidget(self.frame)

        self.retranslateUi(FileInput)
        QtCore.QMetaObject.connectSlotsByName(FileInput)

    def retranslateUi(self, FileInput):
        FileInput.setWindowTitle(QtWidgets.QApplication.translate("FileInput", "Form", None, -1))
        self.label_priority.setText(QtWidgets.QApplication.translate("FileInput", "Priority", None, -1))
        self.label_listId.setText(QtWidgets.QApplication.translate("FileInput", "List ID", None, -1))
        self.comboBox_listType.setItemText(0, QtWidgets.QApplication.translate("FileInput", "Normal", None, -1))
        self.comboBox_listType.setItemText(1, QtWidgets.QApplication.translate("FileInput", "Suppression", None, -1))
        self.comboBox_listType.setItemText(2, QtWidgets.QApplication.translate("FileInput", "Foreign", None, -1))
        self.comboBox_listType.setItemText(3, QtWidgets.QApplication.translate("FileInput", "Campus", None, -1))
        self.pushButton_removeFile.setToolTip(QtWidgets.QApplication.translate("FileInput", "Remove File", None, -1))
        self.pushButton_removeFile.setText(QtWidgets.QApplication.translate("FileInput", "X", None, -1))
