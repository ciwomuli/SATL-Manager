from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_main import Ui_MainWindow
from dataManager import *


# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.dataTeam = None
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.changeCode.clicked.connect(self.changeCode)
        self.ui.addTeam.clicked.connect(self.addTeam)
        self.ui.delTeam.clicked.connect(self.delTeam)
        self.ui.editTeam.clicked.connect(self.editTeam)
        self.ui.listTeam.clicked.connect(self.clickTeam)
        # 初始化数据

    def initDataTeam(self):
        listTeam = self.ui.listTeam
        self.dataTeam = DataManager("data" + self.ui.textCode.text() + ".json")
        while listTeam.count() > 0:
            listTeam.takeItem(0)
        for name in self.dataTeam.getTeams():
            listTeam.addItem(name)

    def changeCode(self):
        self.initDataTeam()

    def addTeam(self):
        if len(self.ui.textTeam.text()) == 0:
            return
        listTeam = self.ui.listTeam
        if self.dataTeam is not None:
            listTeam.addItem(self.ui.textTeam.text())
            self.dataTeam.addTeam(self.ui.textTeam.text())

    def delTeam(self):
        listTeam = self.ui.listTeam
        if self.dataTeam is not None:
            self.dataTeam.delTeam(listTeam.currentItem().text())
            listTeam.takeItem(listTeam.currentRow())

    def editTeam(self):
        listTeam = self.ui.listTeam
        if self.dataTeam is not None:
            self.dataTeam.editTeam(listTeam.currentItem().text(), self.ui.textTeam.text())
            listTeam.currentItem().setText(self.ui.textTeam.text())

    def clickTeam(self):
        listTeam = self.ui.listTeam
        tablePlayer = self.ui.tablePlayer
        self.ui.textTeam.setText(listTeam.currentItem().text())
        while tablePlayer.rowCount() > 0:
            tablePlayer.removeRow(0)
        for player in self.dataTeam.getPlayers(listTeam.currentItem().text()):
            tablePlayer.insertRow(0)
            tablePlayer.setItem(0, 0, QTableWidgetItem(player["nickname"]))
            tablePlayer.setItem(0, 1, QTableWidgetItem(player["id"]))
            tablePlayer.setItem(0, 2, QTableWidgetItem(player["race"]))


app = QApplication([])
mainWindows = MainWindow()
mainWindows.show()
app.exec()
