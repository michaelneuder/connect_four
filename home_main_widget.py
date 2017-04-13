#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

class home_main_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("connect four")
        self.title_font = QFont("Helvetica",60)
        self.title_font.setUnderline(True)
        self.title_label.setFont(self.title_font)

        # menu buttons
        self.menu_button_font = QFont("Helvetica",30)
        self.rules_push_button = QPushButton("how to play")
        self.rules_push_button.setFixedSize(QDesktopWidget().width() * .21, QDesktopWidget().height()*.07)
        self.rules_push_button.setFont(self.menu_button_font)
        self.pvp_push_button = QPushButton("player vs player")
        self.pvp_push_button.setFixedSize(QDesktopWidget().width() * .21, QDesktopWidget().height()*.07)
        self.pvp_push_button.setFont(self.menu_button_font)
        self.pvai_push_button = QPushButton("player vs ai")
        self.pvai_push_button.setFixedSize(QDesktopWidget().width() * .21, QDesktopWidget().height()*.07)
        self.pvai_push_button.setFont(self.menu_button_font)
        self.game_history_push_button = QPushButton("game history")
        self.game_history_push_button.setFixedSize(QDesktopWidget().width() * .21, QDesktopWidget().height()*.07)
        self.game_history_push_button.setFont(self.menu_button_font)
        self.quit_push_button = QPushButton("quit")
        self.quit_push_button.setFixedSize(QDesktopWidget().width() * .21, QDesktopWidget().height()*.07)
        self.quit_push_button.setFont(self.menu_button_font)

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.rules_push_button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.pvp_push_button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.pvai_push_button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.game_history_push_button, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.quit_push_button, alignment=Qt.AlignCenter)


    def exit_app(self):
        exit()
