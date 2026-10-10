# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_problem_page.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextBrowser, QVBoxLayout, QWidget)
from gui.ui import form_resources_rc


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(901, 708)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(901, 708))
        Form.setStyleSheet(u"QLabel {\n"
"	font-family: \"Gill Sans\", sans-serif;\n"
"	font-size: 16px;\n"
"	color: rgb(1, 6, 38);\n"
"	font-weight: 400;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(901, 708))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    width: 12px;\n"
"    background: #F7F5F1;\n"
"    margin: 0px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #c8bbe9;\n"
"    min-height: 30px;\n"
"    border-radius: 6px; /* \u043f\u043e\u0432\u043d\u0435 \u0437\u0430\u043e\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044f */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #a79ce0;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")

        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 7)

        self.info_content = QWebEngineView(self.scrollAreaWidgetContents)
        self.info_content.setObjectName(u"info_content")
        self.info_content.setUrl(QUrl(u"about:blank"))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.info_content.setSizePolicy(sizePolicy)
        self.info_content.setMinimumHeight(800)

        self.verticalLayout_4.addWidget(self.info_content)

        self.data_frame = QFrame(self.scrollAreaWidgetContents)
        self.data_frame.setObjectName(u"data_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        self.data_frame.setSizePolicy(sizePolicy1)
        self.data_frame.setMinimumSize(QSize(0, 0))
        self.data_frame.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(164, 142, 202);\n"
"	border-radius: 8px;\n"
"	font-family: \"Gill Sans\", sans-serif;\n"
"	font-size: 16px;\n"
"	padding-left:5px;\n"
"	height: 30px;\n"
"}")
        self.gridLayout = QGridLayout(self.data_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(22)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.eps_label = QLabel(self.data_frame)
        self.eps_label.setObjectName(u"eps_label")
        self.eps_label.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.eps_label)

        self.eps_lineEdit = QLineEdit(self.data_frame)
        self.eps_lineEdit.setObjectName(u"eps_lineEdit")
        self.eps_lineEdit.setMinimumSize(QSize(291, 30))

        self.horizontalLayout_5.addWidget(self.eps_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.f_label = QLabel(self.data_frame)
        self.f_label.setObjectName(u"f_label")
        self.f_label.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamilies([u"Gill Sans"])
        font.setBold(False)
        self.f_label.setFont(font)
        self.f_label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.f_label)

        self.f_lineEdit = QLineEdit(self.data_frame)
        self.f_lineEdit.setObjectName(u"f_lineEdit")
        self.f_lineEdit.setMinimumSize(QSize(291, 28))
        font1 = QFont()
        font1.setFamilies([u"Gill Sans"])
        self.f_lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.f_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.k_label = QLabel(self.data_frame)
        self.k_label.setObjectName(u"k_label")
        self.k_label.setMinimumSize(QSize(0, 30))
        self.k_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.k_label)

        self.k_lineEdit = QLineEdit(self.data_frame)
        self.k_lineEdit.setObjectName(u"k_lineEdit")
        self.k_lineEdit.setMinimumSize(QSize(291, 25))
        self.k_lineEdit.setFont(font1)

        self.horizontalLayout_2.addWidget(self.k_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.u_0_label = QLabel(self.data_frame)
        self.u_0_label.setObjectName(u"u_0_label")
        self.u_0_label.setMinimumSize(QSize(0, 30))
        self.u_0_label.setTextFormat(Qt.TextFormat.AutoText)

        self.horizontalLayout_7.addWidget(self.u_0_label)

        self.u0_lineEdit = QLineEdit(self.data_frame)
        self.u0_lineEdit.setObjectName(u"u0_lineEdit")
        self.u0_lineEdit.setMinimumSize(QSize(291, 30))

        self.horizontalLayout_7.addWidget(self.u0_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(22)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.alpha_label = QLabel(self.data_frame)
        self.alpha_label.setObjectName(u"alpha_label")
        self.alpha_label.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.alpha_label)

        self.alpha_lineEdit = QLineEdit(self.data_frame)
        self.alpha_lineEdit.setObjectName(u"alpha_lineEdit")
        self.alpha_lineEdit.setMinimumSize(QSize(291, 30))

        self.horizontalLayout_6.addWidget(self.alpha_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_6, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(18)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.phi_label = QLabel(self.data_frame)
        self.phi_label.setObjectName(u"phi_label")
        self.phi_label.setMinimumSize(QSize(0, 30))
        self.phi_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.phi_label)

        self.phi_lineEdit = QLineEdit(self.data_frame)
        self.phi_lineEdit.setObjectName(u"phi_lineEdit")
        self.phi_lineEdit.setMinimumSize(QSize(291, 25))
        self.phi_lineEdit.setFont(font1)

        self.horizontalLayout_3.addWidget(self.phi_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.u_l_label = QLabel(self.data_frame)
        self.u_l_label.setObjectName(u"u_l_label")
        self.u_l_label.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_8.addWidget(self.u_l_label)

        self.ul_lineEdit = QLineEdit(self.data_frame)
        self.ul_lineEdit.setObjectName(u"ul_lineEdit")
        self.ul_lineEdit.setMinimumSize(QSize(291, 30))

        self.horizontalLayout_8.addWidget(self.ul_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_8, 3, 1, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(22)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.v_label = QLabel(self.data_frame)
        self.v_label.setObjectName(u"v_label")
        self.v_label.setMinimumSize(QSize(0, 30))
        self.v_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.v_label)

        self.v_lineEdit = QLineEdit(self.data_frame)
        self.v_lineEdit.setObjectName(u"v_lineEdit")
        self.v_lineEdit.setMinimumSize(QSize(291, 25))

        self.horizontalLayout_4.addWidget(self.v_lineEdit)

        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.verticalLayout_4.addWidget(self.data_frame)

        self.task_frame = QFrame(self.scrollAreaWidgetContents)
        self.task_frame.setObjectName(u"task_frame")
        self.task_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.task_frame.setMinimumSize(QSize(0, 0))
        self.task_frame.setStyleSheet(u"QLabel {\n"
"	font-weight: 600;\n"
"	margin: 5px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font-size:16px;\n"
"	font-family: \"Gill Sans\", sans-sarif;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    border: 2px solid rgb(164, 142, 202);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    border: 2px solid rgb(164, 142, 202);\n"
"    background-color: rgb(164, 142, 202);\n"
"}\n"
"\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.task_frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, 0, -1, -1)
        self.task_label = QLabel(self.task_frame)
        self.task_label.setObjectName(u"task_label")
        self.task_label.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Gill Sans"])
        font2.setWeight(QFont.DemiBold)
        self.task_label.setFont(font2)
        self.task_label.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.task_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.without_constraints_RB = QRadioButton(self.task_frame)
        self.without_constraints_RB.setObjectName(u"without_constraints_RB")

        self.verticalLayout.addWidget(self.without_constraints_RB)

        self.with_constraints_RB = QRadioButton(self.task_frame)
        self.with_constraints_RB.setObjectName(u"with_constraints_RB")

        self.verticalLayout.addWidget(self.with_constraints_RB)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4.addWidget(self.task_frame)

        self.method_frame = QFrame(self.scrollAreaWidgetContents)
        self.method_frame.setObjectName(u"method_frame")
        self.method_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.method_frame.setMinimumSize(QSize(0, 0))
        self.method_frame.setStyleSheet(u"QComboBox {\n"
"	border-radius: 8px;\n"
"	border: 2px solid rgb(164, 142, 202);\n"
"	padding: 1px 8px 1px 3px;\n"
"	selection-background-color: rgb(220, 210, 240);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 20px;\n"
"	border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/caret-down.png);\n"
"    width: 20px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 2px solid rgb(164, 142, 202);\n"
"    border-radius: 0px 0px 8px 8px;\n"
"    selection-background-color: rgb(220, 210, 240);\n"
"    background-color: white;\n"
"	font-family: \"Gill Sans\", sans-serif;\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.method_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.method_label = QLabel(self.method_frame)
        self.method_label.setObjectName(u"method_label")
        self.method_label.setMinimumSize(QSize(0, 30))
        self.method_label.setBaseSize(QSize(0, 0))
        self.method_label.setFont(font2)
        self.method_label.setStyleSheet(u"QLabel {\n"
"	font-weight: 600;\n"
"	margin: 5px;\n"
"}")

        self.verticalLayout_3.addWidget(self.method_label)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(258, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.method_comboBox = QComboBox(self.method_frame)
        self.method_comboBox.setObjectName(u"method_comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.method_comboBox.sizePolicy().hasHeightForWidth())
        self.method_comboBox.setSizePolicy(sizePolicy2)
        self.method_comboBox.setMinimumSize(QSize(301, 35))

        self.horizontalLayout_9.addWidget(self.method_comboBox)

        self.horizontalSpacer_2 = QSpacerItem(268, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalLayout_4.addWidget(self.method_frame)

        self.additional_stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.additional_stackedWidget.setObjectName(u"additional_stackedWidget")
        self.additional_stackedWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.additional_stackedWidget.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setBold(False)
        self.additional_stackedWidget.setFont(font3)
        self.additional_stackedWidget.setStyleSheet(u"QLineEdit {\n"
"	border: 1px solid rgb(164, 142, 202);\n"
"	border-radius: 8px;\n"
"	font-family: \"Gill Sans\", sans-serif;\n"
"	font-size: 16px;\n"
"	padding-left:5px;\n"
"	height: 30px;\n"
"}")
        self.empty_page = QWidget()
        self.empty_page.setObjectName(u"empty_page")
        self.empty_page.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.additional_stackedWidget.addWidget(self.empty_page)

        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"")

        self.layoutWidget = QWidget(self.page_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 871, 85))

        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(291, 41))
        self.label_4.setStyleSheet(u"QLabel {\n"
"	font-weight: 600;\n"
"	margin: 10px;\n"
"}")

        self.verticalLayout_8.addWidget(self.label_4)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, -1, -1, -1)
        self.horizontalSpacer_9 = QSpacerItem(308, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.n_label = QLabel(self.layoutWidget)
        self.n_label.setObjectName(u"n_label")
        self.n_label.setMinimumSize(QSize(30, 32))

        self.horizontalLayout_19.addWidget(self.n_label)

        self.n_lineEdit = QLineEdit(self.layoutWidget)
        self.n_lineEdit.setObjectName(u"n_lineEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.n_lineEdit.sizePolicy().hasHeightForWidth())
        self.n_lineEdit.setSizePolicy(sizePolicy3)
        self.n_lineEdit.setMinimumSize(QSize(200, 32))

        self.horizontalLayout_19.addWidget(self.n_lineEdit)

        self.horizontalLayout_20.addLayout(self.horizontalLayout_19)

        self.horizontalSpacer_10 = QSpacerItem(298, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_10)

        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.additional_stackedWidget.addWidget(self.page_1)

        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"")

        self.page_3.setLayout(QVBoxLayout())
        self.layoutWidget1 = QWidget(self.page_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 871, 88))
        self.page_3.layout().addWidget(self.layoutWidget1)

        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(291, 41))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QLabel {\n"
"	font-weight: 600;\n"
"	margin: 10px;\n"
"}")

        self.verticalLayout_5.addWidget(self.label)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(150)
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.n_1_label = QLabel(self.layoutWidget1)
        self.n_1_label.setObjectName(u"n_1_label")
        self.n_1_label.setMinimumSize(QSize(40, 28))
        self.n_1_label.setBaseSize(QSize(0, 0))

        self.horizontalLayout_11.addWidget(self.n_1_label)

        self.n_1_lineEdit = QLineEdit(self.layoutWidget1)
        self.n_1_lineEdit.setObjectName(u"n_1_lineEdit")
        sizePolicy3.setHeightForWidth(self.n_1_lineEdit.sizePolicy().hasHeightForWidth())
        self.n_1_lineEdit.setSizePolicy(sizePolicy3)
        self.n_1_lineEdit.setMinimumSize(QSize(200, 28))

        self.horizontalLayout_11.addWidget(self.n_1_lineEdit)

        self.gridLayout_2.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.n_max_label = QLabel(self.layoutWidget1)
        self.n_max_label.setObjectName(u"n_max_label")
        self.n_max_label.setMinimumSize(QSize(40, 28))

        self.horizontalLayout_12.addWidget(self.n_max_label)

        self.n_max_lineEdit = QLineEdit(self.layoutWidget1)
        self.n_max_lineEdit.setObjectName(u"n_max_lineEdit")
        sizePolicy3.setHeightForWidth(self.n_max_lineEdit.sizePolicy().hasHeightForWidth())
        self.n_max_lineEdit.setSizePolicy(sizePolicy3)
        self.n_max_lineEdit.setMinimumSize(QSize(200, 28))

        self.horizontalLayout_12.addWidget(self.n_max_lineEdit)

        self.gridLayout_2.addLayout(self.horizontalLayout_12, 0, 1, 1, 1)

        self.horizontalLayout_13.addLayout(self.gridLayout_2)

        self.horizontalSpacer_6 = QSpacerItem(88, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.additional_stackedWidget.addWidget(self.page_3)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"")

        self.page_2.setLayout(QVBoxLayout())
        self.layoutWidget2 = QWidget(self.page_2)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 861, 113))
        self.page_2.layout().addWidget(self.layoutWidget2)

        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(291, 41))
        self.label_5.setStyleSheet(u"QLabel {\n"
"	font-weight: 600;\n"
"	margin: 10px;\n"
"}")

        self.verticalLayout_6.addWidget(self.label_5)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_7 = QSpacerItem(98, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_7)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(150)
        self.gridLayout_4.setVerticalSpacing(6)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.v_max_label = QLabel(self.layoutWidget2)
        self.v_max_label.setObjectName(u"v_max_label")
        self.v_max_label.setMinimumSize(QSize(40, 32))

        self.horizontalLayout_15.addWidget(self.v_max_label)

        self.vmax_lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.vmax_lineEdit_2.setObjectName(u"vmax_lineEdit_2")
        sizePolicy3.setHeightForWidth(self.vmax_lineEdit_2.sizePolicy().hasHeightForWidth())
        self.vmax_lineEdit_2.setSizePolicy(sizePolicy3)
        self.vmax_lineEdit_2.setMinimumSize(QSize(200, 32))

        self.horizontalLayout_15.addWidget(self.vmax_lineEdit_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_15, 0, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.n_label_2 = QLabel(self.layoutWidget2)
        self.n_label_2.setObjectName(u"n_label_2")
        self.n_label_2.setMinimumSize(QSize(30, 32))

        self.horizontalLayout_14.addWidget(self.n_label_2)

        self.n_lineEdit_2 = QLineEdit(self.layoutWidget2)
        self.n_lineEdit_2.setObjectName(u"n_lineEdit_2")
        sizePolicy3.setHeightForWidth(self.n_lineEdit_2.sizePolicy().hasHeightForWidth())
        self.n_lineEdit_2.setSizePolicy(sizePolicy3)
        self.n_lineEdit_2.setMinimumSize(QSize(200, 32))

        self.horizontalLayout_14.addWidget(self.n_lineEdit_2)

        self.gridLayout_4.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)

        self.horizontalLayout_21.addLayout(self.gridLayout_4)

        self.horizontalSpacer_8 = QSpacerItem(98, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)

        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.additional_stackedWidget.addWidget(self.page_2)

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"")

        self.page_4.setLayout(QVBoxLayout())
        self.layoutWidget3 = QWidget(self.page_4)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 861, 85))
        self.page_4.layout().addWidget(self.layoutWidget3)

        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(291, 40))
        self.label_3.setStyleSheet(u"QLabel {\n"
"	font-weight: 600;\n"
"	margin: 10px;\n"
"}")

        self.verticalLayout_7.addWidget(self.label_3)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(45)
        self.gridLayout_3.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.n_1_label_2 = QLabel(self.layoutWidget3)
        self.n_1_label_2.setObjectName(u"n_1_label_2")
        self.n_1_label_2.setMinimumSize(QSize(40, 32))

        self.horizontalLayout_16.addWidget(self.n_1_label_2)

        self.n1_lineEdit = QLineEdit(self.layoutWidget3)
        self.n1_lineEdit.setObjectName(u"n1_lineEdit")
        sizePolicy3.setHeightForWidth(self.n1_lineEdit.sizePolicy().hasHeightForWidth())
        self.n1_lineEdit.setSizePolicy(sizePolicy3)
        self.n1_lineEdit.setMinimumSize(QSize(200, 32))

        self.horizontalLayout_16.addWidget(self.n1_lineEdit)

        self.gridLayout_3.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.n_max_label_2 = QLabel(self.layoutWidget3)
        self.n_max_label_2.setObjectName(u"n_max_label_2")
        self.n_max_label_2.setMinimumSize(QSize(40, 32))

        self.horizontalLayout_17.addWidget(self.n_max_label_2)

        self.nmax_lineEdit = QLineEdit(self.layoutWidget3)
        self.nmax_lineEdit.setObjectName(u"nmax_lineEdit")
        sizePolicy3.setHeightForWidth(self.nmax_lineEdit.sizePolicy().hasHeightForWidth())
        self.nmax_lineEdit.setSizePolicy(sizePolicy3)
        self.nmax_lineEdit.setMinimumSize(QSize(200, 32))

        self.horizontalLayout_17.addWidget(self.nmax_lineEdit)

        self.gridLayout_3.addLayout(self.horizontalLayout_17, 0, 1, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.v_max_label_2 = QLabel(self.layoutWidget3)
        self.v_max_label_2.setObjectName(u"v_max_label_2")
        self.v_max_label_2.setMinimumSize(QSize(40, 32))

        self.horizontalLayout_18.addWidget(self.v_max_label_2)

        self.vmax_lineEdit = QLineEdit(self.layoutWidget3)
        self.vmax_lineEdit.setObjectName(u"vmax_lineEdit")
        sizePolicy3.setHeightForWidth(self.vmax_lineEdit.sizePolicy().hasHeightForWidth())
        self.vmax_lineEdit.setSizePolicy(sizePolicy3)
        self.vmax_lineEdit.setMinimumSize(QSize(200, 32))

        self.horizontalLayout_18.addWidget(self.vmax_lineEdit)

        self.gridLayout_3.addLayout(self.horizontalLayout_18, 0, 2, 1, 1)

        self.verticalLayout_7.addLayout(self.gridLayout_3)

        self.additional_stackedWidget.addWidget(self.page_4)

        self.verticalLayout_4.addWidget(self.additional_stackedWidget)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 60, 0, 25)
        self.horizontalLayout_10.addStretch()

        self.solve_button = QPushButton(self.scrollAreaWidgetContents)
        self.solve_button.setObjectName(u"solve_button")
        sizePolicy2.setHeightForWidth(self.solve_button.sizePolicy().hasHeightForWidth())
        self.solve_button.setSizePolicy(sizePolicy2)
        self.solve_button.setMinimumSize(QSize(161, 35))
        self.solve_button.setFont(font1)
        self.solve_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.solve_button.setStyleSheet(u"QPushButton {\n"
"	font-size: 18px;\n"
"    font-family: \"Gill Sans\", sans-serif;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	color: rgb(60, 40, 107);\n"
"	border: 2px solid rgb(60, 40, 107);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(131, 135, 195);\n"
"	border: 2px solid rgb(60, 40, 107);\n"
"}")

        self.horizontalLayout_10.addWidget(self.solve_button)

        self.horizontalLayout_10.addStretch()

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        self.additional_stackedWidget.setCurrentIndex(3)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.eps_label.setText(QCoreApplication.translate("Form", u"\u03b5:", None))
        self.f_label.setText(QCoreApplication.translate("Form", u"f(x):", None))
        self.k_label.setText(QCoreApplication.translate("Form", u"k(x):", None))
        self.u_0_label.setText(QCoreApplication.translate("Form", u"u(0):", None))
        self.alpha_label.setText(QCoreApplication.translate("Form", u"\u03b1:", None))
        self.phi_label.setText(QCoreApplication.translate("Form", u"\u03c6(x):", None))
        self.u_l_label.setText(QCoreApplication.translate("Form", u"u(l):", None))
        self.v_label.setText(QCoreApplication.translate("Form", u"v\u207d\u2070\u207e:", None))
        self.task_label.setText(QCoreApplication.translate("Form", u"Select problem type:", None))
        self.without_constraints_RB.setText(QCoreApplication.translate("Form", u"Unconstrained control problem: v(x) \u2208 L\u2082[0, l]", None))
        self.with_constraints_RB.setText(QCoreApplication.translate("Form", u"Constrained control problem: v = v(x) \u2208 V = { v(x) \u2208 L\u2082[0, l] : 0 \u2264 v(x) \u2264 v\u2098\u2090\u2093, x \u2208 [0, l] }", None))
        self.method_label.setText(QCoreApplication.translate("Form", u"Select solution method:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Additional parameters:", None))
        self.n_label.setText(QCoreApplication.translate("Form", u"N:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Additional parameters:", None))
        self.n_1_label.setText(QCoreApplication.translate("Form", u"N\u2081:", None))
        self.n_max_label.setText(QCoreApplication.translate("Form", u"N\u2098\u2090\u2093:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Additional parameters:", None))
        self.v_max_label.setText(QCoreApplication.translate("Form", u"v\u2098\u2090\u2093:", None))
        self.n_label_2.setText(QCoreApplication.translate("Form", u"N:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Additional parameters:", None))
        self.n_1_label_2.setText(QCoreApplication.translate("Form", u"N\u2081:", None))
        self.n_max_label_2.setText(QCoreApplication.translate("Form", u"N\u2098\u2090\u2093:", None))
        self.v_max_label_2.setText(QCoreApplication.translate("Form", u"v\u2098\u2090\u2093:", None))
        self.solve_button.setText(QCoreApplication.translate("Form", u"Solve task", None))
    # retranslateUi

