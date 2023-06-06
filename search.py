from ui.ui_search import Ui_Search
from ui.ui_search_result import Ui_SearchResult
from qt_utils import get_qpixmap_from_url, remove_all_children
from PySide6.QtWidgets import QWidget
import praw
import logging

class ResultWidget(QWidget):
    def __init__(self, subreddit, clickedCallback, parent=None):
        super(ResultWidget, self).__init__(parent)
        self.ui = Ui_SearchResult()
        self.ui.setupUi(self)
        self.ui.SubNameLabel.setText(subreddit.display_name)
        self.ui.SubCountLabel.setText("members: " + str(subreddit.subscribers))
        try:
            self.ui.SubIconLabel.setPixmap(get_qpixmap_from_url(subreddit.icon_img))
        except:
            self.ui.SubIconLabel.setVisible(False)
        
        self.clickedCallback = clickedCallback
        self.subreddit = subreddit
        
    def mousePressEvent(self, _):
        logging.debug("selected sub " + self.subreddit.display_name)
        self.clickedCallback(self.subreddit)


class SearchWindow(QWidget):
    def __init__(self, chosenCallback, subreddits: praw.reddit.models.Subreddits, parent=None):
        super(SearchWindow, self).__init__(parent)
        self.ui = Ui_Search()
        self.ui.setupUi(self)
        self.ui.searchButton.clicked.connect(lambda: self.displaySearchResults(chosenCallback, subreddits))
        self.callback = chosenCallback

    def displaySearchResults(self, chosenCallback, subreddits: praw.reddit.models.Subreddits):
        remove_all_children(self.ui.searchResultsLayout)
        for subreddit in subreddits.search(query = self.ui.subNameEdit.text(), limit=30):
            self.ui.searchResultsLayout.addWidget(ResultWidget(subreddit, lambda selected_sub: self.callback(selected_sub)))
