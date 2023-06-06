# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Search(object):
    def setupUi(self, Search):
        if not Search.objectName():
            Search.setObjectName(u"Search")
        Search.resize(591, 522)
        self.gridLayout = QGridLayout(Search)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Search)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 575, 458))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.searchResultsLayout = QVBoxLayout()
        self.searchResultsLayout.setObjectName(u"searchResultsLayout")

        self.gridLayout_2.addLayout(self.searchResultsLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.subNameEdit = QLineEdit(Search)
        self.subNameEdit.setObjectName(u"subNameEdit")

        self.horizontalLayout.addWidget(self.subNameEdit)

        self.searchButton = QPushButton(Search)
        self.searchButton.setObjectName(u"searchButton")

        self.horizontalLayout.addWidget(self.searchButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Search)

        QMetaObject.connectSlotsByName(Search)
    # setupUi

    def retranslateUi(self, Search):
        Search.setWindowTitle(QCoreApplication.translate("Search", u"Form", None))
        self.searchButton.setText(QCoreApplication.translate("Search", u"Search", None))
    # retranslateUi

