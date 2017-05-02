#!/usr/bin/env python3
import numpy as np
import random as rand

# minimax attempt
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
        return row

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
                    self.win_results.append([[row,col],[row+1,col],[row+2,col],[row+3,col]])
                    self.win_found = True
                else:
                    self.win_results.append([[row,col],[row+1,col],[row+2,col],[row+3,col]])
                    self.win_found = True

        # check row
        for i in range(4):
            if(self.board[row,i] == self.board[row,i+1] ==self.board[row,i+2]
            == self.board[row,i+3] != 0):
                if(self.board[row,i] == 1):
                    self.win_results.append([[row,i],[row,i+1],[row,i+2],[row,i+3]])
                    self.win_found = True
                else:
                    self.win_found =  True
                    self.win_results.append([[row,i],[row,i+1],[row,i+2],[row,i+3]])

        # diagonals
        # negative slope diagonal first
        current_max = 1
        potential_win = [[row,col]]

        # iterate to the bottom right of the diagonal
        temp_row = row + 1
        temp_col = col + 1
        while(temp_row < 6 and temp_col < 7 and self.board[temp_row, temp_col] == color_id):
            current_max+=1
            potential_win.append([temp_row, temp_col])
            temp_row+=1
            temp_col+=1
            if(current_max >= 4):
                # print("win1")
                self.win_found = True
                self.win_results.append(potential_win)

        # iterate to the top left of the diagonal
        temp_row = row - 1
        temp_col = col - 1
        while(temp_row >= 0 and temp_col >= 0 and self.board[temp_row, temp_col] == color_id):
            current_max+=1
            potential_win.append([temp_row, temp_col])
            temp_row-=1
            temp_col-=1
            if(current_max >= 4):
                # print("win2")
                self.win_found = True
                self.win_results.append(potential_win)

        # positive slope diagonals
        current_max = 1
        potential_win = [[row,col]]

        # iterate to the top right of the diagonal
        temp_row = row - 1
        temp_col = col + 1
        while(temp_row >= 0 and temp_col < 7 and self.board[temp_row, temp_col] == color_id):
            current_max+=1
            potential_win.append([temp_row, temp_col])
            temp_row-=1
            temp_col+=1
            if(current_max >= 4):
                # print('win3')
                self.win_found = True
                self.win_results.append(potential_win)

        # iterate to the bottom left of the diagonal
        temp_row = row + 1
        temp_col = col - 1
        while(temp_row < 6 and temp_col >= 0 and self.board[temp_row, temp_col] == color_id):
            current_max+=1
            potential_win.append([temp_row, temp_col])
            temp_row+=1
            temp_col-=1
            if(current_max >= 4):
                # print('win4')
                self.win_found = True
                self.win_results.append(potential_win)

        return self.win_found


    # def find_twos(self, row, col):
    #
    #
    # def find_threes(self, row, col):
    #
    # def get_fours(self, row, col):


    # def evaluate_board(self):
        # (2 in a rows)*10 + (3 in a rows)*1000 + (4 in a row)*100000

    # def minimax(self):
    #



def main():
    cf1 = cf()
    keep_going = True
    while (keep_going):
        # user plays red
        if(cf1.move_number % 2 == 1):
            cf1.print_board()
            column = input("enter the column of the move: (type q to quit) ")
            if (column == 'q'):
                keep_going = False
                quit()
            elif (column != '1' and column != '2' and column != '3' and column != '4'
                  and column != '5' and column != '6' and column != '7'):
                print("please enter a valid column value 1-7")
            else:
                # move will be made
                column_int = int(column) - 1
                row = cf1.find_row(column_int)

                if(cf1.is_col_empty(column_int)):
                    cf1.board[row, column_int] = 1
                    cf1.move_number += 1
                    if(cf1.check_win_new(row, column_int, 1)):
                        print('win')
                        print(cf1.win_results)
                        # exit()
                elif(cf1.is_col_full(column_int)):
                    print('column full')
                    pass
                else:
                    # not empty or full
                    cf1.board[row-1, column_int] = 1
                    cf1.move_number += 1
                    if(cf1.check_win_new(row-1, column_int, 1)):
                        print('win')
                        print(cf1.win_results)
                        # exit()
        # ai plays black
        # else:
        #     ai_col = rand.randint(0,6)
        #     ai_row = cf1.find_row(ai_col)
        #     if(cf1.is_col_empty(ai_col)):
        #         cf1.board[ai_row, ai_col] = 2
        #         cf1.move_number += 1
        #         if(cf1.check_win_new(ai_row, ai_col, 2)):
        #             print('win')
        #             cf1.print_board()
        #             print(cf1.win_results)
        #             # exit()
        #     elif(cf1.is_col_full(ai_col)):
        #         print('column full')
        #         pass
        #     else:
        #         # col not full or empty
        #         cf1.board[ai_row-1, ai_col] = 2
        #         cf1.move_number += 1
        #         if(cf1.check_win_new(ai_row-1, ai_col, 2)):
        #             print('win')
        #             cf1.print_board()
        #             print(cf1.win_results)
        #             # exit()
        else:
            cf1.print_board()
            column = input("enter the column of the move: (type q to quit) ")
            if (column == 'q'):
                keep_going = False
                quit()
            elif (column != '1' and column != '2' and column != '3' and column != '4'
                  and column != '5' and column != '6' and column != '7'):
                print("please enter a valid column value 1-7")
            else:
                # move will be made
                column_int = int(column) - 1
                row = cf1.find_row(column_int)

                if(cf1.is_col_empty(column_int)):
                    cf1.board[row, column_int] = 2
                    cf1.move_number += 1
                    if(cf1.check_win_new(row, column_int, 2)):
                        print('win')
                        print(cf1.win_results)
                        # exit()
                elif(cf1.is_col_full(column_int)):
                    print('column full')
                    pass
                else:
                    # not empty or full
                    cf1.board[row-1, column_int] = 2
                    cf1.move_number += 1
                    if(cf1.check_win_new(row-1, column_int, 2)):
                        print('win')
                        print(cf1.win_results)
                        # exit()

if(__name__=='__main__'):
    main()