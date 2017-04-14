#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from cf_mod import cf
import sqlite3

class pvp_main_widget(QWidget):
    home_clicked_signal = pyqtSignal()
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)

    # # ------- connect four stuff --------- # #
        self.test = cf()
        self.keep_going = True
        self.move_number = 1
        self.num_rows = 6
        self.num_cols = 7

    # # -------- widget declaration -------- # #
        # main title
        self.title_label = QLabel("connect four")
        self.title_font = QFont("Times",40)
        self.title_font.setUnderline(True)
        self.title_label.setFont(self.title_font)

        # cell images
        self.file = "empty_cell.png"
        self.empty_cell = QPixmap(self.file)
        self.file_red = "red.png"
        self.red_cell = QPixmap(self.file_red)
        self.file_black = "black.png"
        self.black_cell = QPixmap(self.file_black)



        # header widgets
        self.pvp_label = QLabel("player vs player")
        self.pvp_font = QFont("Times",25)
        self.pvp_label.setFont(self.pvp_font)

        # table for representing board state
        self.board = QTableWidget()
        self.board.setWindowTitle("game state")
        self.board.setFixedSize(QDesktopWidget().width()*.4, QDesktopWidget().width()*(2.4/7))
        self.board.setRowCount(self.num_rows)
        self.board.setColumnCount(self.num_cols)
        self.initialize_board()
        self.board.horizontalHeader().setDefaultSectionSize(self.board.width()*(1/7.001))
        self.board.verticalHeader().setDefaultSectionSize(self.board.height()*(1/6.001))
        self.board.horizontalHeader().hide()
        self.board.verticalHeader().hide()

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
        # self.header_layout.addWidget(self.main_menu_push_button)
        self.header_layout.addStretch(0)
        self.header_layout.addWidget(self.pvp_label)
        self.header_layout.addStretch(0)
        # self.header_layout.addWidget(self.close_save_push_button)

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
        self.main_layout.addWidget(self.board, alignment=Qt.AlignCenter)
        self.main_layout.addLayout(self.footer_layout)

    # # ------- actions --------- # #
        self.board.cellClicked.connect(self.column_clicked)


    def exit_app(self):
        exit()

    def initialize_board(self):
        for i in range(7):
            for j in range(6):
                cell = QLabel()
                cell.setPixmap(self.empty_cell)
                cell.setScaledContents(True)
                self.board.setCellWidget(j,i, cell)

    def column_clicked(self, row, col):
        if(self.move_number % 2 == 1 ):
            print(self.test.is_col_empty(col))
            row_index = self.test.make_move('red', col)
            if(row_index == -1):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('this column is full, please choose another')
                msg.setWindowTitle("full column")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
            else:
                cell = QLabel()
                cell.setPixmap(self.red_cell)
                cell.setScaledContents(True)
                self.board.setCellWidget(row_index,col,cell)
                self.move_number+=1
            self.test.print_board()

        else:
            row_index = self.test.make_move('black', col)
            if(row_index == -1):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('this column is full, please choose another')
                msg.setWindowTitle("full column")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
            else:
                cell = QLabel()
                cell.setPixmap(self.black_cell)
                cell.setScaledContents(True)
                self.board.setCellWidget(row_index,col,cell)
                self.move_number+=1
            self.test.print_board()

        print(self.test.check_win_rc())
