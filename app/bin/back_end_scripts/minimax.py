#!/usr/bin/env python3
import numpy as np
import random as rand

class minimax(object):
    def __init__(self, current_board, move_number):
        self.board = current_board
        self.number_rows = 6
        self.number_cols = 7
        self.move_number = move_number
        self.right_diag_1 = []
        self.right_diag_2 = []
        self.right_diag_3 = []
        self.right_diag_4 = []
        self.right_diag_5 = []
        self.right_diag_6 = []
        self.left_diag_1 = []
        self.left_diag_2 = []
        self.left_diag_3 = []
        self.left_diag_4 = []
        self.left_diag_5 = []
        self.left_diag_6 = []
        self.diag_set = []
        self.update_diags()

    def update_diags(self):
        self.right_diag_1 = [self.board[3,0],self.board[2,1],self.board[1,2],self.board[0,3]]
        self.right_diag_2 = [self.board[4,0],self.board[3,1],self.board[2,2],self.board[1,3],
        self.board[0,4]]
        self.right_diag_3 = [self.board[5,0],self.board[4,1],self.board[3,2],self.board[2,3],
        self.board[1,4],self.board[0,5]]
        self.right_diag_4 = [self.board[5,1],self.board[4,2],self.board[3,3],self.board[2,4],
        self.board[1,5],self.board[0,6]]
        self.right_diag_5 = [self.board[5,2],self.board[4,3],self.board[3,4],self.board[2,5],
        self.board[1,6]]
        self.right_diag_6 = [self.board[5,3],self.board[4,4],self.board[3,5],self.board[2,6]]

        self.left_diag_1 = [self.board[3,6],self.board[2,5],self.board[1,4],self.board[0,3]]
        self.left_diag_2 = [self.board[4,6],self.board[3,5],self.board[2,4],self.board[1,3],
        self.board[0,2]]
        self.left_diag_3 = [self.board[5,6],self.board[4,5],self.board[3,4],self.board[2,3],
        self.board[1,2],self.board[0,1]]
        self.left_diag_4 = [self.board[5,5],self.board[4,4],self.board[3,3],self.board[2,2],
        self.board[1,1],self.board[0,0]]
        self.left_diag_5 = [self.board[5,4],self.board[4,3],self.board[3,2],self.board[2,1],
        self.board[1,0]]
        self.left_diag_6 = [self.board[5,3],self.board[4,2],self.board[3,1],self.board[2,0]]

        self.diag_set = [self.right_diag_1, self.right_diag_2, self.right_diag_3,
                         self.right_diag_4, self.right_diag_5, self.right_diag_6,
                         self.left_diag_1, self.left_diag_2, self.left_diag_3,
                         self.left_diag_4, self.left_diag_5, self.left_diag_6]

    def find_twos_rows(self, color):
        number_of_twos = 0
        '''
        checking for twos along the rows. this gets complicated, because we
        only want to count twos that could be part of a future connect four.
        thus we have to make sure that their is enough empty space around each
        set of two before we count it.
        '''
        for row in range(self.number_rows):
            for col in range(self.number_cols):
                if(col == 0):
                    if(self.board[row][col] == self.board[row][col+1] == color):
                        if(self.board[row][col+2] == self.board[row][col+3] == 0):
                            number_of_twos += 1
                            print(row,col)
                elif(col == 1):
                    if(self.board[row][col] == self.board[row][col+1] == color):
                        if(self.board[row][col-1] == self.board[row][col+2] == 0):
                            number_of_twos += 1
                            print(row,col)
                        elif(self.board[row][col+2] == self.board[row][col+3] == 0):
                            number_of_twos += 1
                            print(row,col)
                elif(col == 2 or col == 3):
                    if(self.board[row][col] == self.board[row][col+1] == color):
                        if(self.board[row][col-1] == self.board[row][col+2] == 0):
                            number_of_twos += 1
                            print(row,col)
                        elif(self.board[row][col+2] == self.board[row][col+3] == 0):
                            number_of_twos += 1
                            print(row,col)
                        elif(self.board[row][col-1] == self.board[row][col-2] == 0):
                            number_of_twos += 1
                            print(row,col)
                elif(col == 4):
                    if(self.board[row][col] == self.board[row][col+1] == color):
                        if(self.board[row][col-1] == self.board[row][col+2] == 0):
                            number_of_twos += 1
                            print(row,col)
                        elif(self.board[row][col-1] == self.board[row][col-2] == 0):
                            number_of_twos += 1
                            print(row,col)
                elif(col == 5):
                    if(self.board[row][col] == self.board[row][col+1] == color):
                        if(self.board[row][col-1] == self.board[row][col-2] == 0):
                            number_of_twos += 1
                            print(row,col)
        return number_of_twos

    def find_twos_rows_test(self, color):
        number_of_twos = 0
        '''
        checking for twos along the rows. this gets complicated, because we
        only want to count twos that could be part of a future connect four.
        thus we have to make sure that their is enough empty space around each
        set of two before we count it.
        '''
        for row in range(self.number_rows):
            for col in range(self.number_cols):
                if( (col+3) < self.number_cols):
                    if(self.board[row][col] == self.board[row][col+1] == color
                        and self.board[row][col+2] == self.board[row][col+3] == 0):
                        number_of_twos += 1
                        print(row, col)
        return number_of_twos


    def find_twos_cols(self, color):
        number_of_twos = 0
        '''
        checking for twos along the col. this is pretty easy as the only way a
        two in a row along a column can be apart of a connect four is if the piece
        immediately above the two is empty.
        '''
        for col in range(self.number_cols):
            for row in range(self.number_rows):
                if(self.board[row][col] == self.board[row-1][col] == color):
                    if(self.board[row-2][col] == 0):
                        number_of_twos += 1
                        print(row,col)

    def find_twos_diag(self, color):
        for diag in self.diag_set:
            diagonal_length = len(diag)
            for i in range(diagonal_length-1):
                if( (i+3) < diagonal_length):
                    if(diag[i] == diag[i+1] == color and diag[i+2] == diag[i+3] == 0):
                        number_of_twos += 1
                        print('found')
                elif( (i-1) > -1 and (i+1) < diagonal_length):
                    if(diag[i] == diag[i+1] == color and diag[i-1] == diag[i+1] == 0):
                        number_of_twos += 1
                        print('found')
                elif( (i-2) > -1):
                    if(diag[i] == diag[i+1] == color and diag[i-1] == diag[i-2] == 0):
                        number_of_twos += 1
                        print('found')




    # def evaluate_board(self):
    #     (2 in a rows)*10 + (3 in a rows)*1000 + (4 in a row)*100000





def main():
    print("\nminimax ai algorithm --- connect four\n")
    sample_board = np.array([[0,0,0,0,0,0,0],
                             [0,0,0,1,1,0,0],
                             [0,0,0,0,0,0,0],
                             [0,0,2,0,1,2,0],
                             [0,1,2,1,2,2,2],
                             [2,1,1,2,1,1,1]])
    minimax_ = minimax(sample_board, 16)
    minimax_.find_twos_rows_test(1)


if __name__=='__main__':
    main()
