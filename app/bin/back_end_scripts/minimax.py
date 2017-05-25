#!/usr/bin/env python3
import numpy as np
import random as rand
import numpy as np

class minimax(object):
    def __init__(self, current_board, move_number):
        self.board = current_board
        self.move_number = move_number
        


    # def find_twos(self, row, col):
    #
    #
    # def find_threes(self, row, col):
    #
    # def get_fours(self, row, col):
    #
    #
    # def evaluate_board(self):
    #     (2 in a rows)*10 + (3 in a rows)*1000 + (4 in a row)*100000
    #




def main():
    print("\nminimax ai algorithm --- connect four\n")
    sample_board = np.zeros((6,7), dtype=np.int)
    minimax_ = minimax(sample_board, 1)

if(__name__=='__main__'):
    main()
