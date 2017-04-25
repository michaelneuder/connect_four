#!/usr/bin/env python3
# connect four

class connect_four(object):
    def __init__(self):
        self.width = 7
        self.height = 6
        self.board = [[0 for x in range(self.height)] for y in range(self.width)]
        self.move_number = 1

    def print_board(self):
        print("    "+"-"*17)
        for x in range(self.height):
            print("    | {} {} {} {} {} {} {} |".format(self.board[0][x],
                self.board[1][x], self.board[2][x], self.board[3][x], self.board[4][x],
                self.board[5][x], self.board[6][x]))
        print("    "+"-"*17)

    def make_move(self, color, column):
        print("a", color, "piece was placed in column", column)
        row = 0
        while(self.board[row][column] == 0 and row < 6):
            row+=1
            print(row)
        if (row == 0 and self.board[column][row] != 0): # condition for a full column
            print("this column is full, please choose another!")
        else: # not full column
            if (row == 5 and self.board[row][column] == 0): # case of the first piece in the column
                print('here')
                if(color == 'red'):
                    self.board[column][row] = 1
                elif(color == 'black'):
                    self.board[column][row] = 2
                else:
                    print("color error")
            else: # not the first piece of the column
                print("entered else")
                if(color == 'red'):
                    self.board[column][row-1] = 1
                elif(color == 'black'):
                    self.board[column][row-1] = 2
                else:
                    print("color error")
        print("this is the new board state")
        self.print_board()

    #
    # def check_win_diag(self):
    #     row = 3
    #     column = 0
    #     for i in range(1):
    #         if(self.board[row-i][column+i] == self.board[row-1-i][column+1+i] == self.board[row-2-i][column+2+i]
    #         == self.board[row-3-i][column+3+i] != 0): # left diag 1
    #             print("we have a winner")
    #             return True
    #     row = 4
    #     column = 0
    #     for i in range(2): #left diag 2
    #         if(self.board[row-i][column+i] == self.board[row-1-i][column+1+i] == self.board[row-2-i][column+2+i]
    #         == self.board[row-3-i][column+3+i] != 0): # left diag 1
    #             print("we have a winner")
    #             return True
    #     row = 5
    #     column = 0
    #     for i in range(3): #left diag 2
    #         if(self.board[row-i][column+i] == self.board[row-1-i][column+1+i] == self.board[row-2-i][column+2+i]
    #         == self.board[row-3-i][column+3+i] != 0): # left diag 1
    #             print("we have a winner")
    #             return True


    def check_win_rc(self):
        for row in range(self.height): # checking for win along each row
            for column in range(self.width - 3):
                if(self.board[column][row] == self.board[column+1][row] == self.board[column+2][row]
                == self.board[column+3][row] != 0):
                    if(self.board[column][row] == 1):
                        print("red wins! four are connected on row", row + 1)
                        return True
                    elif(self.board[column][row] == 2):
                        print("black wins! four are connected on row", row + 1)
                        return True
                    else:
                        print("error 1")
        for column in range(self.width): # checking for win along each column
            for row in range(self.height - 3):
                if(self.board[column][row] == self.board[column][row+1] == self.board[column][row+2]
                == self.board[column][row+3] != 0):
                    if(self.board[column][row] == 1):
                        print("red wins! four are connected on column", column + 1)
                        return True
                    elif(self.board[column][row] == 2):
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
            if(cf_board.check_win_rc()):# or cf_board.check_win_diag()):
                quit()


if (__name__ == "__main__"):
    main()
