# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'post.ui'
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
    QLabel, QLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Post(object):
    def setupUi(self, Post):
        if not Post.objectName():
            Post.setObjectName(u"Post")
        Post.resize(612, 243)
        self.gridLayout = QGridLayout(Post)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Post)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setMidLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.subName = QLabel(self.frame)
        self.subName.setObjectName(u"subName")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subName.sizePolicy().hasHeightForWidth())
        self.subName.setSizePolicy(sizePolicy)
        self.subName.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setBold(True)
        self.subName.setFont(font)

        self.horizontalLayout.addWidget(self.subName, 0, Qt.AlignLeft)

        self.usrName = QLabel(self.frame)
        self.usrName.setObjectName(u"usrName")
        sizePolicy.setHeightForWidth(self.usrName.sizePolicy().hasHeightForWidth())
        self.usrName.setSizePolicy(sizePolicy)
        self.usrName.setMaximumSize(QSize(16777215, 50))
        self.usrName.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.usrName, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.titleThumbLayout = QHBoxLayout()
        self.titleThumbLayout.setObjectName(u"titleThumbLayout")
        self.postTitle = QLabel(self.frame)
        self.postTitle.setObjectName(u"postTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.postTitle.sizePolicy().hasHeightForWidth())
        self.postTitle.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.postTitle.setFont(font1)
        self.postTitle.setTextFormat(Qt.AutoText)
        self.postTitle.setWordWrap(True)

        self.titleThumbLayout.addWidget(self.postTitle)

        self.thumbLabel = QLabel(self.frame)
        self.thumbLabel.setObjectName(u"thumbLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.thumbLabel.sizePolicy().hasHeightForWidth())
        self.thumbLabel.setSizePolicy(sizePolicy2)
        self.thumbLabel.setMaximumSize(QSize(150, 100))
        self.thumbLabel.setPixmap(QPixmap(u"../../../Downloads/reddit_thumb.jpg"))
        self.thumbLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.thumbLabel.setMargin(4)

        self.titleThumbLayout.addWidget(self.thumbLabel)


        self.verticalLayout.addLayout(self.titleThumbLayout)

        self.verticalLayout.setStretch(0, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.toolLayout = QHBoxLayout()
        self.toolLayout.setObjectName(u"toolLayout")
        self.commentsNumLabel = QLabel(self.frame)
        self.commentsNumLabel.setObjectName(u"commentsNumLabel")
        sizePolicy.setHeightForWidth(self.commentsNumLabel.sizePolicy().hasHeightForWidth())
        self.commentsNumLabel.setSizePolicy(sizePolicy)
        self.commentsNumLabel.setMaximumSize(QSize(120, 16777215))
        self.commentsNumLabel.setMargin(2)

        self.toolLayout.addWidget(self.commentsNumLabel, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.voteLayout = QHBoxLayout()
        self.voteLayout.setObjectName(u"voteLayout")
        self.downButton = QPushButton(self.frame)
        self.downButton.setObjectName(u"downButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy3)
        icon = QIcon()
        iconThemeName = u"arrow-down"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.downButton.setIcon(icon)

        self.voteLayout.addWidget(self.downButton, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.scoreLabel = QLabel(self.frame)
        self.scoreLabel.setObjectName(u"scoreLabel")
        sizePolicy2.setHeightForWidth(self.scoreLabel.sizePolicy().hasHeightForWidth())
        self.scoreLabel.setSizePolicy(sizePolicy2)
        self.scoreLabel.setLayoutDirection(Qt.RightToLeft)
        self.scoreLabel.setAlignment(Qt.AlignCenter)

        self.voteLayout.addWidget(self.scoreLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.upvButton = QPushButton(self.frame)
        self.upvButton.setObjectName(u"upvButton")
        sizePolicy3.setHeightForWidth(self.upvButton.sizePolicy().hasHeightForWidth())
        self.upvButton.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        iconThemeName = u"arrow-up"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.upvButton.setIcon(icon1)

        self.voteLayout.addWidget(self.upvButton, 0, Qt.AlignRight|Qt.AlignBottom)


        self.toolLayout.addLayout(self.voteLayout)


        self.verticalLayout_2.addLayout(self.toolLayout)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Post)

        QMetaObject.connectSlotsByName(Post)
    # setupUi

    def retranslateUi(self, Post):
        Post.setWindowTitle(QCoreApplication.translate("Post", u"Post", None))
        self.subName.setText(QCoreApplication.translate("Post", u"<html><head/><body><p><br/></p></body></html>", None))
        self.usrName.setText("")
        self.postTitle.setText("")
        self.thumbLabel.setText("")
        self.commentsNumLabel.setText(QCoreApplication.translate("Post", u"123 comments", None))
        self.downButton.setText("")
        self.scoreLabel.setText(QCoreApplication.translate("Post", u"123", None))
        self.upvButton.setText("")
    # retranslateUi

