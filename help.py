from ui.ui_help import Ui_Help
from PySide6.QtWidgets import QWidget

class Help(QWidget):
    def __init__(self, parent=None):
        super(Help, self).__init__(parent)
        self.ui = Ui_Help()
        self.ui.setupUi(self)

