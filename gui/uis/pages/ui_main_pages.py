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
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt;background:lightgreen;")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"font-size: 14pt;")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.Distribuitor = QFrame(self.page_2)
        self.Distribuitor.setObjectName(u"Distribuitor")
        self.Distribuitor.setEnabled(False)
        self.Distribuitor.setFrameShape(QFrame.StyledPanel)
        self.Distribuitor.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Distribuitor)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.in_frame = QFrame(self.Distribuitor)
        self.in_frame.setObjectName(u"in_frame")
        self.in_frame.setEnabled(False)
        self.in_frame.setMinimumSize(QSize(250, 500))
        self.in_frame.setMaximumSize(QSize(250, 500))
        self.in_frame.setFrameShape(QFrame.StyledPanel)
        self.in_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.in_frame)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.inputs = QLabel(self.in_frame)
        self.inputs.setObjectName(u"inputs")
        self.inputs.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.inputs)

        self.frame = QFrame(self.in_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.in_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.in_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.in_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_9 = QFrame(self.in_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.in_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.in_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.in_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.in_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.in_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.in_frame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_12)


        self.horizontalLayout.addWidget(self.in_frame)

        self.central_frame = QFrame(self.Distribuitor)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setMinimumSize(QSize(0, 0))
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.central_frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_16 = QFrame(self.central_frame)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 35))
        self.frame_16.setMaximumSize(QSize(16777215, 50))
        self.frame_16.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_16)

        self.frame_6 = QFrame(self.central_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(16777215, 300))
        self.frame_6.setStyleSheet(u"font-size: 14pt;background:red;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_17 = QFrame(self.central_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 35))
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_17)


        self.horizontalLayout.addWidget(self.central_frame)

        self.in_frame_2 = QFrame(self.Distribuitor)
        self.in_frame_2.setObjectName(u"in_frame_2")
        self.in_frame_2.setEnabled(False)
        self.in_frame_2.setMinimumSize(QSize(250, 500))
        self.in_frame_2.setMaximumSize(QSize(250, 500))
        self.in_frame_2.setFrameShape(QFrame.StyledPanel)
        self.in_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.in_frame_2)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.outputs = QLabel(self.in_frame_2)
        self.outputs.setObjectName(u"outputs")
        self.outputs.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_3.addWidget(self.outputs)

        self.frame_13 = QFrame(self.in_frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.in_frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_14)

        self.frame_18 = QFrame(self.in_frame_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.in_frame_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.in_frame_2)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.in_frame_2)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.in_frame_2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.in_frame_2)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.in_frame_2)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setStyleSheet(u"font-size: 14pt;background:orange;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.in_frame_2)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.in_frame_2)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"font-size: 14pt;background:green;")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_26)


        self.horizontalLayout.addWidget(self.in_frame_2)


        self.page_2_layout.addWidget(self.Distribuitor)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"font-size: 14pt;background:lightblue;")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"font-size: 14pt;background:yellow;")
        self.page_4_Layout = QVBoxLayout(self.page_4)
        self.page_4_Layout.setObjectName(u"page_4_Layout")
        self.pages.addWidget(self.page_4)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.inputs.setText(QCoreApplication.translate("MainPages", u"Inputs", None))
        self.outputs.setText(QCoreApplication.translate("MainPages", u"Outputs", None))
    # retranslateUi

