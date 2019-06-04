from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
import os,sys

from ui import main
from ui.chmodialog import ChModDialog

class MyFileBrowser(main.Ui_MainWindow, QtWidgets.QMainWindow):
    path = os.getcwd()
    curr_os = sys.platform
    def __init__(self):
        super(MyFileBrowser, self).__init__()
        menubar = self.menuBar()
        self.setupUi(self)
        self.populate()

        #toolbar triggers
        self.ext.triggered.connect(self.do_exit)
        self.back.triggered.connect(self.get_back)
        self.open.triggered.connect(self.do_open)
        self.new_folder.triggered.connect(self.do_mkdir)
        self.new_file.triggered.connect(self.do_mkfile)
        self.delete.triggered.connect(self.do_delete)
        self.symlink.triggered.connect(self.do_mksymlink)
        self.chmod.triggered.connect(self.do_chmod)

    def do_delete(self):
        index = self.treeView.currentIndex()
        obj_path = self.model.filePath(index)
        obj_name = obj_path.split("/")[-1]
        msg = QtWidgets.QMessageBox()
        msg.setText("Are you sure you want to delete this {}?".format(obj_name))
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowTitle("Delete Warning!")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        retval = msg.exec_()
        if(retval == 1024):
            if os.path.isfile(obj_path):
                os.remove(obj_path)
            elif os.path.isdir(obj_path):
                os.rmdir(obj_path)
            else:
                alert_msg = QtWidgets.QMessageBox()
                alert_msg.setText("Path provided isn't a file or a directory")
                alert_msg.exec_()
        else:
            pass

    def do_mkdir(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Name Of Folder', 'Enter Folder Name:')
        if ok and text != None:
            foldername = str(text)
            os.mkdir(foldername)
            self.populate()

    def do_mkfile(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Name Of File', 'Enter File Name:')
        if ok and text != None:
            filename = str(text)
            with open(filename,"w+") as f:
                pass
            self.populate()

    def do_mksymlink(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        file_path = file_path.replace("\\","/")
        src = str(file_path)
        dst = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        if src != "" and dst != "":
            os.symlink(src,dst)

    def do_exit(self):
        sys.exit()
    
    def do_open(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        file_path = file_path.replace("\\","/")
        self.path = file_path
        if os.path.isdir(file_path):
            os.chdir(self.path)
            self.populate()
        else:
            #windows compatible
            if "win" in self.curr_os:
                os.system("start "+file_path)
            #linux compatible
            else:
                os.system("xdg-open "+file_path)

    def get_back(self):
        os.chdir("..")
        self.path = os.getcwd()
        self.populate()

    def populate(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(self.path))
        self.treeView.setSortingEnabled(True)

    def do_chmod(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        perm = oct(os.stat(file_path).st_mode)[-3:]
        self.chmodDialog = ChModDialog(perm)
        out = self.chmodDialog.exec()
        if(out == 1):

            if("win" in self.curr_os): os.chmod(file_path, self.chmodDialog._get_perms())
            else: os.system("chmod {} {}".format(self.chmodDialog._get_perms(),file_path))

    def open_file(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        os.startfile(file_path)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
    app.exec_()