from PySide6.QtWidgets import QWidget
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