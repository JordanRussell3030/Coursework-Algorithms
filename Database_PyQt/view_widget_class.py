from PyQt4.QtCore import *
from PyQt4.QtGui import *

def ViewWidgetZZZ(QWidget):
    def __init__(self):
        super().__init__()
        self.print_id = QLabel(id_)
        self.print_name = QLabel(name)
        self.go_back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.print_id)
        self.layout.addWidget(self.print_name)
        self.layout.addWidget(self.go_back)

        self.setLayout(self.layout)

        self.go_back.clicked.connect(self.back)

    def back(self):
        self.setCurrentIndex[0]

