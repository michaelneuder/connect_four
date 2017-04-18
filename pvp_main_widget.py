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
        self.connection = sqlite3.connect('database/game_history.db')
        self.cursor = self.connection.cursor()

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
        self.file = "images/empty_cell.png"
        self.empty_cell = QPixmap(self.file)
        self.file_red = "images/red.png"
        self.red_cell = QPixmap(self.file_red)
        self.file_black = "images/black.png"
        self.black_cell = QPixmap(self.file_black)

        # player images
        self.p1_file = 'images/r_p1.png'
        self.p1_image = QPixmap(self.p1_file)
        self.p2_file = 'images/b_p2.png'
        self.p2_image = QPixmap(self.p2_file)
        self.g_file = 'images/g.png'
        self.g_image = QPixmap(self.g_file)


        # header widgets
        self.p1_label = QLabel()
        self.p1_label.setFixedSize(self.width() * .2, self.height() * .1)
        self.p1_label.setPixmap(self.p1_image)
        self.p1_label.setScaledContents(True)
        self.p2_label = QLabel()
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
        self.header_layout.addStretch(0)
        self.header_layout.addWidget(self.p1_label)
        self.header_layout.addWidget(self.pvp_label)
        self.header_layout.addWidget(self.p2_label)
        self.header_layout.addStretch(0)


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
                self.move_number_label.setText("move number: " + str(self.move_number -1))
                self.test.move_history.append(col)
            else:
                self.test.board[5,col] = 2
                cell = QLabel()
                cell.setPixmap(self.black_cell)
                cell.setScaledContents(True)
                self.board.setCellWidget(5,col,cell)
                self.move_number+=1
                self.move_number_label.setText("move number: " + str(self.move_number -1))
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
                self.move_number_label.setText("move number: " + str(self.move_number -1))
                self.test.move_history.append(col)
            else:
                self.test.board[row_landed,col] = 2
                cell = QLabel()
                cell.setPixmap(self.black_cell)
                cell.setScaledContents(True)
                self.board.setCellWidget(row_landed,col,cell)
                self.move_number+=1
                self.move_number_label.setText("move number: " + str(self.move_number -1))
                self.test.move_history.append(col)
        self.update_turn_graphic(self.move_number)
        if(self.test.check_win(row_landed, col)):
            if(self.move_number % 2 == 0):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('red wins!!')
                msg.setWindowTitle("winner")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('black wins!!')
                msg.setWindowTitle("winner")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()

    def reset_clicked(self):
        self.test.print_board()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('are you sure you want to reset?  this action cannot be undone')
        msg.setWindowTitle("confirm")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msg.exec_()
        if (retval == QMessageBox.Yes):
            self.initialize_board()
            self.test.__init__()
            self.move_number = 1
            self.move_number_label.setText("move number: " + str(self.move_number))
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
            self.move_number_label.setText("move number: " + str(self.move_number -1))

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
        print(self.test.move_history)
        self.connection.execute('INSERT INTO history values (?, ?)', (1, '290219021509125'))
        self.connection.commit()
        for row in self.connection.execute('SELECT * from history;'):
            print(row)
