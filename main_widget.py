#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
from main_widgets.home_main_widget import home_main_widget
from main_widgets.pvp_main_widget import pvp_main_widget
from main_widgets.pvai_main_widget import pvai_main_widget
from main_widgets.how_to_play import rules_main_widget
from main_widgets.game_history_main_widget import game_history_main_widget

class main_widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)

    # # -------- menu_bar item declaration -------- # #
        self.menu_bar = QMenuBar(self)
        self.file_menu = QMenu('file')
        self.game_menu = QMenu('game')

        # quit
        self.quit_action = QAction(QIcon('exit.png'), '&exit', self)
        self.quit_action.setShortcut('Ctrl+E')
        self.file_menu.addAction(self.quit_action)

        # undo
        self.undo_action = QAction(QIcon('exit.png'), 'undo', self)
        self.undo_action.setShortcut('Ctrl+Z')
        self.game_menu.addAction(self.undo_action)

        # reset
        self.reset_action = QAction(QIcon('exit.png'), '&reset', self)
        self.reset_action.setShortcut('Ctrl+R')
        self.game_menu.addAction(self.reset_action)

        # save
        self.save_action = QAction(QIcon('exit.png'), '&save', self)
        self.save_action.setShortcut('Ctrl+S')
        self.file_menu.addAction(self.save_action)

        # load
        self.load_action = QAction(QIcon('exit.png'), '&load', self)
        self.load_action.setShortcut('Ctrl+L')
        self.file_menu.addAction(self.load_action)

    # # -------- add menus to menu_bar -------- # #
        self.menu_bar.addMenu(self.file_menu)
        self.menu_bar.addMenu(self.game_menu)
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
        self.game_history_widget = game_history_main_widget()

        # footer widgets
        self.main_menu_push_button = QPushButton("main menu")
        self.rules_push_button = QPushButton("how to play")
        self.pvp_push_button = QPushButton("player v. player")
        self.pvai_push_button = QPushButton("player v. ai")
        self.game_history_push_button = QPushButton("game history")
        self.quit_push_button = QPushButton("quit")

    # # -------- add to layouts -------- # #
        # stack layout
        self.stack_layout.addWidget(self.home_widget)
        self.stack_layout.addWidget(self.rules_widget)
        self.stack_layout.addWidget(self.pvp_widget)
        self.stack_layout.addWidget(self.pvai_widget)
        self.stack_layout.addWidget(self.game_history_widget)

        # footer layout
        self.footer_layout.addStretch(0)
        self.footer_layout.addWidget(self.main_menu_push_button)
        self.footer_layout.addWidget(self.rules_push_button)
        self.footer_layout.addWidget(self.pvp_push_button)
        self.footer_layout.addWidget(self.pvai_push_button)
        self.footer_layout.addWidget(self.game_history_push_button)
        self.footer_layout.addWidget(self.quit_push_button)
        self.footer_layout.addStretch(0)

        # hiding upon opening bc menu
        self.main_menu_push_button.hide()
        self.pvp_push_button.hide()
        self.pvai_push_button.hide()
        self.rules_push_button.hide()
        self.game_history_push_button.hide()
        self.quit_push_button.hide()

        # main layout
        self.main_layout.addLayout(self.stack_layout)
        self.main_layout.addLayout(self.footer_layout)

    # # -------- actions -------- # #
        self.main_menu_push_button.clicked.connect(self.main_menu_clicked)
        self.pvp_push_button.clicked.connect(self.pvp_clicked)
        self.pvai_push_button.clicked.connect(self.pvai_clicked)
        self.rules_push_button.clicked.connect(self.rules_clicked)
        self.game_history_push_button.clicked.connect(self.game_history_clicked)
        self.quit_push_button.clicked.connect(self.quit_clicked)
        self.quit_action.triggered.connect(self.quit_clicked)
        self.home_widget.rules_push_button.clicked.connect(self.rules_clicked)
        self.home_widget.pvp_push_button.clicked.connect(self.pvp_clicked)
        self.home_widget.pvai_push_button.clicked.connect(self.pvai_clicked)
        self.home_widget.game_history_push_button.clicked.connect(self.game_history_clicked)
        self.home_widget.quit_push_button.clicked.connect(self.quit_clicked)
        self.undo_action.triggered.connect(self.undo_clicked)
        self.reset_action.triggered.connect(self.reset_clicked)
        self.save_action.triggered.connect(self.save_clicked)
        self.load_action.triggered.connect(self.load_clicked)

    def main_menu_clicked(self):
        self.stack_layout.setCurrentIndex(0)
        self.hide_footer()

    def pvp_clicked(self):
        self.stack_layout.setCurrentIndex(2)
        self.show_footer()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('welcome to the player vs player game. red goes first, and '
        'you can simply click on the column where you want to place your piece!')
        msg.setWindowTitle("player vs player")
        msg.setStandardButtons(QMessageBox.Ok)
        # retval = msg.exec_()

    def pvai_clicked(self):
        self.stack_layout.setCurrentIndex(3)
        self.show_footer()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('welcome to the player vs ai game. red goes first, and '
        'you can simply click on the column where you want to place your piece!')
        msg.setWindowTitle("player vs ai")
        msg.setStandardButtons(QMessageBox.Ok)
        # retval = msg.exec_()

    def rules_clicked(self):
        self.stack_layout.setCurrentIndex(1)
        self.show_footer()

    def game_history_clicked(self):
        self.stack_layout.setCurrentIndex(4)
        self.show_footer()

    def undo_clicked(self):
        self.stack_layout.setCurrentIndex(2)
        self.pvp_widget.undo_clicked()

    def reset_clicked(self):
        self.stack_layout.setCurrentIndex(2)
        self.pvp_widget.reset_clicked()

    def save_clicked(self):
        self.pvp_widget.save_clicked()
        self.stack_layout.setCurrentIndex(2)

    def load_clicked(self):
        self.stack_layout.setCurrentIndex(2)

    def hide_footer(self):
        self.menu_bar.hide()
        self.main_menu_push_button.hide()
        self.pvp_push_button.hide()
        self.pvai_push_button.hide()
        self.rules_push_button.hide()
        self.game_history_push_button.hide()
        self.quit_push_button.hide()

    def show_footer(self):
        self.menu_bar.show()
        self.main_menu_push_button.show()
        self.pvp_push_button.show()
        self.pvai_push_button.show()
        self.rules_push_button.show()
        self.game_history_push_button.show()
        self.quit_push_button.show()

    def quit_clicked(self):
        exit()
