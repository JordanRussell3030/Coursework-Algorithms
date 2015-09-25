import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from entry_widget_class import *
from view_widget_class import *

class EntryWindow(QMainWindow):
    """This class creates a main window to add in data to the database"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Entry Program")
        #self.view_widget = ViewWidgetZZZ()
        self.entry_widget = EntryWidget()

        self.stack = QStackedLayout()

        self.stack.addWidget(self.entry_widget)
        #self.stack.addWidget(self.view_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

def main():
    database_entry_program = QApplication(sys.argv)
    entry_window = EntryWindow()
    entry_window.show()
    entry_window.raise_()
    database_entry_program.exec_()

if __name__ == "__main__":
    main()
