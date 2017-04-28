#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

class rules_main_widget(QWidget):
    home_clicked_signal = pyqtSignal()
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
        self.menu_bar.show()

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("connect four instructions")
        self.title_font = QFont("Helvetica",40)
        self.title_font.setUnderline(True)
        self.title_label.setFont(self.title_font)

        # main description
        self.description = QLabel()
        self.description.setFixedSize(QDesktopWidget().width() * .33, QDesktopWidget().height()*.33)
        self.description_font = QFont("Helvetica",20)
        self.description.setFont(self.description_font)
        self.description.setWordWrap(True)
        self.description.setAlignment(Qt.AlignJustify)
        self.description.setText('To win Connect Four you must be the '
        'first player to get four of your colored checkers in a row either horizontally, '
        'vertically or diagonally. Each player will take turns dropping a piece of their '
        'color in one of the seven columns, until four are connected. Play vs the '
        'computer to see how it works! To play in this application, simply click '
        'the column in which you want to drop a piece.')

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addStretch(0)
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addSpacing(100)
        self.main_layout.addWidget(self.description, alignment=Qt.AlignCenter)
        self.main_layout.addStretch(0)
