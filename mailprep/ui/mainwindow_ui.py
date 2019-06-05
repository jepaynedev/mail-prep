# -*- coding: utf-8 -*-

# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_MailPrep(object):
    def setupUi(self, MainWindow_MailPrep):
        MainWindow_MailPrep.setObjectName("MainWindow_MailPrep")
        MainWindow_MailPrep.resize(659, 397)
        MainWindow_MailPrep.setMinimumSize(QtCore.QSize(659, 397))
        self.centralwidget = QtWidgets.QWidget(MainWindow_MailPrep)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageLanding = QtWidgets.QWidget()
        self.pageLanding.setObjectName("pageLanding")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pageLanding)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_landing = QtWidgets.QFormLayout()
        self.formLayout_landing.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_landing.setObjectName("formLayout_landing")
        self.label_jobNumber = QtWidgets.QLabel(self.pageLanding)
        self.label_jobNumber.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_jobNumber.setObjectName("label_jobNumber")
        self.formLayout_landing.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_jobNumber)
        self.lineEdit_jobNumber = QtWidgets.QLineEdit(self.pageLanding)
        self.lineEdit_jobNumber.setObjectName("lineEdit_jobNumber")
        self.formLayout_landing.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_jobNumber)
        self.label_title = QtWidgets.QLabel(self.pageLanding)
        self.label_title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title.setObjectName("label_title")
        self.formLayout_landing.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_title)
        self.lineEdit_title = QtWidgets.QLineEdit(self.pageLanding)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.formLayout_landing.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_title)
        self.label_department = QtWidgets.QLabel(self.pageLanding)
        self.label_department.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_department.setObjectName("label_department")
        self.formLayout_landing.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_department)
        self.lineEdit_department = QtWidgets.QLineEdit(self.pageLanding)
        self.lineEdit_department.setObjectName("lineEdit_department")
        self.formLayout_landing.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_department)
        self.label_customer = QtWidgets.QLabel(self.pageLanding)
        self.label_customer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_customer.setObjectName("label_customer")
        self.formLayout_landing.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_customer)
        self.lineEdit_customer = QtWidgets.QLineEdit(self.pageLanding)
        self.lineEdit_customer.setObjectName("lineEdit_customer")
        self.formLayout_landing.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_customer)
        self.verticalLayout.addLayout(self.formLayout_landing)
        self.pushButton_createOpen = QtWidgets.QPushButton(self.pageLanding)
        self.pushButton_createOpen.setEnabled(False)
        self.pushButton_createOpen.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_createOpen.setObjectName("pushButton_createOpen")
        self.verticalLayout.addWidget(self.pushButton_createOpen)
        self.stackedWidget.addWidget(self.pageLanding)
        self.pageJob = QtWidgets.QWidget()
        self.pageJob.setObjectName("pageJob")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pageJob)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_fileInputColumn = QtWidgets.QVBoxLayout()
        self.verticalLayout_fileInputColumn.setObjectName("verticalLayout_fileInputColumn")
        self.pushButton_addFiles = QtWidgets.QPushButton(self.pageJob)
        self.pushButton_addFiles.setObjectName("pushButton_addFiles")
        self.verticalLayout_fileInputColumn.addWidget(self.pushButton_addFiles)
        self.scrollArea_files = QtWidgets.QScrollArea(self.pageJob)
        self.scrollArea_files.setMinimumSize(QtCore.QSize(328, 0))
        self.scrollArea_files.setWidgetResizable(True)
        self.scrollArea_files.setObjectName("scrollArea_files")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 312, 20))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_files = QtWidgets.QVBoxLayout()
        self.verticalLayout_files.setObjectName("verticalLayout_files")
        self.verticalLayout_4.addLayout(self.verticalLayout_files)
        self.scrollArea_files.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_fileInputColumn.addWidget(self.scrollArea_files)
        self.horizontalLayout_2.addLayout(self.verticalLayout_fileInputColumn)
        self.formLayout_jobControls = QtWidgets.QFormLayout()
        self.formLayout_jobControls.setObjectName("formLayout_jobControls")
        self.label_convertUpper = QtWidgets.QLabel(self.pageJob)
        self.label_convertUpper.setObjectName("label_convertUpper")
        self.formLayout_jobControls.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_convertUpper)
        self.checkBox_convertUpper = QtWidgets.QCheckBox(self.pageJob)
        self.checkBox_convertUpper.setText("")
        self.checkBox_convertUpper.setObjectName("checkBox_convertUpper")
        self.formLayout_jobControls.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox_convertUpper)
        self.label_markCustomCampus = QtWidgets.QLabel(self.pageJob)
        self.label_markCustomCampus.setObjectName("label_markCustomCampus")
        self.formLayout_jobControls.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_markCustomCampus)
        self.checkBox_markCustomCampus = QtWidgets.QCheckBox(self.pageJob)
        self.checkBox_markCustomCampus.setText("")
        self.checkBox_markCustomCampus.setObjectName("checkBox_markCustomCampus")
        self.formLayout_jobControls.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_markCustomCampus)
        self.label_customCampusFile = QtWidgets.QLabel(self.pageJob)
        self.label_customCampusFile.setObjectName("label_customCampusFile")
        self.formLayout_jobControls.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_customCampusFile)
        self.horizontalLayout_customCampusFile = QtWidgets.QHBoxLayout()
        self.horizontalLayout_customCampusFile.setObjectName("horizontalLayout_customCampusFile")
        self.lineEdit_customCampusFile = QtWidgets.QLineEdit(self.pageJob)
        self.lineEdit_customCampusFile.setObjectName("lineEdit_customCampusFile")
        self.horizontalLayout_customCampusFile.addWidget(self.lineEdit_customCampusFile)
        self.pushButton_browseCustomCampus = QtWidgets.QPushButton(self.pageJob)
        self.pushButton_browseCustomCampus.setObjectName("pushButton_browseCustomCampus")
        self.horizontalLayout_customCampusFile.addWidget(self.pushButton_browseCustomCampus)
        self.formLayout_jobControls.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_customCampusFile)
        self.horizontalLayout_2.addLayout(self.formLayout_jobControls)
        self.stackedWidget.addWidget(self.pageJob)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow_MailPrep.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_MailPrep)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 659, 20))
        self.menubar.setObjectName("menubar")
        self.menu_MailPrep = QtWidgets.QMenu(self.menubar)
        self.menu_MailPrep.setObjectName("menu_MailPrep")
        MainWindow_MailPrep.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_MailPrep)
        self.statusbar.setObjectName("statusbar")
        MainWindow_MailPrep.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow_MailPrep)
        self.actionExit.setObjectName("actionExit")
        self.actionBrowseCustomCampus = QtWidgets.QAction(MainWindow_MailPrep)
        self.actionBrowseCustomCampus.setObjectName("actionBrowseCustomCampus")
        self.actionOpenJob = QtWidgets.QAction(MainWindow_MailPrep)
        self.actionOpenJob.setObjectName("actionOpenJob")
        self.actionCloseJob = QtWidgets.QAction(MainWindow_MailPrep)
        self.actionCloseJob.setObjectName("actionCloseJob")
        self.actionClose = QtWidgets.QAction(MainWindow_MailPrep)
        self.actionClose.setEnabled(False)
        self.actionClose.setObjectName("actionClose")
        self.actionAddFiles = QtWidgets.QAction(MainWindow_MailPrep)
        self.actionAddFiles.setObjectName("actionAddFiles")
        self.menu_MailPrep.addAction(self.actionClose)
        self.menu_MailPrep.addSeparator()
        self.menu_MailPrep.addAction(self.actionExit)
        self.menubar.addAction(self.menu_MailPrep.menuAction())

        self.retranslateUi(MainWindow_MailPrep)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.lineEdit_jobNumber, QtCore.SIGNAL("returnPressed()"), self.lineEdit_title.setFocus)
        QtCore.QObject.connect(self.lineEdit_customer, QtCore.SIGNAL("returnPressed()"), self.pushButton_createOpen.setFocus)
        QtCore.QObject.connect(self.lineEdit_department, QtCore.SIGNAL("returnPressed()"), self.lineEdit_customer.setFocus)
        QtCore.QObject.connect(self.lineEdit_title, QtCore.SIGNAL("returnPressed()"), self.lineEdit_department.setFocus)
        QtCore.QObject.connect(self.pushButton_browseCustomCampus, QtCore.SIGNAL("clicked()"), self.actionBrowseCustomCampus.trigger)
        QtCore.QObject.connect(self.pushButton_createOpen, QtCore.SIGNAL("clicked()"), self.actionOpenJob.trigger)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow_MailPrep.close)
        QtCore.QObject.connect(self.pushButton_addFiles, QtCore.SIGNAL("clicked()"), self.actionAddFiles.trigger)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_MailPrep)

    def retranslateUi(self, MainWindow_MailPrep):
        MainWindow_MailPrep.setWindowTitle(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Mail Prep", None, -1))
        self.label_jobNumber.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Job Number", None, -1))
        self.label_title.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Title", None, -1))
        self.label_department.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Department", None, -1))
        self.label_customer.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Customer", None, -1))
        self.pushButton_createOpen.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Create / Open", None, -1))
        self.pushButton_addFiles.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Add Files", None, -1))
        self.label_convertUpper.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Convert to Upper Case", None, -1))
        self.label_markCustomCampus.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Mark Custom Campus", None, -1))
        self.label_customCampusFile.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Custom Campus File", None, -1))
        self.pushButton_browseCustomCampus.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Browse", None, -1))
        self.menu_MailPrep.setTitle(QtWidgets.QApplication.translate("MainWindow_MailPrep", "File", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "E&xit", None, -1))
        self.actionBrowseCustomCampus.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "BrowseCustomCampus", None, -1))
        self.actionBrowseCustomCampus.setToolTip(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Browse Custom Campus", None, -1))
        self.actionOpenJob.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "OpenJob", None, -1))
        self.actionOpenJob.setToolTip(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Create / Open Job", None, -1))
        self.actionCloseJob.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "CloseJob", None, -1))
        self.actionCloseJob.setToolTip(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Close Job", None, -1))
        self.actionCloseJob.setShortcut(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Ctrl+W", None, -1))
        self.actionClose.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "&Close", None, -1))
        self.actionAddFiles.setText(QtWidgets.QApplication.translate("MainWindow_MailPrep", "AddFiles", None, -1))
        self.actionAddFiles.setToolTip(QtWidgets.QApplication.translate("MainWindow_MailPrep", "Add Files", None, -1))

