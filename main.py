#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication
from main_window import main_window

def main():
    connect_four_app = QApplication([])
    main_window_cf = main_window()
    main_window_cf.show()
    exit(connect_four_app.exec_())

if __name__ == '__main__':
    main()
