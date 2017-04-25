#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from main_widgets.pvai_main_widget import pvai_main_widget
from main_widgets.pvp_main_widget import pvp_main_widget
from main_widgets.home_main_widget import home_main_widget
from main_widgets.how_to_play import rules_main_widget
from main_widget import main_widget

class main_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(QDesktopWidget().width() * 0.6, QDesktopWidget().height() *.85 )
        self.central_widget = main_widget()
        self.setCentralWidget(self.central_widget)

    def game_history_clicked(self):
        print('game history')

    def quit_clicked(self):
        exit()
