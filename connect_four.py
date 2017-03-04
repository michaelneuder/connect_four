#!/usr/bin/env python3
# connect four

class connect_four(object):
    def __init__(self):
        self.size = 7
        self.board = [[0 for x in range(self.size)] for y in range(self.size)]

    def print_board(self):
        print("    "+"-"*17)
        for x in range(self.size):
            print("    | {} {} {} {} {} {} {} |".format(self.board[x][0], self.board[x][1],
            self.board[x][2], self.board[x][3], self.board[x][4], self.board[x][5],
            self.board[x][6]))
        print("    "+"-"*17)

    def make_move(self, color, column):
        print("a", color, "piece was placed in column", column)
        for row in range(self.size):
            while(self.board[column][row] == 0 and row == 4):
                row+=1
            if(color == 'red'):
                self.board[column][row-1] == 1
            elif(color == 'black'):
                self.board[column][row-1] == 2
            else:
                print("color error")
        print("this is the new board state")
        self.print_board()

def main():
    cf_board = connect_four()
    cf_board.print_board()
    cf_board.make_move('red', 4)





if (__name__ == "__main__"):
    main()
