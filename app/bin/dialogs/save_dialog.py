from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

class save_dialog(QDialog):
    def __init__(self, move_history):
        QDialog.__init__(self)
        self.main_layout = QVBoxLayout(self)
        self.moves = move_history

        # properties of the dialog
        self.setWindowTitle("saving game")

        # widgets
        self.title_label = QLabel("enter a game description")
        self.title_font = QFont("Helvetica",20)
        self.title_label.setFont(self.title_font)
        self.description = QLineEdit()

        # button
        self.submit_button = QPushButton("submit")
        self.cancel_button = QPushButton("cancel")

        # layouts
        self.button_layout = QHBoxLayout()

        # adding widgets to layouts
        self.button_layout.addStretch(0)
        self.button_layout.addWidget(self.submit_button)
        self.button_layout.addWidget(self.cancel_button)
        self.button_layout.addStretch(0)
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.description, alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.button_layout)


        # actions
        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.submit_button.clicked.connect(self.submit_clicked)

    def submit_clicked(self):
        text = self.description.text()
        move_string = ''
        for i in self.moves:
            move_string+=(str(i))
        connection = sqlite3.connect('../database/game_history.db')
        cursor = connection.cursor()
        connection.execute("INSERT into history1 values (?, ?)", (text, move_string))
        connection.commit()
        connection.close()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('game was saved to database')
        msg.setWindowTitle("success")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        self.close()

    def cancel_clicked(self):
        self.close()
