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

    def make_move(self, color, column):
        # print("a", color, "piece is being placed in column", column)
        row = 0
        while(self.board[row, column] == 0 and row < 5):
            row+=1
        if (row == 0 and self.board[row,column] != 0): # condition for a full column
            print("this column is full, please choose another!")
        else: # not full column
            if (row == 5 and self.board[row, column] == 0): # case of the first piece in the column
                if(color == 'red'):
                    self.board[row,column] = 1
                elif(color == 'black'):
                    self.board[row,column] = 2
                else:
                    print("color error")
            else: # not the first piece of the column
                if(color == 'red'):
                    self.board[row-1,column] = 1
                elif(color == 'black'):
                    self.board[row-1,column] = 2
                else:
                    print("color error")
        return row

    def check_win_rc(self):
        for row in range(6): # checking for win along each row
            for column in range(4):
                if(self.board[row,column] == self.board[row,column+1] == self.board[row,column+2]
                == self.board[row,column+3] != 0):
                    if(self.board[row,column] == 1):
                        print("red wins! four are connected on row", row + 1)
                        return True
                    elif(self.board[row,column] == 2):
                        print("black wins! four are connected on row", row + 1)
                        return True
                    else:
                        print("error 1")
        for column in range(7): # checking for win along each column
            for row in range(3):
                if(self.board[row,column] == self.board[row+1,column] == self.board[row+2,column]
                == self.board[row+3,column] != 0):
                    if(self.board[row,column] == 1):
                        print("red wins! four are connected on column", column + 1)
                        return True
                    elif(self.board[row,column] == 2):
                        print("black wins! four are connected on row", column + 1)
                        return True
                    else:
                        print("error 2")
        return False

    def check_win_diag(self): # this is hard to loop bc starting indicies bounce around so much
        #left diagonals
        row = 3
        column = 0
        for i in range(1): # left diag 1
            if(self.board[row-i,column+i] == self.board[row-1-i,column+1+i] == self.board[row-2-i,column+2+i]
            == self.board[row-3-i,column+3+i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the left diagonal 1")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the left diagonal 1")
                    return True
                else:
                    print("error 3")
        row = 4
        column = 0
        for i in range(2): #left diag 2
            if(self.board[row-i,column+i] == self.board[row-1-i,column+1+i] == self.board[row-2-i,column+2+i]
            == self.board[row-3-i,column+3+i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the left diagonal 2")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the left diagonal 2")
                    return True
                else:
                    print("error 4")
        row = 5
        column = 0
        for i in range(3): #left diag 3
            if(self.board[row-i,column+i] == self.board[row-1-i,column+1+i] == self.board[row-2-i,column+2+i]
            == self.board[row-3-i,column+3+i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the left diagonal 3")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the left diagonal 3")
                    return True
                else:
                    print("error 5")
        row = 5
        column = 1
        for i in range(3): #left diag 4
            if(self.board[row-i,column+i] == self.board[row-1-i,column+1+i] == self.board[row-2-i,column+2+i]
            == self.board[row-3-i,column+3+i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the left diagonal 4")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the left diagonal 4")
                    return True
                else:
                    print("error 6")
        row = 5
        column = 2
        for i in range(2): #left diag 5
            if(self.board[row-i,column+i] == self.board[row-1-i,column+1+i] == self.board[row-2-i,column+2+i]
            == self.board[row-3-i,column+3+i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the left diagonal 5")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the left diagonal 5")
                    return True
                else:
                    print("error 7")
        row = 5
        column = 3
        for i in range(1): #left diag 6
            if(self.board[row-i,column+i] == self.board[row-1-i,column+1+i] == self.board[row-2-i,column+2+i]
            == self.board[row-3-i,column+3+i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the left diagonal 6")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the left diagonal 6")
                    return True
                else:
                    print("error 8")
        ## right diagonals
        row = 3
        column = 6
        for i in range(1): # right diag 1
            if(self.board[row-i,column-i] == self.board[row-1-i,column-1-i] == self.board[row-2-i,column-2-i]
            == self.board[row-3-i,column-3-i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the right diagonal 1")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the right diagonal 1")
                    return True
                else:
                    print("error 9")
        row = 4
        column = 6
        for i in range(2): # right diag 2
            if(self.board[row-i,column-i] == self.board[row-1-i,column-1-i] == self.board[row-2-i,column-2-i]
            == self.board[row-3-i,column-3-i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the right diagonal 2")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the right diagonal 2")
                    return True
                else:
                    print("error 10")
        row = 5
        column = 6
        for i in range(3): # right diag 3
            if(self.board[row-i,column-i] == self.board[row-1-i,column-1-i] == self.board[row-2-i,column-2-i]
            == self.board[row-3-i,column-3-i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the right diagonal 3")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the right diagonal 3")
                    return True
                else:
                    print("error 11")
        row = 5
        column = 5
        for i in range(3): # right diag 4
            if(self.board[row-i,column-i] == self.board[row-1-i,column-1-i] == self.board[row-2-i,column-2-i]
            == self.board[row-3-i,column-3-i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the right diagonal 4")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the right diagonal 4")
                    return True
                else:
                    print("error 12")
        row = 5
        column = 4
        for i in range(2): # right diag 5
            if(self.board[row-i,column-i] == self.board[row-1-i,column-1-i] == self.board[row-2-i,column-2-i]
            == self.board[row-3-i,column-3-i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the right diagonal 5")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the right diagonal 5")
                    return True
                else:
                    print("error 13")
        row = 5
        column = 3
        for i in range(1): # right diag 6
            if(self.board[row-i,column-i] == self.board[row-1-i,column-1-i] == self.board[row-2-i,column-2-i]
            == self.board[row-3-i,column-3-i] != 0):
                if(self.board[row-i,column+i] == 1):
                    print("red wins! four are connected on the right diagonal 6")
                    return True
                elif(self.board[row-i,column+i] == 2):
                    print("black wins! four are connected on the right diagonal 6")
                    return True
                else:
                    print("error 14")

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
