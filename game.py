from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from blackjackUi import Ui_MainWindow
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
import random

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
        self.wongame=False #win game or not
        self.action='stay'

        self.ui.winnings.setText(str(self.winnings))
        self.ui.playercards.setText(str(self.playercardsvalue))
        self.ui.dealercards.setText(str(self.dealercardsvalue))
        self.ui.dealertext.setText(self.dealertext)

        self.game()


    def game(self):
        

        while True:
            
            #deal 2 cards to player and dealer
            randomnum=abs(random.randint(0,51))
            self.ui.pcard1.setPixmap(QtGui.QPixmap(imagePaths[randomnum]))
            self.playercardsvalue+=cardValues[randomnum]
            self.playercardcount+=1

            randomnum=abs(random.randint(0,51))
            self.ui.pcard2.setPixmap(QtGui.QPixmap(imagePaths[randomnum]))
            self.playercardsvalue+=cardValues[randomnum]
            self.playercardcount+=1

            randomnum=abs(random.randint(0,51))
            self.ui.dcard1.setPixmap(QtGui.QPixmap(imagePaths[randomnum]))
            self.dealercardsvalue+=cardValues[randomnum]
            self.revealeddealervalue=cardValues[randomnum]
            self.dealercardcount+=1

            self.ui.dcard2.setPixmap(QtGui.QPixmap('dickerson.png'))
            self.dealercardsvalue+=cardValues[randomnum]
            self.dealercardcount+=1

            
            self.dealertext='Dealer: You can hit, stay, double down, or split. Press the button to take a picture whenver you are ready.'
            
            self.ui.winnings.setText(str(self.winnings))
            self.ui.playercards.setText(str(self.playercardsvalue))
            self.ui.dealercards.setText(str(self.revealeddealervalue))
            self.ui.dealertext.setText(self.dealertext)

            if self.action=='stay':
                break

    

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    window=BlackjackGame()
    window.show()
    sys.exit(app.exec())
    


    


    

 