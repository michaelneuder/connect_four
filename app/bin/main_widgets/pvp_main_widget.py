#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from back_end_scripts.cf_mod import cf
from dialogs.win_dialog import win_dialog
from dialogs.save_dialog import save_dialog
import sqlite3

class pvp_main_widget(QWidget):
    save_clicked_signal = pyqtSignal()
    def __init__(self):
        QWidget.__init__(self)
        self.main_layout = QVBoxLayout(self)
        self.connection = sqlite3.connect('../database/game_history.db')
        self.cursor = self.connection.cursor()
        self.win_found_bool = False
        self.move_made = False

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

        # line spacer
        self.line = QFrame()
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        # cell images
        self.file = "../images/empty_cell.png"
        self.empty_cell = QPixmap(self.file)
        self.file_red = "../images/red.png"
        self.red_cell = QPixmap(self.file_red)
        self.file_black = "../images/black.png"
        self.black_cell = QPixmap(self.file_black)
        self.file_win = "../images/purple_cell.png"
        self.win_cell = QPixmap(self.file_win)

        # player images
        self.p1_file = '../images/r_p1.png'
        self.p1_image = QPixmap(self.p1_file)
        self.p2_file = '../images/b_p2.png'
        self.p2_image = QPixmap(self.p2_file)
        self.g_file = '../images/g.png'
        self.g_image = QPixmap(self.g_file)

        # header widgets
        self.p1_label = QLabel()
        self.p1_label.setFrameStyle(QFrame.Panel)
        self.p1_label.setLineWidth(2)
        self.p1_label.setStyleSheet("QLabel { background-color : rgb(184,184,186) ;border: solid; border-radius: 10px; border-color: black; border-width: 2px }")
        self.p1_label.setFixedSize(self.width() * .2, self.height() * .1)
        self.p1_label.setPixmap(self.p1_image)
        self.p1_label.setScaledContents(True)
        self.p2_label = QLabel()
        self.p2_label.setStyleSheet("QLabel { background-color : rgb(184,184,186) ;border: solid; border-radius: 10px; border-color: black; border-width: 2px}")
        self.p2_label.setFrameStyle(QFrame.Panel)
        self.p2_label.setLineWidth(2)
        self.p2_label.setFixedSize(self.width() * .2, self.height() * .1)
        self.p2_label.setPixmap(self.p2_image)
        self.p2_label.setScaledContents(True)
        self.pvp_label = QLabel(" vs ")
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
        self.move_number_label = QLabel("move #   ")
        self.move_number_label.setFixedWidth(100)
        self.undo_button = QPushButton("undo")
        self.reset_push_button = QPushButton("reset")
        self.save_push_button = QPushButton("save")

    # # -------- layout declaration -------- # #
        self.header_layout = QHBoxLayout()
        self.footer_layout = QHBoxLayout()
        self.side_bar_layout = QVBoxLayout()
        self.mid_layout = QHBoxLayout()

    # # -------- adding widgets to layouts -------- # #
        # header layout
        self.header_layout.addStretch(0)
        self.header_layout.addWidget(self.p1_label)
        self.header_layout.addWidget(self.pvp_label)
        self.header_layout.addWidget(self.p2_label)
        self.header_layout.addStretch(0)
        self.side_bar_layout.addStretch(0)
        self.side_bar_layout.addWidget(self.undo_button)
        self.side_bar_layout.addWidget(self.reset_push_button)
        self.side_bar_layout.addWidget(self.save_push_button)
        self.side_bar_layout.addWidget(self.move_number_label)
        self.side_bar_layout.addStretch(0)
        self.mid_layout.addWidget(self.board)

    # # -------- adding widgets and layouts to main layout -------- # #
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addSpacing(1)
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addSpacing(30)
        self.main_layout.addLayout(self.mid_layout)
        self.main_layout.addSpacing(15)
        self.main_layout.addWidget(self.line)
        self.main_layout.addSpacing(1)
        self.main_layout.addLayout(self.footer_layout)

    # # ------- actions --------- # #
        self.board.cellClicked.connect(self.column_clicked)
        self.reset_push_button.clicked.connect(self.reset_clicked)
        self.undo_button.clicked.connect(self.undo_clicked)
        self.save_push_button.clicked.connect(self.save_clicked)

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
        if(not self.win_found_bool):
            if(self.test.is_col_full(col)):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('this column is full, please choose another')
                msg.setWindowTitle("full column")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
                return
            elif(self.test.is_col_empty(col)):
                row_landed = 5
                if(self.move_number % 2 == 1):
                    self.test.board[5,col] = 1
                    cell = QLabel()
                    cell.setPixmap(self.red_cell)
                    cell.setScaledContents(True)
                    self.board.setCellWidget(5,col,cell)
                    self.move_number+=1
                    self.test.move_history.append(col)
                else:
                    self.test.board[5,col] = 2
                    cell = QLabel()
                    cell.setPixmap(self.black_cell)
                    cell.setScaledContents(True)
                    self.board.setCellWidget(5,col,cell)
                    self.move_number+=1
                    self.test.move_history.append(col)
            else:
                row_landed = self.test.find_row(col)
                if(self.move_number % 2 == 1):
                    self.test.board[row_landed,col] = 1
                    cell = QLabel()
                    cell.setPixmap(self.red_cell)
                    cell.setScaledContents(True)
                    self.board.setCellWidget(row_landed,col,cell)
                    self.move_number+=1
                    self.test.move_history.append(col)
                else:
                    self.test.board[row_landed,col] = 2
                    cell = QLabel()
                    cell.setPixmap(self.black_cell)
                    cell.setScaledContents(True)
                    self.board.setCellWidget(row_landed,col,cell)
                    self.move_number+=1
                    self.test.move_history.append(col)
            self.update_turn_graphic(self.move_number)
            if(self.move_number % 2 == 0):
                if(self.test.check_win_new(row_landed, col, 1)):
                    self.win_found_bool = True
                    self.win_found(self.test.win_results)
                    dialog = win_dialog('red')
                    dialog.exec_()
            elif(self.move_number % 2 == 1):
                if(self.test.check_win_new(row_landed, col, 2)):
                    self.win_found_bool = True
                    self.win_found(self.test.win_results)
                    dialog = win_dialog('black')
                    dialog.exec_()
        if(self.move_number == 43):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('you have reached a stalemate!')
            msg.setWindowTitle("stalemate")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def reset_clicked(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('are you sure you want to reset?  this action cannot be undone')
        msg.setWindowTitle("confirm")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()
        if (retval == QMessageBox.Yes):
            self.win_found_bool = False
            self.initialize_board()
            self.test.__init__()
            self.move_number = 1
            self.move_number_label.setText("move: " + str(self.move_number))
            self.p2_label.setPixmap(self.g_image)
            self.p2_label.setScaledContents(True)
            self.p1_label.setPixmap(self.p1_image)
            self.p1_label.setScaledContents(True)

    def undo_clicked(self):
        if(self.move_number == 1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('there are no more moves to be taken back!!')
            msg.setWindowTitle("error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            coordinates = self.test.get_last_move()
            cell = QLabel()
            cell.setPixmap(self.empty_cell)
            cell.setScaledContents(True)
            i = coordinates[0]
            j = coordinates[1]
            self.board.setCellWidget(i,j, cell)
            self.move_number-=1
            self.update_turn_graphic(self.move_number)
            self.move_number_label.setText("move: " + str(self.move_number -1))
            self.win_found_bool = False
            self.clear_win()
            self.test.win_found = False
            self.test.win_results = []

    def clear_win(self):
        for i in range(7):
            for j in range(6):
                if(self.test.board[j,i] == 1):
                    cell = QLabel()
                    cell.setPixmap(self.red_cell)
                    cell.setScaledContents(True)
                    self.board.setCellWidget(j,i, cell)
                elif(self.test.board[j,i] == 2):
                    cell = QLabel()
                    cell.setPixmap(self.black_cell)
                    cell.setScaledContents(True)
                    self.board.setCellWidget(j,i, cell)

    def update_turn_graphic(self, move):
        if(move % 2 == 0):
            self.p1_label.setPixmap(self.g_image)
            self.p1_label.setScaledContents(True)
            self.p2_label.setPixmap(self.p2_image)
            self.p2_label.setScaledContents(True)
        else:
            self.p2_label.setPixmap(self.g_image)
            self.p2_label.setScaledContents(True)
            self.p1_label.setPixmap(self.p1_image)
            self.p1_label.setScaledContents(True)

    def save_clicked(self):
        self.dialog = save_dialog(self.test.move_history)
        self.dialog.exec_()
        self.save_clicked_signal.emit()

    def win_found(self, win_list):
        for win in win_list:
            for cell in win:
                i = cell[0]
                j = cell[1]
                cell = QLabel()
                cell.setPixmap(self.win_cell)
                cell.setScaledContents(True)
                self.board.setCellWidget(i,j, cell)
