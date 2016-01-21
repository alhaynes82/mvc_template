from view import View
from model import Model


class Controller():

    def __init__(self, app, root_dir, logging_type, *args, **kwargs):
        self.app = app
        self.root_dir = root_dir
        self.view = View()
        self.view.ui.setupUi(self.view)
        self.model = Model('')