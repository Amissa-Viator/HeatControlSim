# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
from gui.ui import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1132, 708)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(245, 254, 250);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setMinimumSize(QSize(231, 708))
        self.icon_name_widget.setStyleSheet(u"QWidget {	\n"
"	\n"
"	background-color: rgb(74, 75, 157);\n"
"}\n"
"\n"
"QPushButton {\n"
"	text-align:left;\n"
"	height:40px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	font-size:18px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	color:white;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#f5fafe;\n"
"	font-weight:bold;\n"
"	color:#4d4d4d;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.side_menu_label = QLabel(self.icon_name_widget)
        self.side_menu_label.setObjectName(u"side_menu_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.side_menu_label.setFont(font)
        self.side_menu_label.setStyleSheet(u"color:white;")
        self.side_menu_label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignJustify)

        self.verticalLayout_2.addWidget(self.side_menu_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 35, -1, -1)
        self.home_button = QPushButton(self.icon_name_widget)
        self.home_button.setObjectName(u"home_button")
        icon = QIcon()
        icon.addFile(u":/icons/home-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icons/home.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.home_button.setIcon(icon)
        self.home_button.setIconSize(QSize(25, 25))
        self.home_button.setCheckable(True)
        self.home_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_button)

        self.history_button = QPushButton(self.icon_name_widget)
        self.history_button.setObjectName(u"history_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/history-white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icons/time-past.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.history_button.setIcon(icon1)
        self.history_button.setIconSize(QSize(25, 25))
        self.history_button.setCheckable(True)
        self.history_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.history_button)

        self.add_problem_button = QPushButton(self.icon_name_widget)
        self.add_problem_button.setObjectName(u"add_problem_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/add_white.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.add_problem_button.setIcon(icon2)
        self.add_problem_button.setIconSize(QSize(25, 25))
        self.add_problem_button.setCheckable(True)
        self.add_problem_button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.add_problem_button)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 455, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.icon_name_widget)

        self.page_stackedWidget = QStackedWidget(self.centralwidget)
        self.page_stackedWidget.setObjectName(u"page_stackedWidget")
        self.page_stackedWidget.setMinimumSize(QSize(901, 708))

        self.horizontalLayout.addWidget(self.page_stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.page_stackedWidget.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.side_menu_label.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.history_button.setText(QCoreApplication.translate("MainWindow", u" History", None))
        self.add_problem_button.setText(QCoreApplication.translate("MainWindow", u" Add problem", None))
    # retranslateUi

