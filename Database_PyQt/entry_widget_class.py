from PyQt4.QtCore import *
from PyQt4.QtGui import *

from table_class import *

class EntryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.id_label = QLabel("ID")
        self.name_label = QLabel("Name")
        self.TeacherID = QLineEdit()
        self.Teachername = QLineEdit()
        self.add = QPushButton("Add")
        self.delete = QPushButton("Delete")
        self.view = QPushButton("View entries")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.TeacherID)
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.Teachername)
        self.layout.addWidget(self.add)
        self.layout.addWidget(self.delete)
        self.layout.addWidget(self.view)

        self.setLayout(self.layout)

        self.add.clicked.connect(self.submit_add)
        self.delete.clicked.connect(self.submit_delete)
        self.view.clicked.connect(self.view_entries)

    def submit_add(self):
        mydatabase = Database()
        mydatabase.create_data()
        mydatabase.append(self.name_label.text)
        mydatabase.append(self.id_label.text)

    def submit_delete(self):
        pass

    def view_entries(self):
        self.setCurrentIndex[1]
