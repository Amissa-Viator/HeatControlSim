# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'empty_history.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 708)
        Form.setMinimumSize(QSize(901, 708))
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 901, 711))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.empty_label = QLabel(self.verticalLayoutWidget)
        self.empty_label.setObjectName(u"empty_label")
        font = QFont()
        font.setFamilies([u"Gill Sans"])
        font.setPointSize(20)
        font.setBold(True)
        self.empty_label.setFont(font)
        self.empty_label.setStyleSheet(u"QLabel {\n"
"	color: rgb(169, 169, 169);\n"
"	font-family: \"Gill Sans\", sans-serif;\n"
"}")
        self.empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.empty_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.empty_label.setText(QCoreApplication.translate("Form", u"Nothing is saved yet", None))
    # retranslateUi

