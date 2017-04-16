#!/usr/bin/env python3

## connect four using numpy because it is nice
import numpy as np

class cf(object):
    def __init__(self):
        self.board = np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
        self.move_number=1

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

    def check_win(self, row, col):
        pass

def main():
    cf1 = cf()
    cf1.print_board()
    keep_going = True # red moves first
    while (keep_going):
        column = input("enter the column of the move: (type q to quit) ")
        if (column == 'q'):
            keep_going = False
            quit()
        elif (column != '1' and column != '2' and column != '3' and column != '4'
              and column != '5' and column != '6' and column != '7'):
            print("please enter a valid column value 1-7")
        else:
            column_int = int(column)
            if(cf1.move_number%2 == 1): # even move number implies red's move
                cf1.make_move('red', column_int - 1)
                cf1.move_number += 1
            else:
                cf1.make_move('black', column_int - 1)
                cf1.move_number += 1
            if(cf1.check_win_rc() or cf1.check_win_diag()):
                quit()

if (__name__=='__main__'):
    main()
