from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle

class StyleSheet():
    def __init__(self):
        QtGui.QFontDatabase.addApplicationFont("Exo 2")
        font = QtGui.QFont("Exo 2")
        self.setFont(font)

        self.setStyleSheet(
            "QWidget { color: #bbbfc3; background-color: #282b30; }"
            "QPushButton { background-color: #424549; }"
            #"QRadioButton { color: #424549; }"
            #"QRadioButton::indicator { border : 1px solid black; width : 25; height : 12; border-radius : 7; }"

        )

