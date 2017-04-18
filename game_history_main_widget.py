#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

class game_history_main_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("game history")
        self.title_font = QFont("Helvetica",40)
        # self.title_font.setItalic(True)
        self.title_label.setFont(self.title_font)

        # list
        self.game_histroy_list = []
        self.game_history_list_widget = QListWidget()
        self.populate_list()

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addStretch(0)
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.game_history_list_widget, alignment=Qt.AlignCenter)
        self.main_layout.addStretch(0)


    def populate_list(self):
        self.game_history_list_widget.clear()
        connection = sqlite3.connect('database/game_history.db')
        cursor = connection.cursor()
        for row in connection.execute('SELECT * from history'):
            self.game_history_list_widget.addItem('game id: ' + str(row[0]) + ' moves: ' + row[1])
            self.game_histroy_list.append(row)
        connection.close()
