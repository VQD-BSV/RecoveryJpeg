# Form implementation generated from reading ui file 'Create.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Create_New(object):
    def setupUi(self, Create_New):
        Create_New.setObjectName("Create_New")
        Create_New.resize(454, 228)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo/logo.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Create_New.setWindowIcon(icon)
        self.checkBox = QtWidgets.QCheckBox(parent=Create_New)
        self.checkBox.setGeometry(QtCore.QRect(10, 170, 261, 20))
        self.checkBox.setObjectName("checkBox")
        self.listWidget = QtWidgets.QListWidget(parent=Create_New)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 381, 151))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.b_Save = QtWidgets.QPushButton(parent=Create_New)
        self.b_Save.setGeometry(QtCore.QRect(400, 10, 42, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.b_Save.setFont(font)
        self.b_Save.setObjectName("b_Save")
        self.b_Save_2 = QtWidgets.QPushButton(parent=Create_New)
        self.b_Save_2.setGeometry(QtCore.QRect(400, 40, 42, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.b_Save_2.setFont(font)
        self.b_Save_2.setObjectName("b_Save_2")
        self.b_OK = QtWidgets.QPushButton(parent=Create_New)
        self.b_OK.setGeometry(QtCore.QRect(290, 190, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.b_OK.setFont(font)
        self.b_OK.setObjectName("b_OK")
        self.b_Cancel = QtWidgets.QPushButton(parent=Create_New)
        self.b_Cancel.setGeometry(QtCore.QRect(370, 190, 75, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.b_Cancel.setFont(font)
        self.b_Cancel.setObjectName("b_Cancel")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=Create_New)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 190, 151, 20))
        self.checkBox_2.setObjectName("checkBox_2")

        self.retranslateUi(Create_New)
        QtCore.QMetaObject.connectSlotsByName(Create_New)

    def retranslateUi(self, Create_New):
        _translate = QtCore.QCoreApplication.translate
        Create_New.setWindowTitle(_translate("Create_New", "Prototype"))
        self.checkBox.setText(_translate("Create_New", "The file encrypted by ransomware - x25805"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Create_New", "Auto"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.b_Save.setText(_translate("Create_New", "+"))
        self.b_Save_2.setText(_translate("Create_New", "-"))
        self.b_OK.setText(_translate("Create_New", "OK"))
        self.b_Cancel.setText(_translate("Create_New", "Cancel"))
        self.checkBox_2.setText(_translate("Create_New", "Skip thumbnail"))
