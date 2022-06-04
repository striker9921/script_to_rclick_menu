import os
import sys
import json

from PyQt5 import QtCore, QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    project_name = "New Project"
    project_path = os.getcwd()
    template = {}
    script_dir = os.path.dirname(__file__)

    def __init__(self):
        # Call inherited constructor
        super(Ui, self).__init__()
        
        # Load .ui file
        self.ui = uic.loadUi(os.path.join(self.script_dir, "new_project.ui"), self)
        
        # Find ui objects that will be used and assign to a variable
        self.ProjectNameLineEdit = self.ui.findChild(QtWidgets.QLineEdit, "ProjectNameLineEdit")
        self.SelectPathButton = self.ui.findChild(QtWidgets.QPushButton, "SelectPathButton")
        self.FinalProjectPathLabel = self.ui.findChild(QtWidgets.QLabel, "FinalProjectPathLabel")
        self.FileTree = self.ui.findChild(QtWidgets.QTreeWidget, "FileTree")
        self.SelectTemplate = self.ui.findChild(QtWidgets.QComboBox, "SelectTemplate")
        self.AddFolder = self.ui.findChild(QtWidgets.QPushButton, "AddFolder")
        self.AddSubFolder = self.ui.findChild(QtWidgets.QPushButton, "AddSubFolder")
        self.RemoveFolder = self.ui.findChild(QtWidgets.QPushButton, "RemoveFolder")
        self.ConfirmBox = self.ui.findChild(QtWidgets.QDialogButtonBox, "ConfirmBox")
        
        # Connect ui actions to defined functions
        self.ProjectNameLineEdit.textChanged.connect(self.updateProjectName)
        self.SelectPathButton.clicked.connect(self.updateProjectPath)
        self.ConfirmBox.accepted.connect(self.createFiles)
        self.ConfirmBox.rejected.connect(self.quit)
        self.AddFolder.clicked.connect(self.add_folder)
        self.AddSubFolder.clicked.connect(self.add_sub_folder)
        self.RemoveFolder.clicked.connect(self.remove_selected_folder)
        self.SelectTemplate.currentTextChanged.connect(self.load_template)
        
        # Read default template
        self.read_default()

        self.updateFinalProjectPath()

        self.show()


    def updateProjectName(self):
        temp = self.ProjectNameLineEdit.text()
        if temp == "":
            self.project_name = "New Project"
        else:
            self.project_name = temp
        self.FileTree.setHeaderLabel(self.project_name)
        self.updateFinalProjectPath()

    def updateProjectPath(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        if temp != "": 
            self.project_path = "\\".join(temp.split("/"))
            self.updateFinalProjectPath()

    def updateFinalProjectPath(self):
        self.FinalProjectPathLabel.setText(os.path.join(self.project_path,self.project_name))

    def createFiles(self):
        complete_project_path = os.path.join(self.project_path, self.project_name)
        os.mkdir(complete_project_path)
        for i in range(self.FileTree.invisibleRootItem().childCount()):
            self.createFilesRecur(self.FileTree.invisibleRootItem().child(i), complete_project_path)            
        self.quit()
    
    def createFilesRecur(self, root, path):
        cur_path = os.path.join(path, root.text(0))
        os.mkdir(cur_path)
        for i in range(root.childCount()):
            self.createFilesRecur(root.child(i), cur_path)

    def quit(self):
        sys.exit(0)

    def read_default(self):
        fp = open(os.path.join(self.script_dir, "project_template.json"), "r")
        self.template = json.load(fp)["templates"]
        fp.close()

        self.SelectTemplate.clear()
        for key in self.template:
            self.SelectTemplate.addItem(key)
        self.FileTree.clear()
        self.FileTree.setHeaderLabel("New Project")

    def load_template(self):
        self.FileTree.clear()
        template_key = self.SelectTemplate.currentText()
        if(template_key == ""): 
            return
        
        selected_template = self.template[template_key]
        for item in selected_template:
            new_item = QtWidgets.QTreeWidgetItem()
            new_item.setText(0, item)
            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)
            self.load_template_recur(selected_template[item], new_item)
            self.FileTree.addTopLevelItem(new_item)

    def load_template_recur(self, template, root):
        for item in template:
            new_item = QtWidgets.QTreeWidgetItem()
            new_item.setText(0, item)
            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)
            self.load_template_recur(template[item], new_item)
            root.addChild(new_item)

    def add_folder(self, name):
        new_item = QtWidgets.QTreeWidgetItem()
        new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)

        current_items = self.FileTree.selectedItems()
        if not current_items:
            if(name == False) : name = str(self.FileTree.topLevelItemCount())
            new_item.setText(0, name)
            self.FileTree.addTopLevelItem(new_item)
        else:
            parent = current_items[0].parent()
            if not parent:
                if(name == False) : name = str(self.FileTree.topLevelItemCount())
                new_item.setText(0, name)
                self.FileTree.addTopLevelItem(new_item)
            else:    
                if(name == False) : name = str(parent.childCount())
                new_item.setText(0, name)
                parent.addChild(new_item)

    def add_sub_folder(self, name):
        new_item = QtWidgets.QTreeWidgetItem()
        new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)

        current_items = self.FileTree.selectedItems()
        if not current_items:
            if(name == False) : name = str(self.FileTree.topLevelItemCount())
            new_item.setText(0, name)
            self.FileTree.addTopLevelItem(new_item)
        else:
            current_item = current_items[0]
            if(name == False) : name = str(current_item.childCount())
            new_item.setText(0, name)
            current_item.addChild(new_item)
        
    def remove_selected_folder(self):
        selected_items = self.FileTree.selectedItems()
        if not selected_items:
            return
        parent = selected_items[0].parent()
        if not parent: parent = self.FileTree.invisibleRootItem()
        parent.removeChild(selected_items[0])


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()