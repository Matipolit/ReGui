from ui.ui_post import Ui_Post
from ui.ui_post_big import Ui_BigPost
from PySide6.QtWidgets import (QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListView, QListWidget, QListWidgetItem, QWidget)
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtCore import Slot
from urllib import request
from qt_utils import get_qpixmap_from_url, color_buttons_according_to_vote
from comments import Comment
import webbrowser
import logging
import pprint
import praw
import markdown


class SmallPost(QWidget):
    def __init__(self, reddit:praw.Reddit, submission: praw.reddit.models.Submission, clickedCallback, parent=None):
        super(SmallPost, self).__init__(parent)
        self.ui = Ui_Post()
        self.ui.setupUi(self)
        self.ui.subName.setText(submission.subreddit_name_prefixed)
        try:
            if(submission.author is None):
                self.ui.usrName.setText("[deleted]")
            else:
                self.ui.usrName.setText("u/" + submission.author.name)
        except: 
            logging.error("Error while setting author name")
            logging.error(pprint.pformat(vars(submission)))
        self.ui.postTitle.setText(submission.title)
        self.ui.commentsNumLabel.setText("Comments: " + str(submission.num_comments))
        self.ui.scoreLabel.setText(str(submission.score))
        self.ui.downButton.clicked.connect(self.downvote)
        self.ui.upvButton.clicked.connect(self.upvote)
        self.reddit = reddit

        if(submission.url is not None and submission.thumbnail is not None and submission.thumbnail != "self" and submission.thumbnail != "default" and submission.thumbnail != "nsfw"):
            self.ui.thumbLabel.setPixmap(get_qpixmap_from_url(submission.thumbnail))

        self.clickedCallback = clickedCallback
        self.submission = submission
        color_buttons_according_to_vote(submission, self.ui.upvButton, self.ui.downButton)

    @Slot()
    def upvote(self):
        self.submission.upvote()
        self.submission = self.reddit.submission(self.submission.id)
        self.ui.scoreLabel.setText(str(self.submission.score))
        color_buttons_according_to_vote(self.submission, self.ui.upvButton, self.ui.downButton)

    @Slot()
    def downvote(self):
        self.submission.downvote()
        self.submission = self.reddit.submission(self.submission.id)
        self.ui.scoreLabel.setText(str(self.submission.score))
        color_buttons_according_to_vote(self.submission, self.ui.upvButton, self.ui.downButton)

    def mousePressEvent(self, event):
        self.clickedCallback(self.submission)


class BigPost(QWidget):
    def __init__(self, reddit:praw.Reddit, submission: praw.reddit.models.Submission, clickedSubCallback, parent=None):
        super(BigPost, self).__init__(parent)
        self.ui = Ui_BigPost()
        self.ui.setupUi(self)
        self.ui.subName.setText(submission.subreddit_name_prefixed)
        self.ui.subName.mousePressEvent = lambda event: clickedSubCallback(submission.subreddit)
        try:
            if(submission.author is None):
                self.ui.usrName.setText("[deleted]")
            else:
                self.ui.usrName.setText("u/" + submission.author.name)
        except: 
            logging.error("Error while setting author name")
            logging.error(pprint.pformat(vars(submission)))
        
        self.ui.postTitle.setText(submission.title)
        self.ui.downButton.clicked.connect(self.downvote)
        self.ui.upvButton.clicked.connect(self.upvote)
        self.reddit = reddit
        logging.debug("comments: " + pprint.pformat(vars(submission.comments)))

        if(submission.selftext is not None and submission.selftext is not ""):
            self.ui.postContent.setText(markdown.markdown(submission.selftext))
        else:
            self.ui.contentScrollArea.setVisible(False)

        if(hasattr(submission, "preview") and submission.preview["enabled"] == True and submission.preview["images"] is not None):
            #logging.debug("images: " + str(submission.preview["images"]))
            if(len(submission.preview["images"][0]) == 1):
                img_metadata = submission.preview["images"][0]["resolutions"][0]
            else:
                img_metadata = submission.preview["images"][0]["resolutions"][-1]

            if(img_metadata["width"] > 500):
                self.ui.linkImgLabel.setFixedWidth(500)
                self.ui.linkImgLabel.setFixedHeight((500 / img_metadata["width"]) * img_metadata["height"] )
            self.ui.linkImgLabel.setPixmap(get_qpixmap_from_url(img_metadata["url"]))
            self.ui.linkImgLabel.mouseDoubleClickEvent = lambda event: webbrowser.open(submission.url)
        else:
            self.ui.linkImgLabel.setVisible(False)

        if(hasattr(submission, "url_overridden_by_dest")):
            self.ui.urlButton.clicked.connect(self.goToLink)
        else:
            self.ui.urlButton.setVisible(False)

        self.ui.commentsNumLabel.setText("Comments: " + str(submission.num_comments))
        self.ui.scoreLabel.setText(str(submission.score))
        self.submission = submission

        color_buttons_according_to_vote(submission, self.ui.upvButton, self.ui.downButton)

        for comment in submission.comments:
            self.ui.verticalLayout.addWidget(Comment(comment))

    @Slot()
    def upvote(self):
        self.submission.upvote()
        self.submission = self.reddit.submission(self.submission.id)
        self.ui.scoreLabel.setText(str(self.submission.score))
        color_buttons_according_to_vote(self.submission, self.ui.upvButton, self.ui.downButton)

    @Slot()
    def downvote(self):
        self.submission.downvote()
        self.submission = self.reddit.submission(self.submission.id)
        self.ui.scoreLabel.setText(str(self.submission.score))
        color_buttons_according_to_vote(self.submission, self.ui.upvButton, self.ui.downButton)

    @Slot()
    def goToLink(self):
        webbrowser.open(self.submission.url_overridden_by_dest)