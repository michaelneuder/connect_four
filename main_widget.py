#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from home_main_widget import home_main_widget
from pvp_main_widget import pvp_main_widget
from pvai_main_widget import pvai_main_widget
from how_to_play import rules_main_widget

class main_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)

    # # -------- menu_bar item declaration -------- # #
        self.menu_bar = QMenuBar(self)
        self.file_menu = QMenu('file')

        # quit
        self.quit_action = QAction(QIcon('exit.png'), '&exit', self)
        self.quit_action.setShortcut('Ctrl+E')
        self.file_menu.addAction(self.quit_action)

    # # -------- add menus to menu_bar -------- # #
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.hide()

    # # -------- layout declaration -------- # #
        self.stack_layout = QStackedLayout()
        self.footer_layout = QHBoxLayout()
        self.footer_widget = QWidget()

    # # -------- widget declaration -------- # #
        # window widgets
        self.home_widget = home_main_widget()
        self.pvp_widget = pvp_main_widget()
        self.pvai_widget = pvai_main_widget()
        self.rules_widget = rules_main_widget()

        # footer widgets
        self.main_menu_push_button = QPushButton("main menu")
        self.rules_push_button = QPushButton("how to play")
        self.pvp_push_button = QPushButton("player v. player")
        self.pvai_push_button = QPushButton("player v. ai")
        self.quit_push_button = QPushButton("quit")

    # # -------- add to layouts -------- # #
        # stack layout
        self.stack_layout.addWidget(self.home_widget)
        self.stack_layout.addWidget(self.rules_widget)
        self.stack_layout.addWidget(self.pvp_widget)
        self.stack_layout.addWidget(self.pvai_widget)

        # footer layout
        self.footer_layout.addStretch(0)
        self.footer_layout.addWidget(self.main_menu_push_button)
        self.footer_layout.addWidget(self.rules_push_button)
        self.footer_layout.addWidget(self.pvp_push_button)
        self.footer_layout.addWidget(self.pvai_push_button)
        self.footer_layout.addWidget(self.quit_push_button)
        self.footer_layout.addStretch(0)

        # main layout
        self.main_layout.addLayout(self.stack_layout)
        self.main_layout.addLayout(self.footer_layout)

    # # -------- actions -------- # #
        self.main_menu_push_button.clicked.connect(self.main_menu_clicked)
        self.pvp_push_button.clicked.connect(self.pvp_clicked)
        self.pvai_push_button.clicked.connect(self.pvai_clicked)
        self.rules_push_button.clicked.connect(self.rules_clicked)
        self.quit_push_button.clicked.connect(self.quit_clicked)
        self.quit_action.triggered.connect(self.quit_clicked)
        self.home_widget.rules_push_button.clicked.connect(self.rules_clicked)
        self.home_widget.pvp_push_button.clicked.connect(self.pvp_clicked)
        self.home_widget.pvai_push_button.clicked.connect(self.pvai_clicked)
        self.home_widget.game_history_push_button.clicked.connect(self.game_history_clicked)
        self.home_widget.quit_push_button.clicked.connect(self.quit_clicked)

    def main_menu_clicked(self):
        self.stack_layout.setCurrentIndex(0)
        self.menu_bar.hide()

    def pvp_clicked(self):
        self.stack_layout.setCurrentIndex(2)
        self.menu_bar.show()

    def pvai_clicked(self):
        self.stack_layout.setCurrentIndex(3)
        self.menu_bar.show()

    def rules_clicked(self):
        self.stack_layout.setCurrentIndex(1)
        self.menu_bar.show()

    def game_history_clicked(self):
        print("game history")

    def quit_clicked(self):
        exit()
