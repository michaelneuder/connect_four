#!/usr/bin/env python3
# connect four

class connect_four(object):
    def __init__(self):
        self.size = 7
        self.board = [[0 for x in range(self.size)] for y in range(self.size)]
        self.move_number = 1
        # self.right_diagonal1 = [0 for x in range(4)] # diagonals that start at the right side and move left
        # self.right_diagonal2 = [0 for x in range(5)]
        # self.right_diagonal3 = [0 for x in range(6)]
        # self.right_diagonal4 = [0 for x in range(6)]
        # self.right_diagonal5 = [0 for x in range(5)]
        # self.right_diagonal6 = [0 for x in range(4)]
        # self.left_diagonal1 = [0 for x in range(4)]
        # self.left_diagonal2 = [0 for x in range(5)]
        # self.left_diagonal3 = [0 for x in range(6)]
        # self.left_diagonal4 = [0 for x in range(6)]
        # self.left_diagonal5 = [0 for x in range(5)]
        # self.left_diagonal6 = [0 for x in range(4)]

    def print_board(self):
        print("    "+"-"*17)
        for x in range(self.size):
            print("    | {} {} {} {} {} {} {} |".format(self.board[x][0], self.board[x][1],
            self.board[x][2], self.board[x][3], self.board[x][4], self.board[x][5],
            self.board[x][6]))
        print("    "+"-"*17)

    def make_move(self, color, column):
        print("a", color, "piece was placed in column", column)
        row = 0
        while(self.board[row][column] == 0 and row < 6):
            row+=1
        if (row == 0 and self.board[row][column] != 0): # condition for a full column
            print("this column is full, please choose another!")
        else: # not full column
            if (row == 6 and self.board[row][column] == 0): # case of the first piece in the column
                if(color == 'red'):
                    self.board[row][column] = 1
                elif(color == 'black'):
                    self.board[row][column] = 2
                else:
                    print("color error")
            else: # not the first piece of the column
                print("entered else")
                if(color == 'red'):
                    self.board[row-1][column] = 1
                elif(color == 'black'):
                    self.board[row-1][column] = 2
                else:
                    print("color error")
        print("this is the new board state")
        self.print_board()


    def check_win_diag(self):
        row = 3
        column = 0
        if(self.board[row][column] == self.board[row-1][column+1] == self.board[row-2][column+2]
        == self.board[row-3][column+3] != 0): # left diag 1
            print("we have a winner")
            return True
        #print("left diagonal 1 is", self.left_diagonal1[0], self.left_diagonal1[1], self.left_diagonal1[2])
        for i in range(2):
            print(i)
        row = 4
        column = 0
        # for i in range(5):
        #     self.left_diagonal2[i] = self.board[row][column]
        #     row -= 1
        #     column += 1
        # print("left diagonal 2 is", self.left_diagonal2[0], self.left_diagonal2[1], self.left_diagonal2[2])


    def check_win_rc(self):
        for row in range(self.size): # checking for win along each row
            for column in range(self.size - 3):
                if(self.board[row][column] == self.board[row][column+1] == self.board[row][column+2]
                == self.board[row][column+3] != 0):
                    if(self.board[row][column] == 1):
                        print("red wins! four are connected on row", row + 1)
                        return True
                    elif(self.board[row][column] == 2):
                        print("black wins! four are connected on row", row + 1)
                        return True
                    else:
                        print("error 1")
        for column in range(self.size): # checking for win along each column
            for row in range(self.size - 3):
                if(self.board[row][column] == self.board[row+1][column] == self.board[row+2][column]
                == self.board[row+3][column] != 0):
                    if(self.board[row][column] == 1):
                        print("red wins! four are connected on column", column + 1)
                        return True
                    elif(self.board[row][column] == 2):
                        print("black wins! four are connected on row", column + 1)
                        return True
                    else:
                        print("error 2")
        return False

def main():
    cf_board = connect_four()
    cf_board.print_board()
    keep_going = True # red moves first
    while (keep_going):
        column = input("enter the column of the move: (type q to quit) ")
        if (column == 'q'):
            cf_board.keep_going = False
            quit()
        elif (column != '1' and column != '2' and column != '3' and column != '4'
              and column != '5' and column != '6' and column != '7'):
            print("please enter a valid column value 1-7")
        else:
            column_int = int(column)
            if(cf_board.move_number%2 == 1): # even move number implies red's move
                cf_board.make_move('red', column_int - 1)
                cf_board.move_number += 1
            else:
                cf_board.make_move('black', column_int - 1)
                cf_board.move_number += 1
            if(cf_board.check_win_rc() or cf_board.check_win_diag()):
                quit()


if (__name__ == "__main__"):
    main()
