# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'message_box.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from gui.ui import message_resources_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(350, 342)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(350, 342))
        Dialog.setStyleSheet(u"QDialog {\n"
"    border-radius: 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 20, 356, 323))

        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.icon_label = QLabel(self.layoutWidget)
        self.icon_label.setObjectName(u"icon_label")
        sizePolicy.setHeightForWidth(self.icon_label.sizePolicy().hasHeightForWidth())
        self.icon_label.setSizePolicy(sizePolicy)
        self.icon_label.setMinimumSize(QSize(90, 90))
        self.icon_label.setMaximumSize(QSize(90, 90))
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.icon_label)

        self.horizontalSpacer_2 = QSpacerItem(118, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_label = QLabel(self.layoutWidget)
        self.title_label.setObjectName(u"title_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy1)
        self.title_label.setMinimumSize(QSize(350, 40))
        self.title_label.setStyleSheet(u"QLabel {\n"
"	font-size: 26px;\n"
"	font-weight: 600;\n"
"	text-transform: uppercase;\n"
"	color: rgb(74, 74, 74);\n"
"}")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.message_label = QLabel(self.layoutWidget)
        self.message_label.setObjectName(u"message_label")
        sizePolicy1.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy1)
        self.message_label.setMinimumSize(QSize(320, 90))
        self.message_label.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;\n"
"	font-weight: 500;\n"
"	color: rgb(119, 119, 119);\n"
"   padding: 4px;\n"
"}")
        self.message_label.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.message_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.message_label)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.bottom_frame = QFrame(self.layoutWidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        sizePolicy1.setHeightForWidth(self.bottom_frame.sizePolicy().hasHeightForWidth())
        self.bottom_frame.setSizePolicy(sizePolicy1)
        self.bottom_frame.setMinimumSize(QSize(350, 30))
        self.bottom_frame.setMaximumSize(QSize(350, 30))
        self.bottom_frame.setStyleSheet(u"")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.bottom_frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.icon_label.setText("")
        self.title_label.setText("")
        self.message_label.setText("")
    # retranslateUi

