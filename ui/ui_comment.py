# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comment.ui'
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
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Comment(object):
    def setupUi(self, Comment):
        if not Comment.objectName():
            Comment.setObjectName(u"Comment")
        Comment.resize(677, 378)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Comment.sizePolicy().hasHeightForWidth())
        Comment.setSizePolicy(sizePolicy)
        Comment.setWindowOpacity(0.000000000000000)
        Comment.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(Comment)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Comment)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.usrNameLabel = QLabel(self.frame)
        self.usrNameLabel.setObjectName(u"usrNameLabel")

        self.horizontalLayout.addWidget(self.usrNameLabel)

        self.timeLabel = QLabel(self.frame)
        self.timeLabel.setObjectName(u"timeLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setItalic(False)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.timeLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.commentScrollArea = QScrollArea(self.frame)
        self.commentScrollArea.setObjectName(u"commentScrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.commentScrollArea.sizePolicy().hasHeightForWidth())
        self.commentScrollArea.setSizePolicy(sizePolicy3)
        self.commentScrollArea.setFrameShape(QFrame.Box)
        self.commentScrollArea.setFrameShadow(QFrame.Sunken)
        self.commentScrollArea.setLineWidth(1)
        self.commentScrollArea.setMidLineWidth(0)
        self.commentScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 643, 272))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.commentLabel = QLabel(self.scrollAreaWidgetContents)
        self.commentLabel.setObjectName(u"commentLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.commentLabel.sizePolicy().hasHeightForWidth())
        self.commentLabel.setSizePolicy(sizePolicy4)
        self.commentLabel.setTextFormat(Qt.RichText)
        self.commentLabel.setWordWrap(True)
        self.commentLabel.setOpenExternalLinks(True)

        self.gridLayout_2.addWidget(self.commentLabel, 0, 0, 1, 1)

        self.commentScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.commentScrollArea)

        self.scoreLayout = QHBoxLayout()
        self.scoreLayout.setObjectName(u"scoreLayout")
        self.downButton = QPushButton(self.frame)
        self.downButton.setObjectName(u"downButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy5)
        icon = QIcon()
        iconThemeName = u"arrow-down"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.downButton.setIcon(icon)

        self.scoreLayout.addWidget(self.downButton)

        self.scoreLabel = QLabel(self.frame)
        self.scoreLabel.setObjectName(u"scoreLabel")
        sizePolicy.setHeightForWidth(self.scoreLabel.sizePolicy().hasHeightForWidth())
        self.scoreLabel.setSizePolicy(sizePolicy)
        self.scoreLabel.setLayoutDirection(Qt.RightToLeft)
        self.scoreLabel.setAlignment(Qt.AlignCenter)

        self.scoreLayout.addWidget(self.scoreLabel)

        self.upvButton = QPushButton(self.frame)
        self.upvButton.setObjectName(u"upvButton")
        sizePolicy5.setHeightForWidth(self.upvButton.sizePolicy().hasHeightForWidth())
        self.upvButton.setSizePolicy(sizePolicy5)
        icon1 = QIcon()
        iconThemeName = u"arrow-up"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.upvButton.setIcon(icon1)

        self.scoreLayout.addWidget(self.upvButton)


        self.verticalLayout_2.addLayout(self.scoreLayout)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Comment)

        QMetaObject.connectSlotsByName(Comment)
    # setupUi

    def retranslateUi(self, Comment):
        Comment.setWindowTitle(QCoreApplication.translate("Comment", u"Form", None))
        self.usrNameLabel.setText(QCoreApplication.translate("Comment", u"Laeri", None))
        self.timeLabel.setText(QCoreApplication.translate("Comment", u"4 hr. ago", None))
        self.commentLabel.setText(QCoreApplication.translate("Comment", u"<html><head/><body><p>Is this idiomatic when I implement the <span style=\" font-family:'JetBrainsMono Nerd Font Mono';\">From</span> trait for a struct such as <span style=\" font-family:'JetBrainsMono Nerd Font Mono';\">impl From&lt;FromStruct&gt; for TargetStruct</span> which is a consuming function that I also implement: <span style=\" font-family:'JetBrainsMono Nerd Font Mono';\">impl From&lt;&amp;FromStruct&gt; for TargetStruct</span>? And is it also idiomatic when I just refer to the from method for the reference such as: <span style=\" font-family:'JetBrainsMono Nerd Font Mono';\">impl From&lt;FromStruct&gt; for TargetStruct { fn from(value: FromStruct) { From::&lt;&amp;FromStruct&gt;::from(&amp;value) } }</span> I assume this is no problem as long as we do not unnecessarily need to clone fields from the struct within the from method that requires a reference as we could just move them over with 'move' version. However, in my case I need to call <span style=\" font-family:'JetBrainsMono Nerd Font Mono'"
                        ";\">into</span> from some fields within the <span style=\" font-family:'JetBrainsMono Nerd Font Mono';\">FromStruct</span> anyways to build the <span style=\" font-family:'JetBrainsMono Nerd Font Mono';\">TargetStruct</span>.</p></body></html>", None))
        self.downButton.setText("")
        self.scoreLabel.setText(QCoreApplication.translate("Comment", u"123", None))
        self.upvButton.setText("")
    # retranslateUi

