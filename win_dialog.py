from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3


class win_dialog(QDialog):
    def __init__(self, color):
        QDialog.__init__(self)
        self.main_layout = QVBoxLayout(self)
        self.color = color

        # properties of the dialog
        self.setWindowTitle("winner!!")

        # main title
        self.title_label = QLabel("game over!")
        self.title_font = QFont("Helvetica",40)
        self.title_label.setFont(self.title_font)

        # red win
        self.red_label = QLabel("red player wins!")
        self.red_font = QFont("Helvetica",20)
        self.red_label.setFont(self.red_font)

        # black win
        self.black_label = QLabel("black player wins!")
        self.black_font = QFont("Helvetica",20)
        self.black_label.setFont(self.black_font)

        # player images
        self.p1_file = 'images/red.png'
        self.p1_image = QPixmap(self.p1_file)
        self.p2_file = 'images/black.png'
        self.p2_image = QPixmap(self.p2_file)
        self.p1_label = QLabel()
        self.p1_label.setFrameStyle(QFrame.Panel)
        self.p1_label.setLineWidth(2)
        # self.p1_label.setStyleSheet("QLabel { background-color : rgb(184,184,186) ;border: solid; border-radius: 10px; border-color: black; border-width: 2px }")
        self.p1_label.setFixedSize(self.height() * .1, self.height() * .1)
        self.p1_label.setPixmap(self.p1_image)
        self.p1_label.setScaledContents(True)
        self.p2_label = QLabel()
        self.p2_label.setFrameStyle(QFrame.Panel)
        self.p2_label.setLineWidth(2)
        # self.p1_label.setStyleSheet("QLabel { background-color : rgb(184,184,186) ;border: solid; border-radius: 10px; border-color: black; border-width: 2px }")
        self.p2_label.setFixedSize(self.height() * .1, self.height() * .1)
        self.p2_label.setPixmap(self.p2_image)
        self.p2_label.setScaledContents(True)

        # button
        self.ok_button = QPushButton("ok")

        # layouts
        self.red_layout = QHBoxLayout()
        self.black_layout = QHBoxLayout()

        # adding widgets to layouts
        self.main_layout.addWidget(self.title_label)
        # self.main_layout.addWidget(self.red_label)
        # self.main_layout.addWidget(self.black_label)
        # self.main_layout.addWidget(self.p1_label)
        self.red_layout.addWidget(self.p1_label)
        self.red_layout.addWidget(self.red_label)
        self.black_layout.addWidget(self.p2_label)
        self.black_layout.addWidget(self.black_label)
        self.main_layout.addLayout(self.red_layout)
        self.main_layout.addLayout(self.black_layout)
        self.main_layout.addWidget(self.ok_button, alignment=Qt.AlignCenter)


        # actions
        self.ok_button.clicked.connect(self.ok_clicked)

        if(self.color == 'red'):
            self.red_win()
        elif(self.color == 'black'):
            self.black_win()

    def red_win(self):
        self.black_label.hide()
        self.p2_label.hide()
        self.red_label.show()
        self.p1_label.show()

    def black_win(self):
        self.red_label.hide()
        self.p1_label.hide()
        self.black_label.show()
        self.p2_label.show()

    def ok_clicked(self):
        self.close()
