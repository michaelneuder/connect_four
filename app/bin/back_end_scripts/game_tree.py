#!usr/bin/env python3

class game_tree(object):
    def __init__(self, board):
        self.children = []
        self.data = []

    def create_children(self):
    	for i in range(7):
            self.children.append(game_tree())

    def set_children(self, list):
        for i in range(7):
            self.data.append(list[i])
