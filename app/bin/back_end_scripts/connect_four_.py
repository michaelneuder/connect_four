#!/usr/bin/env python3
from minimax import minimax
from game_tree import game_tree
from copy import deepcopy

class connect_four(object):
    def __init__(self):
        self.number_cols = 7
        self.number_rows = 6
        # self.board = np.zeros((self.number_rows, self.number_cols), dtype=np.int)
        self.board = [[0 for col in range(self.number_cols)] for row in range(self.number_rows)]
        self.move_number = 1
        self.move_history = []

    def print_board(self):
        print("    "+"-"*17)
        for i in range(6):
            print("    | {} {} {} {} {} {} {} |".format(self.board[i][0],
            self.board[i][1], self.board[i][2], self.board[i][3], self.board[i][4],
            self.board[i][5], self.board[i][6]))
        print("    "+"-"*17)

    def make_move(self, col, color):
        row = self.find_row(col)
        if(row == -1):
            self.print_message("couldn't make move --- column full")
            return
        else:
            self.board[row][col] = color
            self.move_history.append([row, col])
            self.move_number += 1

    def find_row(self, col):
        for i in range(5,-1,-1):
            if(self.board[i][col] == 0):
                return i
        return -1

    def play_game(self):
        keep_going = True
        while(keep_going):
            self.print_board()
            column = input("enter column to move (q to quit; u to undo): ")
            if(column == 'q'):
                keep_going = False
            elif(column == 'u'):
                self.undo_move()
            elif(column != '1' and column != '2' and column != '3' and column != '4'
                  and column != '5' and column != '6' and column != '7'):
                self.print_message("please enter a valid column value 1-7")
            else:
                if(self.move_number % 2 == 1):
                    self.make_move(int(column)-1, 1)
                else:
                    self.make_move(int(column)-1, 2)

    def undo_move(self):
        if(self.move_history):
            last_move = self.move_history.pop()
            row, col = last_move[0], last_move[1]
            self.board[row][col] = 0
            self.move_number -= 1
        else:
            self.print_message("no more moves to undo")

    def print_message(self, message):
        print('-------------------------------')
        print(message)
        print('-------------------------------')

    def get_potential_moves(self):
        # dont forget to add column full check
        game_states = []
        for i in range(self.number_cols):
            self.make_move(i, 1)
            current_state = deepcopy(self.board)
            game_states.append(current_state)
            self.undo_move()
        return game_states


    def evaluate_board(self, board):
        evalution = 10
        return evalution


def main():
    cf = connect_four()
    # cf.play_game()
    # cf.find_best_move()

if __name__=='__main__':
    main()
