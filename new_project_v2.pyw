import os
import sys

from PyQt5 import QtCore, QtWidgets, uic

class Ui(QtWidgets.QDialog):
    project_name = "New Project"
    project_path = os.getcwd()
    template = []

    def __init__(self):
        # Call inherited constructor
        super(Ui, self).__init__()
        
        # Read default template
        self.read_default()
        
        # Load .ui file
        self.ui = uic.loadUi("new_project.ui", self)
        
        # Find ui objects that will be used and assign to a variable
        self.ProjectNameLineEdit = self.ui.findChild(QtWidgets.QLineEdit, "ProjectNameLineEdit")
        self.SelectPathButton = self.ui.findChild(QtWidgets.QPushButton, "SelectPathButton")
        self.FinalProjectPathLabel = self.ui.findChild(QtWidgets.QLabel, "FinalProjectPathLabel")
        self.InnerFolderList = self.ui.findChild(QtWidgets.QListWidget, "InnerFolderList")
        self.AddInnerFolder = self.ui.findChild(QtWidgets.QPushButton, "AddInnerFolder")
        self.RemoveInnerFolder = self.ui.findChild(QtWidgets.QPushButton, "RemoveInnerFolder")
        self.ConfirmBox = self.ui.findChild(QtWidgets.QDialogButtonBox, "ConfirmBox")
        
        # Connect ui actions to defined functions
        self.ProjectNameLineEdit.textChanged.connect(self.updateProjectName)
        self.SelectPathButton.clicked.connect(self.updateProjectPath)
        self.ConfirmBox.accepted.connect(self.createFiles)
        self.ConfirmBox.rejected.connect(self.quit)
        self.AddInnerFolder.clicked.connect(self.add_inner_folder)
        self.RemoveInnerFolder.clicked.connect(self.remove_selected_folder)

        # Add Default Inner Folders
        for folder in self.template:
            self.add_inner_folder(folder)

        self.updateFinalProjectPath()

        self.show()


    def updateProjectName(self):
        temp = self.ProjectNameLineEdit.text()
        if temp == "":
            self.project_name = "New Project"
        else:
            self.project_name = temp
        self.updateFinalProjectPath()

    def updateProjectPath(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        if temp != "": 
            self.project_path = temp
            self.updateFinalProjectPath()

    def updateFinalProjectPath(self):
        self.FinalProjectPathLabel.setText(os.path.join(self.project_path,self.project_name))

    def createFiles(self):
        complete_project_path = os.path.join(self.project_path, self.project_name)
        os.mkdir(complete_project_path)
        
        self.quit()

    def quit(self):
        sys.exit(0)

    def read_default(self):
        fp = open("project_template.txt", "r")
        for line in fp:
            self.template.append(line[:-1])
        fp.close()

    def add_inner_folder(self, name="NewInnerFolder"):
        # Credit: https://stackoverflow.com/questions/22340514/qt-designer-qlistwidget-checkbox
        new_item = QtWidgets.QListWidgetItem()
        new_item.setText(name)
        new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEditable)
        new_item.setCheckState(QtCore.Qt.Checked)
        self.InnerFolderList.addItem(new_item)
        
    def remove_selected_folder(self):
        # Credit: https://stackoverflow.com/questions/23835847/how-to-remove-item-from-qlistwidget#:~:text=removeItemWidget%20doesn't%20remove%20item,an%20item%20from%20the%20list.
        listItems = self.InnerFolderList.selectedItems()
        if not listItems: return        
        for item in listItems:
            self.InnerFolderList.takeItem(self.InnerFolderList.row(item))



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()