from ui.ui_comment import Ui_Comment
from PySide6.QtWidgets import (QWidget)
import praw
import markdown
from datetime import datetime


class Comment(QWidget):
    def __init__(self, comment: praw.reddit.models.Comment, parent=None):
        super(Comment, self).__init__(parent)
        self.ui = Ui_Comment()
        self.ui.setupUi(self)
        self.ui.commentLabel.setText(markdown.markdown(comment.body))
        self.ui.scoreLabel.setText(str(comment.score))
        self.ui.usrNameLabel.setText(comment.author.name)
        self.ui.timeLabel.setText(datetime.utcfromtimestamp(comment.created_utc).strftime("%Y.%m.%d %H:%M"))