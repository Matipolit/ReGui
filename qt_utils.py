from PySide6.QtWidgets import QWidget, QPushButton, QLayout
from urllib import request
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QThread, Signal


def remove_all_children(widget: QWidget | QLayout):
    for i in reversed(range(widget.count())):
        widget.itemAt(i).widget().setParent(None)


def get_qpixmap_from_url(url: str):
    img_data = request.urlopen(url).read()
    image = QImage()
    image.loadFromData(img_data)
    return QPixmap(image)


class GetPixmapThread(QThread):
    # Signals to relay thread progress to the main GUI thread
    progressSignal = Signal(int)
    completeSignal = Signal(str)

    def __init__(self, url: str, pixMapToFill: QPixmap, parent=None):
        super(GetPixmapThread, self).__init__(parent)
        self.maxRange = 100
        self.url = url
        self.pixmap = pixMapToFill

    def run(self):
        # blocking code goes here
        img_data = request.urlopen(self.url).read()
        self.pixmap.loadFromData(img_data)
        self.completeSignal.emit(self.completionMessage)


def color_buttons_according_to_vote(
    submission, upvButton: QPushButton, downButton: QPushButton
):
    if submission.likes == True:
        upvButton.setStyleSheet("background-color: rgba(0, 20, 220, 0.2);")
        downButton.setStyleSheet("")
    elif submission.likes == False:
        downButton.setStyleSheet("background-color: rgba(220, 20, 0, 0.2);")
        upvButton.setStyleSheet("")
    elif submission.likes is None:
        upvButton.setStyleSheet("")
        downButton.setStyleSheet("")
