# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(688, 494)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 40, 811, 531))
        self.tabTeams = QWidget()
        self.tabTeams.setObjectName(u"tabTeams")
        self.listTeam = QListWidget(self.tabTeams)
        self.listTeam.setObjectName(u"listTeam")
        self.listTeam.setGeometry(QRect(20, 20, 201, 291))
        self.tablePlayer = QTableWidget(self.tabTeams)
        if (self.tablePlayer.columnCount() < 3):
            self.tablePlayer.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablePlayer.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablePlayer.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablePlayer.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tablePlayer.setObjectName(u"tablePlayer")
        self.tablePlayer.setGeometry(QRect(280, 20, 321, 211))
        self.addTeam = QPushButton(self.tabTeams)
        self.addTeam.setObjectName(u"addTeam")
        self.addTeam.setGeometry(QRect(20, 360, 31, 24))
        self.delTeam = QPushButton(self.tabTeams)
        self.delTeam.setObjectName(u"delTeam")
        self.delTeam.setGeometry(QRect(60, 360, 31, 24))
        self.addPlayer = QPushButton(self.tabTeams)
        self.addPlayer.setObjectName(u"addPlayer")
        self.addPlayer.setGeometry(QRect(280, 360, 31, 24))
        self.delPlayer = QPushButton(self.tabTeams)
        self.delPlayer.setObjectName(u"delPlayer")
        self.delPlayer.setGeometry(QRect(320, 360, 31, 24))
        self.exportTL = QPushButton(self.tabTeams)
        self.exportTL.setObjectName(u"exportTL")
        self.exportTL.setGeometry(QRect(590, 350, 91, 31))
        self.textTeam = QLineEdit(self.tabTeams)
        self.textTeam.setObjectName(u"textTeam")
        self.textTeam.setGeometry(QRect(80, 330, 121, 21))
        self.label = QLabel(self.tabTeams)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 330, 51, 16))
        self.editTeam = QPushButton(self.tabTeams)
        self.editTeam.setObjectName(u"editTeam")
        self.editTeam.setGeometry(QRect(100, 360, 51, 24))
        self.editPlayer = QPushButton(self.tabTeams)
        self.editPlayer.setObjectName(u"editPlayer")
        self.editPlayer.setGeometry(QRect(360, 360, 51, 24))
        self.label_2 = QLabel(self.tabTeams)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 250, 53, 16))
        self.label_3 = QLabel(self.tabTeams)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 280, 53, 16))
        self.label_4 = QLabel(self.tabTeams)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 310, 53, 16))
        self.textNickName = QLineEdit(self.tabTeams)
        self.textNickName.setObjectName(u"textNickName")
        self.textNickName.setGeometry(QRect(350, 250, 113, 21))
        self.textID = QLineEdit(self.tabTeams)
        self.textID.setObjectName(u"textID")
        self.textID.setGeometry(QRect(350, 280, 113, 21))
        self.textRace = QLineEdit(self.tabTeams)
        self.textRace.setObjectName(u"textRace")
        self.textRace.setGeometry(QRect(350, 310, 113, 21))
        self.tabWidget.addTab(self.tabTeams, "")
        self.tabSchedule = QWidget()
        self.tabSchedule.setObjectName(u"tabSchedule")
        self.tabWidget.addTab(self.tabSchedule, "")
        self.tabResult = QWidget()
        self.tabResult.setObjectName(u"tabResult")
        self.boxRound = QComboBox(self.tabResult)
        self.boxRound.setObjectName(u"boxRound")
        self.boxRound.setGeometry(QRect(60, 10, 121, 22))
        self.label_6 = QLabel(self.tabResult)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 53, 16))
        self.addRound = QPushButton(self.tabResult)
        self.addRound.setObjectName(u"addRound")
        self.addRound.setGeometry(QRect(320, 10, 21, 24))
        self.editRound = QLineEdit(self.tabResult)
        self.editRound.setObjectName(u"editRound")
        self.editRound.setGeometry(QRect(200, 10, 113, 21))
        self.delRound = QPushButton(self.tabResult)
        self.delRound.setObjectName(u"delRound")
        self.delRound.setGeometry(QRect(350, 10, 21, 24))
        self.editHomeTeam = QLineEdit(self.tabResult)
        self.editHomeTeam.setObjectName(u"editHomeTeam")
        self.editHomeTeam.setGeometry(QRect(60, 300, 113, 21))
        self.editAwayTeam = QLineEdit(self.tabResult)
        self.editAwayTeam.setObjectName(u"editAwayTeam")
        self.editAwayTeam.setGeometry(QRect(60, 330, 113, 21))
        self.label_7 = QLabel(self.tabResult)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 300, 53, 16))
        self.label_8 = QLabel(self.tabResult)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 330, 53, 16))
        self.addResult = QPushButton(self.tabResult)
        self.addResult.setObjectName(u"addResult")
        self.addResult.setGeometry(QRect(30, 360, 21, 24))
        self.delResult = QPushButton(self.tabResult)
        self.delResult.setObjectName(u"delResult")
        self.delResult.setGeometry(QRect(60, 360, 21, 24))
        self.editResult = QPushButton(self.tabResult)
        self.editResult.setObjectName(u"editResult")
        self.editResult.setGeometry(QRect(90, 360, 41, 24))
        self.tableDetail = QTableWidget(self.tabResult)
        if (self.tableDetail.columnCount() < 4):
            self.tableDetail.setColumnCount(4)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableDetail.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        self.tableDetail.setObjectName(u"tableDetail")
        self.tableDetail.setGeometry(QRect(230, 40, 441, 241))
        self.editPlayer1 = QLineEdit(self.tabResult)
        self.editPlayer1.setObjectName(u"editPlayer1")
        self.editPlayer1.setGeometry(QRect(230, 290, 91, 21))
        self.editPlayer2 = QLineEdit(self.tabResult)
        self.editPlayer2.setObjectName(u"editPlayer2")
        self.editPlayer2.setGeometry(QRect(330, 290, 91, 21))
        self.editMap = QLineEdit(self.tabResult)
        self.editMap.setObjectName(u"editMap")
        self.editMap.setGeometry(QRect(430, 290, 91, 21))
        self.editWinner = QLineEdit(self.tabResult)
        self.editWinner.setObjectName(u"editWinner")
        self.editWinner.setGeometry(QRect(530, 290, 91, 21))
        self.delDetailResult = QPushButton(self.tabResult)
        self.delDetailResult.setObjectName(u"delDetailResult")
        self.delDetailResult.setGeometry(QRect(260, 320, 21, 24))
        self.addDetailResult = QPushButton(self.tabResult)
        self.addDetailResult.setObjectName(u"addDetailResult")
        self.addDetailResult.setGeometry(QRect(230, 320, 21, 24))
        self.editDetailResult = QPushButton(self.tabResult)
        self.editDetailResult.setObjectName(u"editDetailResult")
        self.editDetailResult.setGeometry(QRect(290, 320, 41, 24))
        self.pushButton = QPushButton(self.tabResult)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(530, 350, 111, 24))
        self.openExcelResult = QPushButton(self.tabResult)
        self.openExcelResult.setObjectName(u"openExcelResult")
        self.openExcelResult.setGeometry(QRect(230, 350, 75, 24))
        self.boxSheetResult = QComboBox(self.tabResult)
        self.boxSheetResult.setObjectName(u"boxSheetResult")
        self.boxSheetResult.setGeometry(QRect(330, 350, 69, 22))
        self.importResult = QPushButton(self.tabResult)
        self.importResult.setObjectName(u"importResult")
        self.importResult.setGeometry(QRect(430, 350, 75, 24))
        self.listResult = QListWidget(self.tabResult)
        self.listResult.setObjectName(u"listResult")
        self.listResult.setGeometry(QRect(10, 40, 191, 241))
        self.tabWidget.addTab(self.tabResult, "")
        self.boxCode = QComboBox(self.centralwidget)
        self.boxCode.addItem("")
        self.boxCode.addItem("")
        self.boxCode.addItem("")
        self.boxCode.setObjectName(u"boxCode")
        self.boxCode.setGeometry(QRect(60, 10, 69, 22))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 53, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 688, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SATL Manager", None))
        ___qtablewidgetitem = self.tablePlayer.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u6635\u79f0", None));
        ___qtablewidgetitem1 = self.tablePlayer.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"id", None));
        ___qtablewidgetitem2 = self.tablePlayer.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u79cd\u65cf", None));
        self.addTeam.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.delTeam.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.addPlayer.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.delPlayer.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.exportTL.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u4e3aTL\u4ee3\u7801", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6218\u961f\u540d\u79f0", None))
        self.editTeam.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.editPlayer.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6635\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TLid", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u79cd\u65cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTeams), QCoreApplication.translate("MainWindow", u"\u6218\u961f\u7ba1\u7406", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSchedule), QCoreApplication.translate("MainWindow", u"\u6392\u9635\u7ba1\u7406", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8f6e\u6b21", None))
        self.addRound.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.delRound.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u961f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5ba2\u961f", None))
        self.addResult.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.delResult.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.editResult.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        ___qtablewidgetitem3 = self.tableDetail.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u624b1", None));
        ___qtablewidgetitem4 = self.tableDetail.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u624b2", None));
        ___qtablewidgetitem5 = self.tableDetail.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5730\u56fe", None));
        ___qtablewidgetitem6 = self.tableDetail.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u80dc\u8005", None));
        self.delDetailResult.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.addDetailResult.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.editDetailResult.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u4e3aTL\u4ee3\u7801", None))
        self.openExcelResult.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00Excel", None))
        self.importResult.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabResult), QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u7ba1\u7406", None))
        self.boxCode.setItemText(0, QCoreApplication.translate("MainWindow", u"C", None))
        self.boxCode.setItemText(1, QCoreApplication.translate("MainWindow", u"B", None))
        self.boxCode.setItemText(2, QCoreApplication.translate("MainWindow", u"A", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7ea7\u522b\uff1a", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

