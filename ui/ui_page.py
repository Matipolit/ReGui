# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Page(object):
    def setupUi(self, Page):
        if not Page.objectName():
            Page.setObjectName(u"Page")
        Page.resize(969, 851)
        self.gridLayout = QGridLayout(Page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pageVerticalLayout = QVBoxLayout()
        self.pageVerticalLayout.setObjectName(u"pageVerticalLayout")
        self.pageScrollArea = QScrollArea(Page)
        self.pageScrollArea.setObjectName(u"pageScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pageScrollArea.sizePolicy().hasHeightForWidth())
        self.pageScrollArea.setSizePolicy(sizePolicy)
        self.pageScrollArea.setMaximumSize(QSize(800, 16777215))
        self.pageScrollArea.setWidgetResizable(True)
        self.pageScrollAreaWidgetContents = QWidget()
        self.pageScrollAreaWidgetContents.setObjectName(u"pageScrollAreaWidgetContents")
        self.pageScrollAreaWidgetContents.setGeometry(QRect(0, 0, 469, 789))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.pageScrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.pageScrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.pageScrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pageScrollVerticalLayout = QVBoxLayout()
        self.pageScrollVerticalLayout.setObjectName(u"pageScrollVerticalLayout")

        self.horizontalLayout_2.addLayout(self.pageScrollVerticalLayout)

        self.pageScrollArea.setWidget(self.pageScrollAreaWidgetContents)

        self.pageVerticalLayout.addWidget(self.pageScrollArea)


        self.horizontalLayout.addLayout(self.pageVerticalLayout)

        self.postVerticalLayout = QVBoxLayout()
        self.postVerticalLayout.setObjectName(u"postVerticalLayout")

        self.horizontalLayout.addLayout(self.postVerticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.pageTopHorLayout = QHBoxLayout()
        self.pageTopHorLayout.setObjectName(u"pageTopHorLayout")
        self.backButton = QPushButton(Page)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMaximumSize(QSize(150, 16777215))
        icon = QIcon(QIcon.fromTheme(u"draw-arrow-back"))
        self.backButton.setIcon(icon)

        self.pageTopHorLayout.addWidget(self.backButton)

        self.label = QLabel(Page)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.pageTopHorLayout.addWidget(self.label)

        self.searchButton = QPushButton(Page)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMaximumSize(QSize(150, 16777215))
        icon1 = QIcon(QIcon.fromTheme(u"search"))
        self.searchButton.setIcon(icon1)

        self.pageTopHorLayout.addWidget(self.searchButton)


        self.gridLayout.addLayout(self.pageTopHorLayout, 0, 1, 1, 1)


        self.retranslateUi(Page)

        QMetaObject.connectSlotsByName(Page)
    # setupUi

    def retranslateUi(self, Page):
        Page.setWindowTitle(QCoreApplication.translate("Page", u"Form", None))
        self.backButton.setText(QCoreApplication.translate("Page", u"Back", None))
        self.label.setText(QCoreApplication.translate("Page", u"Home", None))
        self.searchButton.setText(QCoreApplication.translate("Page", u"Go to subreddit", None))
    # retranslateUi

