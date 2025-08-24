# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(546, 386)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_2.addWidget(self.progressBar, 2, 0, 1, 1)

        self.pushButton_runsqlbtn = QPushButton(self.centralwidget)
        self.pushButton_runsqlbtn.setObjectName(u"pushButton_runsqlbtn")

        self.gridLayout_2.addWidget(self.pushButton_runsqlbtn, 2, 1, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_clearbtn = QPushButton(self.centralwidget)
        self.pushButton_clearbtn.setObjectName(u"pushButton_clearbtn")

        self.gridLayout.addWidget(self.pushButton_clearbtn, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_uploadbtn = QPushButton(self.centralwidget)
        self.pushButton_uploadbtn.setObjectName(u"pushButton_uploadbtn")

        self.gridLayout.addWidget(self.pushButton_uploadbtn, 1, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton_downloadbtn = QPushButton(self.centralwidget)
        self.pushButton_downloadbtn.setObjectName(u"pushButton_downloadbtn")

        self.gridLayout.addWidget(self.pushButton_downloadbtn, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 546, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_runsqlbtn.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.pushButton_clearbtn.setText(QCoreApplication.translate("MainWindow", u"Clear Table", None))
        self.pushButton_uploadbtn.setText(QCoreApplication.translate("MainWindow", u"Upload ID", None))
        self.pushButton_downloadbtn.setText(QCoreApplication.translate("MainWindow", u"Download", None))
    # retranslateUi

