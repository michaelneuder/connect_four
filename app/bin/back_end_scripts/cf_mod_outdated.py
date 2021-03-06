#!/usr/bin/env python3


#### old file, but really cool idea. i liked the use of dictionary 

# class file used to keep track of connect four board and check for wins
import numpy as np

class cf(object):
    def __init__(self):
        self.board = np.array([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],[0,0,0,0,0,0,0]])
        self.move_number=1
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
        self.diag_dict = {}
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

        self.update_dict()

    def update_dict(self):
        self.diag_dict = {
        # row 1
        (0,0) : [self.left_diag_4] ,
        (0,1) : [self.left_diag_3] ,
        (0,2) : [self.left_diag_2] ,
        (0,3) : [self.left_diag_1, self.right_diag_1] ,
        (0,4) : [self.right_diag_2] ,
        (0,5) : [self.right_diag_3] ,
        (0,6) : [self.right_diag_4] ,

        # row 2
        (1,0) : [self.left_diag_5] ,
        (1,1) : [self.left_diag_4] ,
        (1,2) : [self.left_diag_3, self.right_diag_1] ,
        (1,3) : [self.left_diag_2, self.right_diag_2] ,
        (1,4) : [self.left_diag_1, self.right_diag_3] ,
        (1,5) : [self.right_diag_4] ,
        (1,6) : [self.right_diag_5] ,

        # row 3
        (2,0) : [self.left_diag_6] ,
        (2,1) : [self.left_diag_5, self.right_diag_1] ,
        (2,2) : [self.left_diag_4, self.right_diag_2] ,
        (2,3) : [self.left_diag_3, self.right_diag_3] ,
        (2,4) : [self.left_diag_2, self.right_diag_4] ,
        (2,5) : [self.left_diag_1, self.right_diag_5] ,
        (2,6) : [self.right_diag_6] ,

        # row 4
        (3,0) : [self.right_diag_1] ,
        (3,1) : [self.right_diag_2, self.left_diag_6] ,
        (3,2) : [self.right_diag_3, self.left_diag_5] ,
        (3,3) : [self.right_diag_4, self.left_diag_4] ,
        (3,4) : [self.right_diag_5, self.left_diag_3] ,
        (3,5) : [self.right_diag_6, self.left_diag_2] ,
        (3,6) : [self.left_diag_1] ,

        # row 5
        (4,0) : [self.right_diag_2] ,
        (4,1) : [self.right_diag_3] ,
        (4,2) : [self.right_diag_4, self.left_diag_6] ,
        (4,3) : [self.right_diag_5, self.left_diag_5] ,
        (4,4) : [self.right_diag_6, self.left_diag_4] ,
        (4,5) : [self.left_diag_3] ,
        (4,6) : [self.left_diag_2] ,

        # row 6
        (5,0) : [self.right_diag_3] ,
        (5,1) : [self.right_diag_4] ,
        (5,2) : [self.right_diag_5] ,
        (5,3) : [self.right_diag_6, self.left_diag_6] ,
        (5,4) : [self.left_diag_5] ,
        (5,5) : [self.left_diag_4] ,
        (5,6) : [self.left_diag_3] ,
        }

    def check_win(self, row, col):
        self.update_diags()

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

        # check diagonally
        for diagonal in self.diag_dict[(row,col)]:
            # print(diagonal)
            for i in range(len(diagonal) - 3):
                if(diagonal[i] == diagonal [i+1] == diagonal [i+2] == diagonal [i+3] != 0):
                    if(self.board[row,col] == 1):
                        print('red win')
                        return True
                        exit()
                    else:
                        print('black win')
                        return True
        return self.win_found

    def get_last_move(self):
        col = self.move_history.pop()
        row = self.find_row(col) + 1
        self.board[row, col] = 0
        removed_cell = [row, col]
        return removed_cell

    def check_win_new(self, row, col, color_id):
        # negative slope diagonal first
        current_max = 1

        # iterate to the bottom right of the diagonal
        temp_row = row + 1
        temp_col = col + 1
        while(temp_row < 6 and temp_col < 7 and self.board[temp_row, temp_col] == color_id):
            print('here')
            current_max+=1
            print(current_max)
            temp_row+=1
            temp_col+=1
            if(current_max >= 4):
                print("win!")

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
                print("win!!")

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
                print('win!!!')

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
                print('win!!!!')
