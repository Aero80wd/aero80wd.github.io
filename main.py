import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from tkinter import messagebox,Tk
import untitled
from functools import partial
import threading
root = Tk()
root.withdraw()


def text():
    messagebox.showinfo('1','a')
def textext():
    messagebox.showinfo('2','a')
num = False
def convert(ui):

    input1 = ui.numin.text()

    input2 = ui.spinBox.text()

    ui.label.setText(str(int(input1) + int(input2)))




if __name__ == '__main__':


    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = untitled.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('加法机')


    MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());
    if len(sys.argv) == 3:
        print(int(sys.argv[1]) + int(sys.argv[2]))
        sys.exit(0)
    if len(sys.argv) == 4:
        sys.argv.pop(2)
        print(int(sys.argv[1]) + int(sys.argv[2]))
        sys.exit()
    MainWindow.show()
    ui.ok.clicked.connect(partial(convert, ui))

    sys.exit(app.exec_())

root.mainloop()