# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_result.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_SearchResult(object):
    def setupUi(self, SearchResult):
        if not SearchResult.objectName():
            SearchResult.setObjectName(u"SearchResult")
        SearchResult.resize(571, 123)
        self.gridLayout = QGridLayout(SearchResult)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(SearchResult)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.SubIconLabel = QLabel(self.frame)
        self.SubIconLabel.setObjectName(u"SubIconLabel")
        self.SubIconLabel.setMaximumSize(QSize(60, 60))
        self.SubIconLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.SubIconLabel)

        self.SubNameLabel = QLabel(self.frame)
        self.SubNameLabel.setObjectName(u"SubNameLabel")

        self.horizontalLayout.addWidget(self.SubNameLabel)

        self.SubCountLabel = QLabel(self.frame)
        self.SubCountLabel.setObjectName(u"SubCountLabel")

        self.horizontalLayout.addWidget(self.SubCountLabel)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(SearchResult)

        QMetaObject.connectSlotsByName(SearchResult)
    # setupUi

    def retranslateUi(self, SearchResult):
        SearchResult.setWindowTitle(QCoreApplication.translate("SearchResult", u"Form", None))
        self.SubIconLabel.setText("")
        self.SubNameLabel.setText(QCoreApplication.translate("SearchResult", u"SubName", None))
        self.SubCountLabel.setText(QCoreApplication.translate("SearchResult", u"SubCount", None))
    # retranslateUi

