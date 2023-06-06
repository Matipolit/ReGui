import praw
import locale
import argparse
import sys
import logging
from ui.ui_login import Ui_LoginWidget
from pages import Page
from data_handling import DataHandler
from state import AppState
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QStackedLayout, QWidget


locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")

parser = argparse.ArgumentParser(prog="ReGui", description="A Reddit GUI using PySide6")

parser.add_argument("-l", "--loglevel")
args = parser.parse_args()
if args.loglevel is not None:
    loglevel = args.loglevel
else:
    loglevel = "info"

numeric_level = getattr(logging, loglevel.upper(), None)
print(f"log level: {numeric_level}")
if not isinstance(numeric_level, int):
    raise ValueError("Invalid log level: %s" % loglevel)

mylogger = logging.getLogger()
mylogger.setLevel(numeric_level)

stdout_handler = logging.StreamHandler(stream=sys.stdout)
mylogger.addHandler(stdout_handler)


data_handler = DataHandler()
token = data_handler.get_token()
if token is None or token == "":
    reddit = praw.Reddit(
        client_id="0pwzprPqEpM2CQqnAie3_g",
        client_secret="-iXVV7jUiIIoR0wIX9wemkWnxUTV7g",
        user_agent="ReGui6",
        redirect_uri="http://localhost:8080/authorize",
    )
else:
    reddit = praw.Reddit(
        client_id="0pwzprPqEpM2CQqnAie3_g",
        client_secret="-iXVV7jUiIIoR0wIX9wemkWnxUTV7g",
        refresh_token=token,
        user_agent="ReGui6",
    )


class MainLayout(QWidget):
    def __init__(self, parent=None):
        super(MainLayout, self).__init__(parent)
        self.resize(1000, 600)
        self.state = AppState.LOGIN
        self.layout = QStackedLayout(self)
        self.login_widget = QWidget()
        self.login_widget.ui = Ui_LoginWidget()
        self.login_widget.ui.setupUi(self.login_widget)
        self.login_widget.ui.authorizeButton.clicked.connect(self.authorize_first_time)
        self.login_widget.ui.loginButton.clicked.connect(self.login)
        self.update_login_buttons()
        self.layout.addWidget(self.login_widget)

        self.page_widget = Page(reddit, self.logout_callback)
        self.layout.addWidget(self.page_widget)
        self.update_ui()

    def logout_callback(self):
        self.state = AppState.LOGIN
        self.update_ui()

    def update_ui(self):
        match self.state:
            case AppState.LOGIN:
                self.layout.setCurrentIndex(0)
                self.update_login_buttons()
            case AppState.LOGGED_IN:
                self.layout.setCurrentIndex(1)
                self.populate_page_with_posts(reddit.front)

    @QtCore.Slot()
    def populate_page_with_posts(self, subreddit):
        self.page_widget.populate(subreddit)

    @QtCore.Slot()
    def update_login_buttons(self):
        if reddit.user.me() is not None:
            self.login_widget.ui.authorizeButton.setVisible(False)
            self.login_widget.ui.loginButton.setVisible(True)
            self.login_widget.ui.loginButton.setText(
                f"Log in as {reddit.user.me().name}"
            )
        else:
            self.login_widget.ui.authorizeButton.setVisible(True)
            self.login_widget.ui.loginButton.setVisible(False)

    @QtCore.Slot()
    def authorize_first_time(self):
        data_handler.authorize_first_time(reddit)
        self.update_login_buttons()

    @QtCore.Slot()
    def login(self):
        self.state = AppState.LOGGED_IN
        self.update_ui()


app = QApplication(sys.argv)
app.setApplicationDisplayName("ReGui")

main_layout = MainLayout()
main_layout.show()
sys.exit(app.exec())
