# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginWidget(object):
    def setupUi(self, LoginWidget):
        if not LoginWidget.objectName():
            LoginWidget.setObjectName(u"LoginWidget")
        LoginWidget.resize(400, 300)
        self.gridLayout = QGridLayout(LoginWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loginButton = QPushButton(LoginWidget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setMaximumSize(QSize(200, 16777215))
        icon = QIcon(QIcon.fromTheme(u"arrow-right"))
        self.loginButton.setIcon(icon)

        self.verticalLayout.addWidget(self.loginButton, 0, Qt.AlignHCenter)

        self.authorizeButton = QPushButton(LoginWidget)
        self.authorizeButton.setObjectName(u"authorizeButton")
        self.authorizeButton.setMaximumSize(QSize(200, 16777215))
        icon1 = QIcon()
        iconThemeName = u"lastfm-personal"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.authorizeButton.setIcon(icon1)

        self.verticalLayout.addWidget(self.authorizeButton, 0, Qt.AlignHCenter)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(LoginWidget)

        QMetaObject.connectSlotsByName(LoginWidget)
    # setupUi

    def retranslateUi(self, LoginWidget):
        LoginWidget.setWindowTitle(QCoreApplication.translate("LoginWidget", u"Form", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWidget", u"Log in", None))
        self.authorizeButton.setText(QCoreApplication.translate("LoginWidget", u"Authorize with Reddit", None))
    # retranslateUi
