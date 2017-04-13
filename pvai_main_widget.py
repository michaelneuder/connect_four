#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

class pvai_main_widget(QWidget):
    home_clicked_signal = pyqtSignal()
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("connect four")
        self.title_font = QFont("Times",40)
        self.title_font.setUnderline(True)
        self.title_label.setFont(self.title_font)


        # header widgets
        self.pvp_label = QLabel("player vs ai")
        self.pvp_font = QFont("Times",25)
        self.pvp_label.setFont(self.pvp_font)
        self.main_menu_push_button = QPushButton("main menu")
        self.close_save_push_button = QPushButton("save && close")

        # column selection widgets
        self.turn_label_p1 = QLabel("P1 turn")
        self.turn_label_p2 = QLabel("P2 turn")
        self.column_1_select_button = QPushButton("1")
        self.column_2_select_button = QPushButton("2")
        self.column_3_select_button = QPushButton("3")
        self.column_4_select_button = QPushButton("4")
        self.column_5_select_button = QPushButton("5")
        self.column_6_select_button = QPushButton("6")
        self.column_7_select_button = QPushButton("7")

        # table for representing board state
        self.board = QTableWidget()
        self.board.setWindowTitle("game state")
        self.board.resize(400, 250)
        self.board.setRowCount(6)
        self.board.setColumnCount(7)

        # footer widgets
        self.move_number_label = QLabel("move #")
        self.undo_button = QPushButton("undo")
        self.reset_push_button = QPushButton("reset")
        self.save_push_button = QPushButton("save current board")


    # # -------- layout declaration -------- # #
        self.header_layout = QHBoxLayout()
        self.column_selection_layout = QHBoxLayout()
        self.footer_layout = QHBoxLayout()

    # # -------- adding widgets to layouts -------- # #
        # header layout
        self.header_layout.addWidget(self.main_menu_push_button)
        self.header_layout.addStretch(0)
        self.header_layout.addWidget(self.pvp_label)
        self.header_layout.addStretch(0)
        self.header_layout.addWidget(self.close_save_push_button)

        # column_selection_layout
        self.column_selection_layout.addWidget(self.turn_label_p1)
        self.column_selection_layout.addStretch(0)
        self.column_selection_layout.addWidget(self.column_1_select_button)
        self.column_selection_layout.addWidget(self.column_2_select_button)
        self.column_selection_layout.addWidget(self.column_3_select_button)
        self.column_selection_layout.addWidget(self.column_4_select_button)
        self.column_selection_layout.addWidget(self.column_5_select_button)
        self.column_selection_layout.addWidget(self.column_6_select_button)
        self.column_selection_layout.addWidget(self.column_7_select_button)
        self.column_selection_layout.addStretch(0)
        self.column_selection_layout.addWidget(self.turn_label_p2)

        # footer layout
        self.footer_layout.addWidget(self.move_number_label)
        self.footer_layout.addStretch(0)
        self.footer_layout.addWidget(self.undo_button)
        self.footer_layout.addWidget(self.reset_push_button)
        self.footer_layout.addWidget(self.save_push_button)

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addLayout(self.column_selection_layout)
        self.main_layout.addWidget(self.board)
        self.main_layout.addLayout(self.footer_layout)

    # # -------- actions -------- # #
        self.main_menu_push_button.clicked.connect(self.main_menu_clicked)


    def exit_app(self):
        exit()

    def main_menu_clicked(self):
        self.home_clicked_signal.emit()
