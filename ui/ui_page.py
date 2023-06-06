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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Page(object):
    def setupUi(self, Page):
        if not Page.objectName():
            Page.setObjectName(u"Page")
        Page.resize(969, 887)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Page.sizePolicy().hasHeightForWidth())
        Page.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Page)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pageTopHorLayout = QHBoxLayout()
        self.pageTopHorLayout.setObjectName(u"pageTopHorLayout")
        self.backButton = QPushButton(Page)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setMaximumSize(QSize(150, 16777215))
        icon = QIcon()
        iconThemeName = u"draw-arrow-back"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

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
        icon1 = QIcon()
        iconThemeName = u"search"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.searchButton.setIcon(icon1)

        self.pageTopHorLayout.addWidget(self.searchButton)


        self.verticalLayout.addLayout(self.pageTopHorLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pageVerticalLayout = QVBoxLayout()
        self.pageVerticalLayout.setObjectName(u"pageVerticalLayout")
        self.pageScrollArea = QScrollArea(Page)
        self.pageScrollArea.setObjectName(u"pageScrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.pageScrollArea.sizePolicy().hasHeightForWidth())
        self.pageScrollArea.setSizePolicy(sizePolicy1)
        self.pageScrollArea.setMaximumSize(QSize(800, 16777215))
        self.pageScrollArea.setWidgetResizable(True)
        self.pageScrollAreaWidgetContents = QWidget()
        self.pageScrollAreaWidgetContents.setObjectName(u"pageScrollAreaWidgetContents")
        self.pageScrollAreaWidgetContents.setGeometry(QRect(0, 0, 469, 775))
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.pageScrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.pageScrollAreaWidgetContents.setSizePolicy(sizePolicy2)
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


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.helpButton = QPushButton(Page)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setMaximumSize(QSize(150, 16777215))
        icon2 = QIcon(QIcon.fromTheme(u"help-hint"))
        self.helpButton.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.helpButton)

        self.logoutButton = QPushButton(Page)
        self.logoutButton.setObjectName(u"logoutButton")
        self.logoutButton.setMaximumSize(QSize(150, 16777215))
        icon3 = QIcon(QIcon.fromTheme(u"application-exit-symbolic"))
        self.logoutButton.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.logoutButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Page)

        QMetaObject.connectSlotsByName(Page)
    # setupUi

    def retranslateUi(self, Page):
        Page.setWindowTitle(QCoreApplication.translate("Page", u"Form", None))
        self.backButton.setText(QCoreApplication.translate("Page", u"Back", None))
        self.label.setText(QCoreApplication.translate("Page", u"Home", None))
        self.searchButton.setText(QCoreApplication.translate("Page", u"Go to subreddit", None))
        self.helpButton.setText(QCoreApplication.translate("Page", u"Help", None))
        self.logoutButton.setText(QCoreApplication.translate("Page", u"Log out", None))
    # retranslateUi

