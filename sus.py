from multiprocessing.sharedctypes import Value
from PyQt6.QtWidgets import QApplication, QWidget , QPushButton, QLabel
from PyQt6.QtGui import QIcon , QFont
import sys
from random import randint

#position of No
#height 200-300
#width 220-310


# This is the window itself you know the renderin and ol
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The SUS detector")
        self.setGeometry(900,200,  400,350)
        #self.setGeometry(#where to spawn app,size of the app)

        self.create_widgets()

# This function creates the inside of that window
    def create_widgets(self):
        # Tweak the Yes button
        self.btnYes = QPushButton("Yes", self)
        # Yea u need maffs here but just search for default coordinates
        self.btnYes.setGeometry(40,265,80,40)
        self.btnYes.clicked.connect(self.clickedYes)



        # Tweak the No button
        self.btnNo = QPushButton("No", self)
        self.btnNo.setGeometry(270,265,80,40)#270
        self.btnNo.clicked.connect(self.clickedNo)


        # The Question
        self.label = QLabel("Does your parents know your Gay?", self)
        self.label.setGeometry(40,100,400,100)
        self.label.setFont(QFont("Lato",15))
        self.label.setStyleSheet("font-weight: bold")


    # The No button logic
    def clickedNo(self):
        height = randint(200,300)
        width = randint(220,310)
        self.btnNo.setGeometry(width,height,80,40)


    def clickedYes(self):
        self.label.setText("Damn Bro.......sus")
        self.label.setGeometry(60,100,400,100)
        self.btnYes.setGeometry(500,500,80,40)
        self.btnNo.setGeometry(500,500,80,40)
        

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())