from ui.ui_page import Ui_Page
from ui.ui_subreddit import Ui_SubHeader
from posts import SmallPost, BigPost
from search import SearchWindow
from help import Help
from qt_utils import remove_all_children, get_qpixmap_from_url
import pprint
from PySide6.QtWidgets import (
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QListView,
    QListWidget,
    QListWidgetItem,
    QWidget,
)
from PySide6 import QtCore
import logging
import praw


class FillSubmissionsThread(QtCore.QThread):
    progressSignal = QtCore.Signal(int)
    completeSignal = QtCore.Signal(str)

    def __init__(self, posts_iter, listToFill: list, number: int, parent=None):
        super(FillSubmissionsThread, self).__init__(parent)
        self.posts_iter = posts_iter
        self.listToFill = listToFill
        self.number = number

    def run(self):
        emitStep = self.number / 100.0
        for i in range(self.number):
            submission = self.posts_iter.__next__()
            self.listToFill.append(submission)
            self.progressSignal.emit(int(i / emitStep))
        self.completeSignal.emit("complete")


class SubHeader(QWidget):
    def __init__(
        self,
        name: str,
        subs: int,
        subscribed: bool,
        icon_url: str,
        sub_callback,
        parent=None,
    ):
        super(SubHeader, self).__init__(parent)
        self.ui = Ui_SubHeader()
        self.ui.setupUi(self)
        self.ui.nameLabel.setText(name)
        self.subCount = subs
        self.ui.subCountLabel.setText(str(subs) + " members")
        if not subscribed:
            self.update_ui_not_subscribed(sub_callback)
        else:
            self.update_ui_subscribed(sub_callback)
        try:
            self.ui.iconLabel.setPixmap(get_qpixmap_from_url(icon_url))
        except:
            logging.error("couldn't set subreddit icon")

    def update_ui_not_subscribed(self, sub_callback):
        self.ui.subButton.setText("Subscribe")
        self.ui.subButton.clicked.connect(
            lambda: self.run_sub_callback(sub_callback, True)
        )

    def update_ui_subscribed(self, sub_callback):
        self.ui.subButton.setText("Unsubscribe")
        self.ui.subButton.clicked.connect(
            lambda: self.run_sub_callback(sub_callback, False)
        )

    @QtCore.Slot()
    def run_sub_callback(self, sub_callback, subscribe: bool):
        if subscribe:
            sub_callback(True)
            self.subCount += 1
            self.update_ui_subscribed(sub_callback)
        else:
            sub_callback(False)
            self.subCount -= 1
            self.update_ui_not_subscribed(sub_callback)

        self.ui.subCountLabel.setText(str(self.subCount))


class Page(QWidget):
    def __init__(self, reddit: praw.Reddit, logout_callback, parent=None):
        super(Page, self).__init__(parent)
        self.ui = Ui_Page()
        self.ui.setupUi(self)
        self.ui.backButton.setVisible(False)
        self.ui.backButton.clicked.connect(self.go_back_in_history)
        self.ui.searchButton.clicked.connect(lambda: self.handle_search_button(reddit))
        self.ui.helpButton.clicked.connect(self.show_help)
        self.ui.logoutButton.clicked.connect(
            lambda: self.handle_logout_button(logout_callback)
        )
        self.ui.loadingPostsBar.setParent(self)
        self.ui.loadingPostsBar.setRange(0, 100)
        self.subHistory = []
        self.reddit = reddit

    @QtCore.Slot()
    def show_help(self):
        self.helpPage = Help()
        self.helpPage.show()

    @QtCore.Slot()
    def handle_logout_button(self, callback):
        callback()

    def handle_search_button(self, reddit: praw.Reddit):
        self.searchWindow = SearchWindow(
            lambda subreddit: self.handle_search_sub_clicked(subreddit),
            reddit.subreddits,
        )
        self.searchWindow.show()

    def handle_search_sub_clicked(self, subreddit: praw.reddit.models.Subreddit):
        self.populate(subreddit)
        self.searchWindow.close()
        self.searchWindow = None

    def handle_sub_button(self, subscribe, subreddit: praw.reddit.models.Subreddit):
        if subscribe:
            subreddit.subscribe()
        else:
            subreddit.unsubscribe()

    def populate(
        self, subreddit: praw.reddit.models.Subreddit | praw.reddit.models.Front
    ):
        self.subHistory.append(subreddit)
        if len(self.subHistory) > 1:
            self.ui.backButton.setVisible(True)
        remove_all_children(self.ui.pageScrollVerticalLayout)
        if isinstance(subreddit, praw.reddit.models.Front):
            self.ui.label.setText("Home")
        else:
            self.ui.label.setText(subreddit.display_name)
            logging.debug("Subreddit vars: " + pprint.pformat(vars(subreddit)))
            self.ui.pageScrollVerticalLayout.addWidget(
                SubHeader(
                    subreddit.display_name,
                    subreddit.subscribers,
                    subreddit.user_is_subscriber,
                    subreddit.icon_img,
                    lambda subscribe: self.handle_sub_button(subscribe, subreddit),
                )
            )
        self.sub_iterator = subreddit.hot(limit=1000)
        self.fill_submissions_list(10)

    def fill_submissions_list(self, number: int):
        submissions_list = []
        self.fillPostsThread = FillSubmissionsThread(
            self.sub_iterator, submissions_list, number
        )
        self.ui.loadingPostsBar.setVisible(True)
        self.fillPostsThread.start()
        self.fillPostsThread.completeSignal.connect(
            lambda event: self.addPostsFromList(submissions_list, number)
        )
        self.fillPostsThread.progressSignal.connect(
            lambda event: self.ui.loadingPostsBar.setValue(event)
        )

    @QtCore.Slot()
    def addPostsFromList(self, submissions_list: list, number: int):
        for submission in submissions_list:
            post_widget = SmallPost(
                self.reddit,
                submission,
                lambda submission: self.show_big_post(submission),
            )
            self.ui.pageScrollVerticalLayout.addWidget(post_widget)
        if hasattr(self, "moreButton"):
            self.ui.pageScrollVerticalLayout.removeWidget(self.moreButton)
            self.ui.pageScrollVerticalLayout.addWidget(self.moreButton)
        else:
            self.moreButton = QPushButton(text="Load more")
            self.moreButton.clicked.connect(lambda: self.fill_submissions_list(number))
            self.ui.pageScrollVerticalLayout.addWidget(self.moreButton)
        self.ui.loadingPostsBar.setValue(0)
        self.ui.loadingPostsBar.setVisible(False)

    def show_big_post(self, submission):
        remove_all_children(self.ui.postVerticalLayout)
        self.ui.postVerticalLayout.addWidget(
            BigPost(
                self.reddit,
                submission,
                clickedSubCallback=lambda subreddit: self.populate(subreddit),
            )
        )

    @QtCore.Slot()
    def go_back_in_history(self):
        if len(self.subHistory) > 1:
            self.subHistory.pop()
            self.populate(self.subHistory[-1])
            self.subHistory.pop()
        if len(self.subHistory) == 1:
            self.ui.backButton.setVisible(False)
