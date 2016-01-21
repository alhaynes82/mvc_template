from PySide import QtGui


from view.ui.main import Ui_MainWindow


class View(QtGui.QMainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()