from ui.ui_comment import Ui_Comment
from PySide6.QtWidgets import QWidget
import praw
import markdown
from datetime import datetime
from qt_utils import color_buttons_according_to_vote


class Comment(QWidget):
    def __init__(self, comment: praw.reddit.models.Comment, parent=None):
        super(Comment, self).__init__(parent)
        self.ui = Ui_Comment()
        self.ui.setupUi(self)
        self.ui.commentLabel.setText(markdown.markdown(comment.body))
        self.ui.scoreLabel.setText(str(comment.score))
        if comment.author is not None:
            self.ui.usrNameLabel.setText(comment.author.name)
        else:
            self.ui.usrNameLabel.setText("[deleted]")
        self.ui.timeLabel.setText(
            datetime.utcfromtimestamp(comment.created_utc).strftime("%Y.%m.%d %H:%M")
        )
        self.ui.downButton.clicked.connect(
            lambda: self.downvote(comment, score)(comment, comment.score)
        )
        self.ui.upvButton.clicked.connect(lambda: self.upvote(comment, comment.score))
        color_buttons_according_to_vote(comment, self.ui.upvButton, self.ui.downButton)

    def upvote(self, comment: praw.reddit.models.Comment, score: int):
        comment.upvote()
        comment.refresh()
        self.ui.scoreLabel.setText(str(comment.score))
        color_buttons_according_to_vote(comment, self.ui.upvButton, self.ui.downButton)

    def downvote(self, comment, score: int):
        comment.downvote()
        comment.refresh()
        self.ui.scoreLabel.setText(str(comment.score))
        color_buttons_according_to_vote(comment, self.ui.upvButton, self.ui.downButton)
