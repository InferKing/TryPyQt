from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from random import choice, randint, uniform
import pyautogui as pg
import sys


class Window(QWidget):
    def __init__(self):
        # parameters
        self.MAX_LENGTH = 25  # should be more than 24
        self.MIN_LENGTH = 6
        self.PASSWORD_LENGTH = 8
        self.X = 0
        self.Y = 0
        # init
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setWindowTitle("Generator of password")
        self.setFixedSize(400, 200)
        self.setLayout(layout)
        self.label = QLabel("Lets make a new password!")
        layout.addWidget(self.label, 0, 0)
        # lineEdit
        self.lineEdit = QLineEdit()
        self.lineEdit.setFixedWidth(220)
        self.lineEdit.setText("Password")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setMaxLength(self.MAX_LENGTH)
        layout.addWidget(self.lineEdit, 1, 0)
        # button
        self.button = QPushButton("Generate")
        self.button.setFixedWidth(150)
        self.button.clicked.connect(self.create_password)
        layout.addWidget(self.button, 1, 1)
        # checkBoxes
        self.checkBox_digits = QCheckBox("Digits")
        self.checkBox_digits.setChecked(True)
        layout.addWidget(self.checkBox_digits, 2, 0)
        self.checkBox_letters = QCheckBox("Letters")
        self.checkBox_letters.setChecked(True)
        layout.addWidget(self.checkBox_letters, 3, 0)
        self.checkBox_symbols = QCheckBox("Symbols")
        self.checkBox_symbols.setChecked(True)
        layout.addWidget(self.checkBox_symbols, 2, 1)
        self.checkBox_capital_letters = QCheckBox("Capital letters")
        self.checkBox_capital_letters.setChecked(True)
        layout.addWidget(self.checkBox_capital_letters, 3, 1)
        # slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setValue(self.PASSWORD_LENGTH)
        self.slider.setMinimum(self.MIN_LENGTH)
        self.slider.setMaximum(self.MAX_LENGTH)  # self.slider.range(self.MIN_LENGTH,self.MAX_LENGTH)
        self.slider.setTickPosition(self.PASSWORD_LENGTH)
        self.slider.setTickInterval(self.MAX_LENGTH)
        self.slider.valueChanged.connect(self.slider_shows_length)  # valueChanged returns value in handler
        layout.addWidget(self.slider, 4, 0)
        self.sliderLabel = QLabel(f"Length of password {str(self.slider.tickPosition())}")
        layout.addWidget(self.sliderLabel, 4, 1)
        # move button
        self.secButton = QPushButton("CLICK ME")
        self.secButton.clicked.connect(self.move_window)
        layout.addWidget(self.secButton,5,0)


    def create_password(self):
        array = []
        letters = "qwertyuiopasdfghjklzxcvbnm"
        digits = "0123456789"
        symbols = "._-#@!/?[]{}"
        if self.checkBox_digits.isChecked():
            for i in digits: array.append(i)
        if self.checkBox_letters.isChecked():
            for i in letters: array.append(i)
        if self.checkBox_symbols.isChecked():
            for i in symbols: array.append(i)
        if self.checkBox_capital_letters.isChecked():
            for i in letters.upper(): array.append(i)
        if not array:
            self.lineEdit.setText("Select at least one item!")
        else:
            password = ""
            for i in range(self.PASSWORD_LENGTH):
                password += choice(array)
            self.lineEdit.setText(password)
            # alert(text="Password was created!", title="ALERT", button="OK")

    def slider_shows_length(self, value):
        self.PASSWORD_LENGTH = value
        self.sliderLabel.setText(f"Length of password {str(value)}")

    def move_window(self):
        self.X = randint(0,1500)
        self.Y = randint(0,850)
        print(self.X,self.Y)
        self.move(self.X,self.Y)
        pg.click(self.X+randint(50,200),self.Y+205,duration=uniform(0.4,0.7))


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
