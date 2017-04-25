#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from dialogs.playback_dialog import playback_dialog
import sqlite3

class game_history_main_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)
        self.moves = ''

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("saved games")
        self.title_font = QFont("Helvetica",40)
        self.title_font.setUnderline(True)
        self.title_label.setFont(self.title_font)

        # list
        self.game_history_list = []
        self.game_history_list_widget = QListWidget()
        self.game_history_list_widget.setFixedSize(self.width(), self.height())
        self.populate_list()

        # footer
        self.open_game_button = QPushButton("open game")
        self.load_game_button = QPushButton("load game")
        self.delete_game_button = QPushButton("delete game")
        self.footer_layout = QHBoxLayout()
        self.footer_layout.addStretch(0)
        self.footer_layout.addWidget(self.open_game_button)
        self.footer_layout.addWidget(self.load_game_button)
        self.footer_layout.addWidget(self.delete_game_button)
        self.footer_layout.addStretch(0)

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addStretch(0)
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addSpacing(100)
        self.main_layout.addWidget(self.game_history_list_widget, alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.footer_layout)
        self.main_layout.addStretch(0)

    ## actions
        self.game_history_list_widget.itemDoubleClicked.connect(self.game_selected)
        self.open_game_button.clicked.connect(self.game_selected)
        self.load_game_button.clicked.connect(self.update_move_string)
        self.delete_game_button.clicked.connect(self.delete_game)

    def populate_list(self):
        self.game_history_list_widget.clear()
        self.game_history_list = []
        connection = sqlite3.connect('../database/game_history.db')
        cursor = connection.cursor()
        for row in connection.execute('SELECT * from history1'):
            self.game_history_list_widget.addItem('game description --- \"' + str(row[0]) + '\"')
            self.game_history_list.append(row)
        connection.close()

    def game_selected(self):
        dialog = playback_dialog(self.game_history_list[self.game_history_list_widget.currentRow()][1])
        dialog.exec_()

    def update_move_string(self):
        self.moves = self.game_history_list[self.game_history_list_widget.currentRow()][1]

    def delete_game(self):
        description = self.game_history_list[self.game_history_list_widget.currentRow()][0]
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('are you sure you want to delete this game?')
        msg.setWindowTitle("confirm")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()
        if(retval == QMessageBox.Yes):
            connection = sqlite3.connect('../database/game_history.db')
            cursor = connection.cursor()
            cursor.execute("DELETE FROM history1 where game_description=(?)",(description,))
            connection.commit()
            self.populate_list()
            connection.close()
