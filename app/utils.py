# utils.py

from PyQt5 import QtWidgets

def create_separator():
    separator = QtWidgets.QFrame()
    separator.setFrameShape(QtWidgets.QFrame.HLine)
    separator.setFrameShadow(QtWidgets.QFrame.Sunken)
    return separator
