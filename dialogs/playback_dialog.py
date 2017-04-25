from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from back_end_scripts.cf_mod import cf
from dialogs.win_dialog import win_dialog
import sqlite3


class playback_dialog(QDialog):
    def __init__(self, moves):
        QDialog.__init__(self)
        self.main_layout = QVBoxLayout(self)
        self.num_rows = 6
        self.num_cols = 7
        self.moves_string = moves
        self.move_number = 0
        self.test = cf()
        self.win_found_bool = False

        # properties of the dialog
        self.setWindowTitle("playback")

        # main title
        self.title_label = QLabel("game moves")
        self.title_font = QFont("Helvetica",40)
        self.title_label.setFont(self.title_font)

        # cell images
        self.file = "images/empty_cell.png"
        self.empty_cell = QPixmap(self.file)
        self.file_red = "images/red.png"
        self.red_cell = QPixmap(self.file_red)
        self.file_black = "images/black.png"
        self.black_cell = QPixmap(self.file_black)
        self.file_win = "images/purple_cell.png"
        self.win_cell = QPixmap(self.file_win)

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

        # widgets for footer_layout
        self.close_push_button = QPushButton("close")
        self.forward_push_button = QPushButton(">>>")
        self.backward_push_button = QPushButton("<<<")


        # layout declaration
        self.footer_layout = QHBoxLayout()

        # layouts adding
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.board)
        self.footer_layout.addStretch(0)
        self.footer_layout.addWidget(self.backward_push_button)
        self.footer_layout.addWidget(self.forward_push_button)
        self.footer_layout.addWidget(self.close_push_button)
        self.footer_layout.addStretch(0)
        self.main_layout.addLayout(self.footer_layout)

        # actions
        self.close_push_button.clicked.connect(self.close_clicked)
        self.forward_push_button.clicked.connect(self.move_forward)
        self.backward_push_button.clicked.connect(self.move_back)


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
                if(self.move_number % 2 == 0):
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
                if(self.move_number % 2 == 0):
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
            if(self.move_number % 2 == 1):
                if(self.test.check_win_new(row_landed, col, 1)):
                    self.win_found_bool = True
                    self.win_found(self.test.win_results)
                    dialog = win_dialog('red')
                    dialog.exec_()
            elif(self.move_number % 2 == 0):
                if(self.test.check_win_new(row_landed, col, 2)):
                    self.win_found_bool = True
                    self.win_found(self.test.win_results)
                    dialog = win_dialog('black')
                    dialog.exec_()

    def move_forward(self):
        if(self.move_number < len(self.moves_string)):
            self.column_clicked(0, int(self.moves_string[self.move_number]))
            self.test.print_board()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText('this is the end of the game!')
            msg.setWindowTitle("unable to continue")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def move_back(self):
        if(self.move_number == 0):
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

    def win_found(self, win_list):
        for win in win_list:
            for cell in win:
                i = cell[0]
                j = cell[1]
                cell = QLabel()
                cell.setPixmap(self.win_cell)
                cell.setScaledContents(True)
                self.board.setCellWidget(i,j, cell)

    def close_clicked(self):
        self.close()
