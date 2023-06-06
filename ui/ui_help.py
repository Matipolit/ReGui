# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Help(object):
    def setupUi(self, Help):
        if not Help.objectName():
            Help.setObjectName(u"Help")
        Help.resize(736, 506)
        self.gridLayout = QGridLayout(Help)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(Help)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 720, 490))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.label_2)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.retranslateUi(Help)

        QMetaObject.connectSlotsByName(Help)
    # setupUi

    def retranslateUi(self, Help):
        Help.setWindowTitle(QCoreApplication.translate("Help", u"Form", None))
        self.label.setText(QCoreApplication.translate("Help", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("Help", u"<html><head/><body><p><span style=\" font-weight:600;\">View post:</span></p><p>Click a post preview in a subreddit to see the whole post and its comments.</p><p><span style=\" font-weight:600;\">Go to subreddit:</span></p><p>To go to a subreddit click its name in a post or use the search function.</p><p><span style=\" font-weight:600;\">Search:</span></p><p>Type in a subreddit name and click the search button, then a list of subreddits will appear.</p><p>Double click one to open it.</p><p><span style=\" font-weight:600;\">Vote:</span></p><p>Double click on the buttons with up or down arrows to upvote/downvote a post or comment.</p><p> They will be colored if the vote was successful.</p></body></html>", None))
    # retranslateUi

