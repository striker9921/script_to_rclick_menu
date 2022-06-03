# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_project.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

    project_name = "New Project"
    project_path = ""

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(303, 388)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WindowVLayout = QtWidgets.QVBoxLayout()
        self.WindowVLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.WindowVLayout.setContentsMargins(5, 5, 5, 5)
        self.WindowVLayout.setSpacing(5)

        self.WindowVLayout.setObjectName("WindowVLayout")
        self.ProjectInfoVLayout = QtWidgets.QVBoxLayout()
        
        self.ProjectInfoVLayout.setObjectName("ProjectInfoVLayout")
        self.ProjectNameHLayout = QtWidgets.QHBoxLayout()

        self.ProjectNameHLayout.setObjectName("ProjectNameHLayout")
        self.ProjectNameLabelTitle = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.ProjectNameLabelTitle.setFont(font)
        self.ProjectNameLabelTitle.setObjectName("ProjectNameLabelTitle")
        self.ProjectNameHLayout.addWidget(self.ProjectNameLabelTitle)
        self.ProjectNameLineEdit = QtWidgets.QLineEdit(Dialog)
        self.ProjectNameLineEdit.setMinimumSize(QtCore.QSize(183, 19))
        self.ProjectNameLineEdit.setMaximumSize(QtCore.QSize(183, 19))
        self.ProjectNameLineEdit.setObjectName("ProjectNameLineEdit")
        self.ProjectNameHLayout.addWidget(self.ProjectNameLineEdit)
        self.ProjectInfoVLayout.addLayout(self.ProjectNameHLayout)
        self.ProjectPathHLayout = QtWidgets.QHBoxLayout()
        self.ProjectPathHLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)

        self.ProjectPathHLayout.setObjectName("ProjectPathHLayout")
        self.ProjectPathLabelTitle = QtWidgets.QLabel(Dialog)
        self.ProjectPathLabelTitle.setMinimumSize(QtCore.QSize(0, 0))
        self.ProjectPathLabelTitle.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.ProjectPathLabelTitle.setFont(font)
        self.ProjectPathLabelTitle.setObjectName("ProjectPathLabelTitle")
        self.ProjectPathHLayout.addWidget(self.ProjectPathLabelTitle)
        self.SelectPathButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectPathButton.sizePolicy().hasHeightForWidth())
        self.SelectPathButton.setSizePolicy(sizePolicy)
        self.SelectPathButton.setMinimumSize(QtCore.QSize(183, 0))
        self.SelectPathButton.setMaximumSize(QtCore.QSize(183, 30))
        self.SelectPathButton.setObjectName("SelectPathButton")
        self.ProjectPathHLayout.addWidget(self.SelectPathButton)
        self.ProjectInfoVLayout.addLayout(self.ProjectPathHLayout)
        self.FinalProjectPathLabelHLayout = QtWidgets.QHBoxLayout()

        self.FinalProjectPathLabelHLayout.setObjectName("FinalProjectPathLabelHLayout")
        self.FinalProjectPathLabelTitle = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.FinalProjectPathLabelTitle.setFont(font)
        self.FinalProjectPathLabelTitle.setObjectName("FinalProjectPathLabelTitle")
        self.FinalProjectPathLabelHLayout.addWidget(self.FinalProjectPathLabelTitle)
        self.ProjectInfoVLayout.addLayout(self.FinalProjectPathLabelHLayout)
        self.FinalProjectPathHLayout = QtWidgets.QHBoxLayout()

        self.FinalProjectPathHLayout.setObjectName("FinalProjectPathHLayout")
        self.FinalProjectPathLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.FinalProjectPathLabel.setFont(font)
        self.FinalProjectPathLabel.setObjectName("FinalProjectPathLabel")
        self.FinalProjectPathHLayout.addWidget(self.FinalProjectPathLabel)
        self.ProjectInfoVLayout.addLayout(self.FinalProjectPathHLayout)
        self.WindowVLayout.addLayout(self.ProjectInfoVLayout)
        self.InnerFolderVLayout = QtWidgets.QVBoxLayout()
        
        self.InnerFolderVLayout.setObjectName("InnerFolderVLayout")
        self.InnerFolderHLayout01 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout01.setObjectName("InnerFolderHLayout01")
        self.InnerFolderCheckbox01 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox01.setObjectName("InnerFolderCheckbox01")
        self.InnerFolderHLayout01.addWidget(self.InnerFolderCheckbox01)
        self.InnerFolderNameLine01 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine01.setObjectName("InnerFolderNameLine01")
        self.InnerFolderHLayout01.addWidget(self.InnerFolderNameLine01)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout01)
        self.InnerFolderHLayout02 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout02.setObjectName("InnerFolderHLayout02")
        self.InnerFolderCheckbox02 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox02.setObjectName("InnerFolderCheckbox02")
        self.InnerFolderHLayout02.addWidget(self.InnerFolderCheckbox02)
        self.InnerFolderNameLine02 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine02.setObjectName("InnerFolderNameLine02")
        self.InnerFolderHLayout02.addWidget(self.InnerFolderNameLine02)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout02)
        self.InnerFolderHLayout03 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout03.setObjectName("InnerFolderHLayout03")
        self.InnerFolderCheckbox03 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox03.setObjectName("InnerFolderCheckbox03")
        self.InnerFolderHLayout03.addWidget(self.InnerFolderCheckbox03)
        self.InnerFolderNameLine03 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine03.setObjectName("InnerFolderNameLine03")
        self.InnerFolderHLayout03.addWidget(self.InnerFolderNameLine03)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout03)
        self.InnerFolderHLayout04 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout04.setObjectName("InnerFolderHLayout04")
        self.InnerFolderCheckbox04 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox04.setObjectName("InnerFolderCheckbox04")
        self.InnerFolderHLayout04.addWidget(self.InnerFolderCheckbox04)
        self.InnerFolderNameLine04 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine04.setObjectName("InnerFolderNameLine04")
        self.InnerFolderHLayout04.addWidget(self.InnerFolderNameLine04)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout04)
        self.InnerFolderHLayout05 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout05.setObjectName("InnerFolderHLayout05")
        self.InnerFolderCheckbox05 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox05.setObjectName("InnerFolderCheckbox05")
        self.InnerFolderHLayout05.addWidget(self.InnerFolderCheckbox05)
        self.InnerFolderNameLine05 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine05.setObjectName("InnerFolderNameLine05")
        self.InnerFolderHLayout05.addWidget(self.InnerFolderNameLine05)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout05)
        self.InnerFolderHLayout06 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout06.setObjectName("InnerFolderHLayout06")
        self.InnerFolderCheckbox06 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox06.setObjectName("InnerFolderCheckbox06")
        self.InnerFolderHLayout06.addWidget(self.InnerFolderCheckbox06)
        self.InnerFolderNameLine06 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine06.setObjectName("InnerFolderNameLine06")
        self.InnerFolderHLayout06.addWidget(self.InnerFolderNameLine06)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout06)
        self.InnerFolderHLayout07 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout07.setObjectName("InnerFolderHLayout07")
        self.InnerFolderCheckbox07 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox07.setObjectName("InnerFolderCheckbox07")
        self.InnerFolderHLayout07.addWidget(self.InnerFolderCheckbox07)
        self.InnerFolderNameLine07 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine07.setObjectName("InnerFolderNameLine07")
        self.InnerFolderHLayout07.addWidget(self.InnerFolderNameLine07)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout07)
        self.InnerFolderHLayout08 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout08.setObjectName("InnerFolderHLayout08")
        self.InnerFolderCheckbox08 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox08.setObjectName("InnerFolderCheckbox08")
        self.InnerFolderHLayout08.addWidget(self.InnerFolderCheckbox08)
        self.InnerFolderNameLine08 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine08.setObjectName("InnerFolderNameLine08")
        self.InnerFolderHLayout08.addWidget(self.InnerFolderNameLine08)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout08)
        self.InnerFolderHLayout09 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout09.setObjectName("InnerFolderHLayout09")
        self.InnerFolderCheckbox09 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox09.setObjectName("InnerFolderCheckbox09")
        self.InnerFolderHLayout09.addWidget(self.InnerFolderCheckbox09)
        self.InnerFolderNameLine09 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine09.setObjectName("InnerFolderNameLine09")
        self.InnerFolderHLayout09.addWidget(self.InnerFolderNameLine09)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout09)
        self.InnerFolderHLayout10 = QtWidgets.QHBoxLayout()
        self.InnerFolderHLayout10.setObjectName("InnerFolderHLayout10")
        self.InnerFolderCheckbox10 = QtWidgets.QCheckBox(Dialog)
        self.InnerFolderCheckbox10.setObjectName("InnerFolderCheckbox10")
        self.InnerFolderHLayout10.addWidget(self.InnerFolderCheckbox10)
        self.InnerFolderNameLine10 = QtWidgets.QLineEdit(Dialog)
        self.InnerFolderNameLine10.setObjectName("InnerFolderNameLine10")
        self.InnerFolderHLayout10.addWidget(self.InnerFolderNameLine10)
        self.InnerFolderVLayout.addLayout(self.InnerFolderHLayout10)
        self.ConfirmBox = QtWidgets.QDialogButtonBox(Dialog)
        self.ConfirmBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ConfirmBox.setObjectName("ConfirmBox")
        self.InnerFolderVLayout.addWidget(self.ConfirmBox)
        self.WindowVLayout.addLayout(self.InnerFolderVLayout)
        self.verticalLayout.addLayout(self.WindowVLayout)

        self.ProjectNameLineEdit.textChanged.connect(self.updateProjectName)
        self.SelectPathButton.clicked.connect(self.updateProjectPath)
        self.ConfirmBox.accepted.connect(self.createFiles)
        self.ConfirmBox.rejected.connect(self.done)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Create a New Project"))
        self.ProjectNameLabelTitle.setText(_translate("Dialog", "Project Name: "))
        self.ProjectPathLabelTitle.setText(_translate("Dialog", "Project Path: "))
        self.SelectPathButton.setText(_translate("Dialog", "Select Path"))
        self.FinalProjectPathLabelTitle.setText(_translate("Dialog", "Final Project Path: "))
        self.FinalProjectPathLabel.setText(_translate("Dialog", ""))
        self.InnerFolderCheckbox01.setText(_translate("Dialog", "01"))
        self.InnerFolderCheckbox02.setText(_translate("Dialog", "02"))
        self.InnerFolderCheckbox03.setText(_translate("Dialog", "03"))
        self.InnerFolderCheckbox04.setText(_translate("Dialog", "04"))
        self.InnerFolderCheckbox05.setText(_translate("Dialog", "05"))
        self.InnerFolderCheckbox06.setText(_translate("Dialog", "06"))
        self.InnerFolderCheckbox07.setText(_translate("Dialog", "07"))
        self.InnerFolderCheckbox08.setText(_translate("Dialog", "08"))
        self.InnerFolderCheckbox09.setText(_translate("Dialog", "09"))
        self.InnerFolderCheckbox10.setText(_translate("Dialog", "10"))

        self.updateFinalProjectPath()

    def updateProjectName(self):
        self.project_name = self.ProjectNameLineEdit.text()
        self.updateFinalProjectPath()

    def updateProjectPath(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        if temp != "": 
            self.project_path = temp
            self.updateFinalProjectPath()

    def updateFinalProjectPath(self):
        self.FinalProjectPathLabel.setText(self.project_path + "/" + self.project_name)

    def createFiles(self):
        complete_project_path = os.path.join(self.project_path, self.project_name)
        os.mkdir(complete_project_path)
        if self.InnerFolderCheckbox01.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine01.text()))
        if self.InnerFolderCheckbox02.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine02.text()))
        if self.InnerFolderCheckbox03.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine03.text()))
        if self.InnerFolderCheckbox04.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine04.text()))
        if self.InnerFolderCheckbox05.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine05.text()))
        if self.InnerFolderCheckbox06.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine06.text()))
        if self.InnerFolderCheckbox07.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine07.text()))
        if self.InnerFolderCheckbox08.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine08.text()))
        if self.InnerFolderCheckbox09.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine09.text()))
        if self.InnerFolderCheckbox10.isChecked() : os.mkdir(os.path.join(complete_project_path,self.InnerFolderNameLine10.text()))
        self.done()

    def done(self):
        sys.exit(0)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()

    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
