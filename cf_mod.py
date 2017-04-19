#!/usr/bin/env python3

# class file used to keep track of connect four board and check for wins
import numpy as np

class cf(object):
    def __init__(self):
        self.board = np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
        self.move_number=1
        self.move_history = []
        self.win_results = []
        self.win_found = False

    def print_board(self):
        print("    "+"-"*17)
        for i in range(6):
            print("    | {} {} {} {} {} {} {} |".format(self.board[i,0],
            self.board[i,1], self.board[i,2], self.board[i,3], self.board[i,4],
            self.board[i,5], self.board[i,6]))
        print("    "+"-"*17)

    def is_col_empty(self, col):
        if (self.board[5, col] == 0):
            return True
        return False

    def is_col_full(self, col):
        if(self.board[0, col] != 0):
            return True
        return False

    def find_row(self, col):
        row = 0
        while(self.board[row, col] == 0 and row < 5):
            row+=1
        return row-1

    def get_last_move(self):
        col = self.move_history.pop()
        row = self.find_row(col) + 1
        self.board[row, col] = 0
        removed_cell = [row, col]
        return removed_cell

    def check_win_new(self, row, col, color_id):
        # check column
        if(row > 2):
            pass
        else:
            if(self.board[row,col] == self.board[row+1,col] ==
            self.board[row+2,col] == self.board[row+3,col]):
                if(self.board[row,col] == 1):
                    print('red win')
                    self.win_results.append([[row,col],[row+1,col],[row+2,col],[row+3,col]])
                    self.win_found = True
                else:
                    print("black win")
                    self.win_results.append([[row,col],[row+1,col],[row+2,col],[row+3,col]])
                    self.win_found = True

        # check row
        for i in range(4):
            if(self.board[row,i] == self.board[row,i+1] ==self.board[row,i+2]
            == self.board[row,i+3] != 0):
                if(self.board[row,i] == 1):
                    print('red win')
                    self.win_results.append([[row,i],[row,i+1],[row,i+2],[row,i+3]])
                    self.win_found = True
                else:
                    print('black win')
                    self.win_found =  True
                    self.win_results.append([[row,i],[row,i+1],[row,i+2],[row,i+3]])

        # diagonals
        # negative slope diagonal first
        current_max = 1
        potential_win = []

        # iterate to the bottom right of the diagonal
        temp_row = row + 1
        temp_col = col + 1
        while(temp_row < 6 and temp_col < 7 and self.board[temp_row, temp_col] == color_id):
            print('here')
            current_max+=1
            print(current_max)
            temp_row+=1
            temp_col+=1
            # potential_win.append([])
            if(current_max >= 4):
                print("win1")
                self.win_found = True

        # iterate to the top left of the diagonal
        temp_row = row - 1
        temp_col = col - 1
        while(temp_row >= 0 and temp_col >= 0 and self.board[temp_row, temp_col] == color_id):
            print('here2')
            current_max+=1
            print(current_max)
            temp_row-=1
            temp_col-=1

            if(current_max >= 4):
                print("win2")

        # positive slope diagonals
        current_max = 1

        # iterate to the top right of the diagonal
        temp_row = row - 1
        temp_col = col + 1
        while(temp_row >= 0 and temp_col < 7 and self.board[temp_row, temp_col] == color_id):
            print('here3')
            current_max+=1
            print(current_max)
            temp_row-=1
            temp_col+=1
            if(current_max >= 4):
                print('win3')

        # iterate to the bottom left of the diagonal
        temp_row = row + 1
        temp_col = col - 1
        while(temp_row < 6 and temp_col >= 0 and self.board[temp_row, temp_col] == color_id):
            print('here4')
            current_max+=1
            print(current_max)
            temp_row+=1
            temp_col-=1
            if(current_max >= 4):
                print('win4')
