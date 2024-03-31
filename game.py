from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from blackjackUi import Ui_MainWindow
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
import random
import time

cardValues = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
]

imagePaths = [
    "PNG-cards-1.3/2_of_clubs.png",
    "PNG-cards-1.3/3_of_clubs.png",
    "PNG-cards-1.3/4_of_clubs.png",
    "PNG-cards-1.3/5_of_clubs.png",
    "PNG-cards-1.3/6_of_clubs.png",
    "PNG-cards-1.3/7_of_clubs.png",
    "PNG-cards-1.3/8_of_clubs.png",
    "PNG-cards-1.3/9_of_clubs.png",
    "PNG-cards-1.3/10_of_clubs.png",
    "PNG-cards-1.3/jack_of_clubs2.png",
    "PNG-cards-1.3/queen_of_clubs2.png",
    "PNG-cards-1.3/king_of_clubs2.png",
    "PNG-cards-1.3/ace_of_clubs.png",
    "PNG-cards-1.3/2_of_diamonds.png",
    "PNG-cards-1.3/3_of_diamonds.png",
    "PNG-cards-1.3/4_of_diamonds.png",
    "PNG-cards-1.3/5_of_diamonds.png",
    "PNG-cards-1.3/6_of_diamonds.png",
    "PNG-cards-1.3/7_of_diamonds.png",
    "PNG-cards-1.3/8_of_diamonds.png",
    "PNG-cards-1.3/9_of_diamonds.png",
    "PNG-cards-1.3/10_of_diamonds.png",
    "PNG-cards-1.3/jack_of_diamonds2.png",
    "PNG-cards-1.3/queen_of_diamonds2.png",
    "PNG-cards-1.3/king_of_diamonds2.png",
    "PNG-cards-1.3/ace_of_diamonds.png",
    "PNG-cards-1.3/2_of_spades.png",
    "PNG-cards-1.3/3_of_spades.png",
    "PNG-cards-1.3/4_of_spades.png",
    "PNG-cards-1.3/5_of_spades.png",
    "PNG-cards-1.3/6_of_spades.png",
    "PNG-cards-1.3/7_of_spades.png",
    "PNG-cards-1.3/8_of_spades.png",
    "PNG-cards-1.3/9_of_spades.png",
    "PNG-cards-1.3/10_of_spades.png",
    "PNG-cards-1.3/jack_of_spades2.png",
    "PNG-cards-1.3/queen_of_spades2.png",
    "PNG-cards-1.3/king_of_spades2.png",
    "PNG-cards-1.3/ace_of_spades.png",
    "PNG-cards-1.3/2_of_hearts.png",
    "PNG-cards-1.3/3_of_hearts.png",
    "PNG-cards-1.3/4_of_hearts.png",
    "PNG-cards-1.3/5_of_hearts.png",
    "PNG-cards-1.3/6_of_hearts.png",
    "PNG-cards-1.3/7_of_hearts.png",
    "PNG-cards-1.3/8_of_hearts.png",
    "PNG-cards-1.3/9_of_hearts.png",
    "PNG-cards-1.3/10_of_hearts.png",
    "PNG-cards-1.3/jack_of_hearts2.png",
    "PNG-cards-1.3/queen_of_hearts2.png",
    "PNG-cards-1.3/king_of_hearts2.png",
    "PNG-cards-1.3/ace_of_hearts.png",
]

class BlackjackGame(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.winnings=0
        self.dealercardcount=0
        self.revealeddealervalue=0
        self.playercardcount=0
        self.playercardsvalue=0
        self.dealercardsvalue=0
        self.dealertext=""

        self.gameInProgress=True

        self.camerainput=False
        self.action='stay'
        self.playerafter=False

        self.ui.winnings.setText(str(self.winnings))
        self.ui.playercards.setText(str(self.playercardsvalue))
        self.ui.dealercards.setText(str(self.dealercardsvalue))
        self.ui.dealertext.setText(self.dealertext)

        self.game()

    def dealCard(self,playerordealer):
        if not playerordealer:
            randomnum=abs(random.randint(0,51))
            label_name = f"pcard{self.playercardcount+1}"
            getattr(self.ui, label_name).setPixmap(QtGui.QPixmap(imagePaths[randomnum]))
            self.playercardsvalue+=cardValues[randomnum]
            self.playercardcount+=1
        else:
            randomnum=abs(random.randint(0,51))
            label_name = f"dcard{self.dealercardcount+1}"
            self.dealercardsvalue+=cardValues[randomnum]
            self.dealercardcount+=1

            if self.dealercardcount==1:
                self.revealeddealervalue=cardValues[randomnum]

            if self.dealercardcount==2:
                self.ui.dcard2.setPixmap(QtGui.QPixmap('dickerson.png'))
            else:
                getattr(self.ui, label_name).setPixmap(QtGui.QPixmap(imagePaths[randomnum]))

    def game(self):
        

        while self.gameInProgress:
            
            # #deal 2 cards to player and dealer
            if self.dealercardcount==0:
                self.dealCard(False)
                self.dealCard(False)
                self.dealCard(True)
                self.dealCard(True)
            elif self.gameInProgress:
                self.dealCard(self.playerafter)
            

            self.dealertext='Dealer: You can hit, stay, double down, or split. Press the button to take a picture whenver you are ready.'
            
            self.ui.winnings.setText(str(self.winnings))
            self.ui.playercards.setText(str(self.playercardsvalue))
            self.ui.dealercards.setText(str(self.revealeddealervalue))
            self.ui.dealertext.setText(self.dealertext)

            #game won? else get camera input in a while loop
            
            if self.playercardsvalue==21 and self.playercardcount==2:
                self.winnings+=1
                self.gameInProgress=False
            else:
                self.action='stay'
                #get camera input

            
                

    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window=BlackjackGame()
    window.show()
    sys.exit(app.exec())
    


    


    

 