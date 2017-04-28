from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

class color_select_dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.main_layout = QVBoxLayout(self)

        # properties of the dialog
        self.setWindowTitle("select your color")

        # widgets
        self.red_button = QPushButton()
        self.red_pic = QPixmap('../images/red_transparent')
        self.red_icon = QIcon(self.red_pic)
        self.red_button.setIcon(self.red_icon)
        self.red_button.setIconSize(self.red_pic.rect().size()*.4)

        self.black_button = QPushButton()
        self.black_pic = QPixmap('../images/black_transparent')
        self.black_icon = QIcon(self.black_pic)
        self.black_button.setIcon(self.black_icon)
        self.black_button.setIconSize(self.black_pic.rect().size()*.4)

        # button
        self.cancel_button = QPushButton("cancel")

        # layouts
        self.button_layout = QHBoxLayout()

        # adding widgets to layouts
        self.button_layout.addStretch(0)
        self.button_layout.addWidget(self.red_button)
        self.button_layout.addWidget(self.black_button)
        self.button_layout.addStretch(0)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.cancel_button, alignment=Qt.AlignCenter)


        # actions
        self.cancel_button.clicked.connect(self.cancel_clicked)
        # self.submit_button.clicked.connect(self.submit_clicked)

    def cancel_clicked(self):
        self.close()
