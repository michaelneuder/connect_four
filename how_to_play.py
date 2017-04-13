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

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("connect four instructions")
        self.title_font = QFont("Helvetica",40)
        self.title_font.setItalic(True)
        self.title_label.setFont(self.title_font)

        # main description
        self.description = QTextEdit()
        self.description.setFixedSize(QDesktopWidget().width() * .3, QDesktopWidget().height()*.3)
        self.description.setReadOnly(True)
        self.description_font = QFont("Helvetica",20)
        self.description.setFont(self.description_font)
        self.description.setText('Summary: To win Connect Four you must be the '
        'first player to get four of your colored checkers in a row either horizontally, '
        'vertically or diagonally. Each player will take turns dropping a piece of their '
        'color in one of the seven columns, until four are connected. Play vs the '
        'computer to see how it works!')

        # footer widgets
        self.main_menu_push_button = QPushButton("main menu")
        self.quit_push_button = QPushButton("quit")

    # # -------- layout declaration -------- # #
        self.footer_layout = QHBoxLayout()

    # # -------- adding widgets to layouts -------- # #
        self.footer_layout.addStretch(0)
        self.footer_layout.addWidget(self.main_menu_push_button)
        self.footer_layout.addWidget(self.quit_push_button)
        self.footer_layout.addStretch(0)

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.description, alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.footer_layout)


    # # -------- actions -------- # #
        self.quit_push_button.clicked.connect(self.exit_app)
        self.main_menu_push_button.clicked.connect(self.home_clicked)

    def exit_app(self):
        exit()

    def home_clicked(self):
        self.home_clicked_signal.emit()
