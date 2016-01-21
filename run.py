import os
import sys
import logging

from PySide import QtGui

from controller import Controller

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    if sys.argv[0] == 'debug':
        logging_type = logging.DEBUG
    else:
        logging_type = logging.INFO

    App = Controller(app, root_dir=os.path.dirname(__file__), logging_type=logging_type)
    sys.exit(app.exec_())