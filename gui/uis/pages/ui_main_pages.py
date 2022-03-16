# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(1058, 636)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)


        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 0))
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.theta1_layout = QHBoxLayout()
        self.theta1_layout.setObjectName(u"theta1_layout")

        self.verticalLayout.addLayout(self.theta1_layout)

        self.theta2_layout = QHBoxLayout()
        self.theta2_layout.setObjectName(u"theta2_layout")

        self.verticalLayout.addLayout(self.theta2_layout)

        self.theta3_layout = QHBoxLayout()
        self.theta3_layout.setObjectName(u"theta3_layout")

        self.verticalLayout.addLayout(self.theta3_layout)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.P1_layout = QHBoxLayout()
        self.P1_layout.setObjectName(u"P1_layout")

        self.verticalLayout.addLayout(self.P1_layout)

        self.P2_layout = QHBoxLayout()
        self.P2_layout.setObjectName(u"P2_layout")

        self.verticalLayout.addLayout(self.P2_layout)

        self.P3_layout = QHBoxLayout()
        self.P3_layout.setObjectName(u"P3_layout")

        self.verticalLayout.addLayout(self.P3_layout)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.O2_layout = QHBoxLayout()
        self.O2_layout.setObjectName(u"O2_layout")

        self.verticalLayout.addLayout(self.O2_layout)

        self.O4_layout = QHBoxLayout()
        self.O4_layout.setObjectName(u"O4_layout")

        self.verticalLayout.addLayout(self.O4_layout)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.image_latout = QVBoxLayout()
        self.image_latout.setObjectName(u"image_latout")

        self.verticalLayout_2.addLayout(self.image_latout)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")

        self.verticalLayout_2.addLayout(self.button_layout)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(300, 0))
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.alphas_layout = QHBoxLayout()
        self.alphas_layout.setObjectName(u"alphas_layout")

        self.verticalLayout_3.addLayout(self.alphas_layout)

        self.P21_layout = QHBoxLayout()
        self.P21_layout.setObjectName(u"P21_layout")

        self.verticalLayout_3.addLayout(self.P21_layout)

        self.P31_layout = QHBoxLayout()
        self.P31_layout.setObjectName(u"P31_layout")

        self.verticalLayout_3.addLayout(self.P31_layout)

        self.beta_layout = QHBoxLayout()
        self.beta_layout.setObjectName(u"beta_layout")

        self.verticalLayout_3.addLayout(self.beta_layout)

        self.others1_layout = QHBoxLayout()
        self.others1_layout.setObjectName(u"others1_layout")

        self.verticalLayout_3.addLayout(self.others1_layout)

        self.others2_layout = QHBoxLayout()
        self.others2_layout.setObjectName(u"others2_layout")

        self.verticalLayout_3.addLayout(self.others2_layout)

        self.gamma_layout = QHBoxLayout()
        self.gamma_layout.setObjectName(u"gamma_layout")

        self.verticalLayout_3.addLayout(self.gamma_layout)

        self.others3_layout = QHBoxLayout()
        self.others3_layout.setObjectName(u"others3_layout")

        self.verticalLayout_3.addLayout(self.others3_layout)

        self.others4_layout = QHBoxLayout()
        self.others4_layout.setObjectName(u"others4_layout")

        self.verticalLayout_3.addLayout(self.others4_layout)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8, 0, Qt.AlignHCenter)

        self.Lengths1_layout = QHBoxLayout()
        self.Lengths1_layout.setObjectName(u"Lengths1_layout")

        self.verticalLayout_3.addLayout(self.Lengths1_layout)

        self.Lengths2_layout = QHBoxLayout()
        self.Lengths2_layout.setObjectName(u"Lengths2_layout")

        self.verticalLayout_3.addLayout(self.Lengths2_layout)


        self.horizontalLayout.addWidget(self.frame_4)


        self.page_2_layout.addWidget(self.frame)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.empty_page_label = QLabel(self.page_3)
        self.empty_page_label.setObjectName(u"empty_page_label")
        font1 = QFont()
        font1.setPointSize(16)
        self.empty_page_label.setFont(font1)
        self.empty_page_label.setAlignment(Qt.AlignCenter)

        self.page_3_layout.addWidget(self.empty_page_label)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To PyOneDark GUI", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">INPUTS</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:11pt;\">Initial angles (\u00b0)</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:11pt;\">Point of interest\n"
"</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:11pt;\">Fixed pivots</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">OUTPUTS</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"<html><head/><body><p><span style=\" font-size:11pt;\">Lengths</span></p></body></html>", None))
        self.empty_page_label.setText(QCoreApplication.translate("MainPages", u"Empty Page", None))
    # retranslateUi

