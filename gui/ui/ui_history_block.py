# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_block.ui'
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
from PySide6.QtWidgets import (QApplication, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 708)
        Form.setMinimumSize(QSize(901, 708))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.blocks_scrollArea = QScrollArea(Form)
        self.blocks_scrollArea.setObjectName(u"blocks_scrollArea")
        self.blocks_scrollArea.setMinimumSize(QSize(901, 708))
        self.blocks_scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"	width: 12px;\n"
"	background: #F7F5F1;\n"
"	margin: 0px;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	background: #c8bbe9;\n"
"	min-height: 30px;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: #a79ce0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"	height: 0px;\n"
"}")
        self.blocks_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.blocks_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.blocks_scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setMinimumSize(QSize(901, 708))

        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.blocks_scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

