from PySide6.QtWidgets import QWidget, QPushButton
from urllib import request
from PySide6.QtGui import QImage, QPixmap

def remove_all_children(widget: QWidget):
    for i in reversed(range(widget.count())): 
        widget.itemAt(i).widget().setParent(None)

def get_qpixmap_from_url(url: str):
    img_data = request.urlopen(url).read()
    image = QImage()
    image.loadFromData(img_data)
    return QPixmap(image)

def color_buttons_according_to_vote(submission, upvButton: QPushButton, downButton: QPushButton):
    if(submission.likes == True):
        upvButton.setStyleSheet("background-color: rgba(0, 20, 220, 0.2);")
        downButton.setStyleSheet("")
    elif(submission.likes == False):
        downButton.setStyleSheet("background-color: rgba(220, 20, 0, 0.2);")
        upvButton.setStyleSheet("")
    elif(submission.likes is None):
        upvButton.setStyleSheet("")
        downButton.setStyleSheet("")