from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from ui_main import Ui_MainWindow
from dataTeamManager import *
from dataResultManager import *


# 注意 这里选择的父类 要和你UI文件窗体一样的类型
# 主窗口是 QMainWindow， 表单是 QWidget， 对话框是 QDialog
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.dataResult = None
        self.resultPath = None
        self.dataTeam = None
        self.ui = Ui_MainWindow()
        # 初始化界面
        self.ui.setupUi(self)
        self.ui.boxCode.currentTextChanged.connect(self.changeCode)
        self.ui.addTeam.clicked.connect(self.addTeam)
        self.ui.delTeam.clicked.connect(self.delTeam)
        self.ui.editTeam.clicked.connect(self.editTeam)
        self.ui.listTeam.clicked.connect(self.clickTeam)
        self.ui.openExcelResult.clicked.connect(self.openExcelResult)
        self.ui.boxRound.currentTextChanged.connect(self.updateResult)
        self.ui.listResult.clicked.connect(self.updateDetail)
        # 初始化数据
        self.initDataTeam()
        self.initDataResult()

    def initDataTeam(self):
        listTeam = self.ui.listTeam
        self.dataTeam = DataTeamManager("dataTeam" + self.ui.boxCode.currentText() + ".json")
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
            tablePlayer.insertRow(tablePlayer.rowCount())
            tablePlayer.setItem(tablePlayer.rowCount() - 1, 0, QTableWidgetItem(player["nickname"]))
            tablePlayer.setItem(tablePlayer.rowCount() - 1, 1, QTableWidgetItem(player["id"]))
            tablePlayer.setItem(tablePlayer.rowCount() - 1, 2, QTableWidgetItem(player["race"]))

    def initDataResult(self):
        boxRound = self.ui.boxRound
        self.dataResult = DataResultManager("dataResult" + self.ui.boxCode.currentText() + ".json")
        boxRound.clear()
        for roundName in self.dataResult.getRoundList():
            boxRound.addItem(roundName)
        self.updateResult()

    def updateResult(self):
        roundName = self.ui.boxRound.currentText()
        listResult = self.ui.listResult
        while listResult.count() > 0:
            listResult.takeItem(0)
        for result in self.dataResult.getResultList(roundName):
            listResult.addItem(result)

    def updateDetail(self):
        tableDetail = self.ui.tableDetail
        while tableDetail.rowCount() > 0:
            tableDetail.removeRow(0)
        for detail in self.dataResult.getDetail(self.ui.boxRound.currentText(), self.ui.listResult.currentRow()):
            tableDetail.insertRow(tableDetail.rowCount())
            tableDetail.setItem(tableDetail.rowCount() - 1, 0, QTableWidgetItem(detail["player1"]))
            tableDetail.setItem(tableDetail.rowCount() - 1, 1, QTableWidgetItem(detail["player2"]))
            tableDetail.setItem(tableDetail.rowCount() - 1, 2, QTableWidgetItem(detail["map"]))
            tableDetail.setItem(tableDetail.rowCount() - 1, 3, QTableWidgetItem(detail["winner"]))

    def openExcelResult(self):
        (file_path, file_type) = QFileDialog.getOpenFileName(self, "导入结果")
        self.resultPath = file_path



app = QApplication([])
mainWindows = MainWindow()
mainWindows.show()
app.exec()
