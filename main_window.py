#!/usr/bin/env python3
from PyQt5.QtWidgets import *
from pvai_main_widget import pvai_main_widget
from pvp_main_widget import pvp_main_widget
from home_main_widget import home_main_widget
from how_to_play import rules_main_widget
from main_widget import main_widget

class main_window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(QDesktopWidget().width() * 0.6, QDesktopWidget().height() *.85 )
        self.central_widget = main_widget()
        self.setCentralWidget(self.central_widget)

        # self.main_menu_return()
    # def main_menu_return(self):
    #     self.central_widget = home_main_widget()
    #     self.setCentralWidget(self.central_widget)
    #     self.central_widget.pvp_push_button.clicked.connect(self.pvp_clicked)
    #     self.central_widget.pvai_push_button.clicked.connect(self.pvai_clicked)
    #     self.central_widget.rules_push_button.clicked.connect(self.rules_clicked)
    #     self.central_widget.game_history_push_button.clicked.connect(self.game_history_clicked)
    #     self.central_widget.quit_push_button.clicked.connect(self.quit_clicked)
    #
    # def pvp_clicked(self):
    #     self.central_widget = pvp_main_widget()
    #     self.setCentralWidget(self.central_widget)
    #     self.central_widget.home_clicked_signal.connect(self.main_menu_return)
    #
    # def pvai_clicked(self):
    #     self.central_widget = pvai_main_widget()
    #     self.setCentralWidget(self.central_widget)
    #     self.central_widget.home_clicked_signal.connect(self.main_menu_return)
    #
    # def rules_clicked(self):
    #     self.central_widget = rules_main_widget()
    #     self.setCentralWidget(self.central_widget)
    #     self.central_widget.home_clicked_signal.connect(self.main_menu_return)

    def game_history_clicked(self):
        print('game history')

    def quit_clicked(self):
        exit()
