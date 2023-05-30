# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'subreddit.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SubHeader(object):
    def setupUi(self, SubHeader):
        if not SubHeader.objectName():
            SubHeader.setObjectName(u"SubHeader")
        SubHeader.resize(612, 182)
        self.gridLayout = QGridLayout(SubHeader)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.iconLabel = QLabel(SubHeader)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setMaximumSize(QSize(100, 100))
        self.iconLabel.setPixmap(QPixmap(u"../../../Downloads/subreddit-icon.png"))
        self.iconLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.iconLabel)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameLabel = QLabel(SubHeader)
        self.nameLabel.setObjectName(u"nameLabel")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.nameLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.nameLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.subCountLabel = QLabel(SubHeader)
        self.subCountLabel.setObjectName(u"subCountLabel")

        self.horizontalLayout_2.addWidget(self.subCountLabel)

        self.subButton = QPushButton(SubHeader)
        self.subButton.setObjectName(u"subButton")

        self.horizontalLayout_2.addWidget(self.subButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SubHeader)

        QMetaObject.connectSlotsByName(SubHeader)
    # setupUi

    def retranslateUi(self, SubHeader):
        SubHeader.setWindowTitle(QCoreApplication.translate("SubHeader", u"Form", None))
        self.iconLabel.setText("")
        self.nameLabel.setText(QCoreApplication.translate("SubHeader", u"r/rust", None))
        self.subCountLabel.setText(QCoreApplication.translate("SubHeader", u"69420 subscribers", None))
        self.subButton.setText(QCoreApplication.translate("SubHeader", u"Subscribe", None))
    # retranslateUi

