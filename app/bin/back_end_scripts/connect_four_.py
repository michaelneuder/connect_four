#!/usr/bin/env python3
import numpy as np
import random as rand
from minimax import minimax

class connect_four(object):
    def __init__(self):
        self.number_cols = 7
        self.number_rows = 6
        self.board = np.zeros((self.number_rows, self.number_cols), dtype=np.int)
        self.move_number = 1
        self.move_history = []

    def print_board(self):
        print(self.board)

    def make_move(self, col, color):
        row = self.find_row(col)
        if(row == -1):
            print("couldn't make move --- column full")
            return
        print(row, col)
        self.board[row, col] = color

    def find_row(self, col):
        for i in range(5,-1,-1):
            if(self.board[i, col] == 0):
                return i
        return -1

def main():
    cf = connect_four()
    cf.make_move(1,1)
    cf.make_move(1,1)
    cf.make_move(1,1)
    cf.make_move(1,1)
    cf.make_move(1,1)
    cf.make_move(1,1)
    cf.make_move(1,1)
    print(cf.find_row(1))
    cf.print_board()


if __name__=='__main__':
    main()
