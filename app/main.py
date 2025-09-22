import sys
from PyQt5 import QtWidgets
from .editor import PDFTocEditor

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = PDFTocEditor()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()