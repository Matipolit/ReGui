# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post-big.ui'
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
    QLayout, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_BigPost(object):
    def setupUi(self, BigPost):
        if not BigPost.objectName():
            BigPost.setObjectName(u"BigPost")
        BigPost.resize(713, 688)
        BigPost.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout = QGridLayout(BigPost)
        self.gridLayout.setObjectName(u"gridLayout")
        self.postScrollArea = QScrollArea(BigPost)
        self.postScrollArea.setObjectName(u"postScrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.postScrollArea.sizePolicy().hasHeightForWidth())
        self.postScrollArea.setSizePolicy(sizePolicy)
        self.postScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 697, 672))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.topLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.subName = QLabel(self.scrollAreaWidgetContents_2)
        self.subName.setObjectName(u"subName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.subName.sizePolicy().hasHeightForWidth())
        self.subName.setSizePolicy(sizePolicy1)
        self.subName.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setBold(True)
        self.subName.setFont(font)

        self.topLayout.addWidget(self.subName, 0, Qt.AlignLeft)

        self.usrName = QLabel(self.scrollAreaWidgetContents_2)
        self.usrName.setObjectName(u"usrName")
        sizePolicy1.setHeightForWidth(self.usrName.sizePolicy().hasHeightForWidth())
        self.usrName.setSizePolicy(sizePolicy1)
        self.usrName.setMaximumSize(QSize(16777215, 40))
        self.usrName.setLayoutDirection(Qt.LeftToRight)

        self.topLayout.addWidget(self.usrName, 0, Qt.AlignRight)


        self.titleLayout.addLayout(self.topLayout)

        self.postTitle = QLabel(self.scrollAreaWidgetContents_2)
        self.postTitle.setObjectName(u"postTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.postTitle.sizePolicy().hasHeightForWidth())
        self.postTitle.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.postTitle.setFont(font1)
        self.postTitle.setTextFormat(Qt.AutoText)
        self.postTitle.setWordWrap(True)

        self.titleLayout.addWidget(self.postTitle)

        self.contentScrollArea = QScrollArea(self.scrollAreaWidgetContents_2)
        self.contentScrollArea.setObjectName(u"contentScrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(6)
        sizePolicy3.setHeightForWidth(self.contentScrollArea.sizePolicy().hasHeightForWidth())
        self.contentScrollArea.setSizePolicy(sizePolicy3)
        self.contentScrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.contentScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 677, 346))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.postContent = QLabel(self.scrollAreaWidgetContents)
        self.postContent.setObjectName(u"postContent")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.postContent.sizePolicy().hasHeightForWidth())
        self.postContent.setSizePolicy(sizePolicy4)
        self.postContent.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.postContent.setFont(font2)
        self.postContent.setTextFormat(Qt.RichText)
        self.postContent.setWordWrap(True)
        self.postContent.setOpenExternalLinks(True)
        self.postContent.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.gridLayout_2.addWidget(self.postContent, 0, 0, 1, 1)

        self.contentScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.titleLayout.addWidget(self.contentScrollArea)

        self.linkImgLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.linkImgLabel.setObjectName(u"linkImgLabel")
        sizePolicy2.setHeightForWidth(self.linkImgLabel.sizePolicy().hasHeightForWidth())
        self.linkImgLabel.setSizePolicy(sizePolicy2)
        self.linkImgLabel.setPixmap(QPixmap(u"../../../Downloads/reddit_thumb.jpg"))
        self.linkImgLabel.setScaledContents(True)
        self.linkImgLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.linkImgLabel.setMargin(2)

        self.titleLayout.addWidget(self.linkImgLabel)

        self.urlButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.urlButton.setObjectName(u"urlButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(1)
        sizePolicy5.setHeightForWidth(self.urlButton.sizePolicy().hasHeightForWidth())
        self.urlButton.setSizePolicy(sizePolicy5)
        self.urlButton.setMinimumSize(QSize(150, 0))
        self.urlButton.setMaximumSize(QSize(16777215, 150))
        icon = QIcon()
        iconThemeName = u"link"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.urlButton.setIcon(icon)

        self.titleLayout.addWidget(self.urlButton, 0, Qt.AlignHCenter)

        self.toolLayout = QHBoxLayout()
        self.toolLayout.setObjectName(u"toolLayout")
        self.commentsNumLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.commentsNumLabel.setObjectName(u"commentsNumLabel")
        sizePolicy1.setHeightForWidth(self.commentsNumLabel.sizePolicy().hasHeightForWidth())
        self.commentsNumLabel.setSizePolicy(sizePolicy1)
        self.commentsNumLabel.setMaximumSize(QSize(120, 16777215))
        self.commentsNumLabel.setMargin(2)

        self.toolLayout.addWidget(self.commentsNumLabel, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.voteLayout = QHBoxLayout()
        self.voteLayout.setObjectName(u"voteLayout")
        self.downButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.downButton.setObjectName(u"downButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy6)
        icon1 = QIcon()
        iconThemeName = u"arrow-down"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.downButton.setIcon(icon1)

        self.voteLayout.addWidget(self.downButton, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.scoreLabel = QLabel(self.scrollAreaWidgetContents_2)
        self.scoreLabel.setObjectName(u"scoreLabel")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.scoreLabel.sizePolicy().hasHeightForWidth())
        self.scoreLabel.setSizePolicy(sizePolicy7)
        self.scoreLabel.setLayoutDirection(Qt.RightToLeft)
        self.scoreLabel.setAlignment(Qt.AlignCenter)

        self.voteLayout.addWidget(self.scoreLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.upvButton = QPushButton(self.scrollAreaWidgetContents_2)
        self.upvButton.setObjectName(u"upvButton")
        sizePolicy6.setHeightForWidth(self.upvButton.sizePolicy().hasHeightForWidth())
        self.upvButton.setSizePolicy(sizePolicy6)
        icon2 = QIcon()
        iconThemeName = u"arrow-up"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.upvButton.setIcon(icon2)

        self.voteLayout.addWidget(self.upvButton, 0, Qt.AlignRight|Qt.AlignBottom)


        self.toolLayout.addLayout(self.voteLayout)


        self.titleLayout.addLayout(self.toolLayout)

        self.titleLayout.setStretch(0, 1)

        self.verticalLayout.addLayout(self.titleLayout)


        self.gridLayout_3.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.postScrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.postScrollArea, 0, 0, 1, 1)


        self.retranslateUi(BigPost)

        QMetaObject.connectSlotsByName(BigPost)
    # setupUi

    def retranslateUi(self, BigPost):
        BigPost.setWindowTitle(QCoreApplication.translate("BigPost", u"Form", None))
        self.subName.setText(QCoreApplication.translate("BigPost", u"<html><head/><body><p><br/></p></body></html>", None))
        self.usrName.setText("")
        self.postTitle.setText("")
        self.postContent.setText(QCoreApplication.translate("BigPost", u"content", None))
        self.linkImgLabel.setText("")
        self.urlButton.setText(QCoreApplication.translate("BigPost", u"Link", None))
        self.commentsNumLabel.setText(QCoreApplication.translate("BigPost", u"123 comments", None))
        self.downButton.setText("")
        self.scoreLabel.setText(QCoreApplication.translate("BigPost", u"123", None))
        self.upvButton.setText("")
    # retranslateUi

