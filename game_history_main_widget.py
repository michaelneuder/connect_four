#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from playback_dialog import playback_dialog
import sqlite3

class game_history_main_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)
        self.selection_change_count = 0

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("game history")
        self.title_font = QFont("Helvetica",40)
        self.title_font.setUnderline(True)
        self.title_label.setFont(self.title_font)

        # list
        self.game_history_list = []
        self.game_history_list_widget = QListWidget()
        self.game_history_list_widget.setFixedSize(self.width(), self.height())
        self.populate_list()

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addStretch(0)
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addSpacing(100)
        self.main_layout.addWidget(self.game_history_list_widget, alignment=Qt.AlignCenter)
        self.main_layout.addStretch(0)

    ## actions
        self.game_history_list_widget.currentRowChanged.connect(self.game_selected)


    def populate_list(self):
        self.game_history_list_widget.clear()
        connection = sqlite3.connect('database/game_history.db')
        cursor = connection.cursor()
        for row in connection.execute('SELECT * from history'):
            self.game_history_list_widget.addItem('game id: ' + str(row[0]) + ' moves: ' + row[1])
            self.game_history_list.append(row)
        connection.close()

    def game_selected(self, number):
        self.selection_change_count+=1
        if(self.selection_change_count > 1):
            dialog = playback_dialog(self.game_history_list[number][1])
            dialog.exec_()
