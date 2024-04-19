from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from blackjackUi import Ui_MainWindow
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
import random
import cv2
import time
import keras
from keras.models import Sequential, load_model
import os
from PIL import Image
import numpy as np

cardValues = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
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


class Hand:
    def __init__(self):
        self.playerhand = True
        self.value = 0
        self.multiplier = 1  # for doubling
        self.card1val=0
        self.card2val=0
        self.cardCount = 0
        self.numAces = 0
        


class BlackjackGame(Ui_MainWindow):

    def __init__(self):
        super().__init__()
        
        self.winnings=0
        self.revealeddealervalue=0
        self.dealertext=""
        self.playercardcount=0
        self.split=False

        self.unrevealedcard=0

        self.hands=[]
        self.currenthand=0

        self.gameInProgress=True
        self.dealerDone=False

        self.camerainput=False
        self.action='stay'
        self.playerUp=True

        self.model=keras.models.load_model('my_image_model.h5')
    
    def init_ui(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        MainWindow.show()
        self.ui.start.clicked.connect(self.game)
        self.ui.doubledown.clicked.connect(self.double)
        self.ui.picture.clicked.connect(self.takePicture)

        self.app.exec()
            
    def double(self):
        self.action='double'

    def takePicture(self):
        print('\ntaking picture in 1 second:')
        time.sleep(1)
        cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
        if not cap.isOpened():
            print("Error: Unable to open camera")
        

    # Capture a frame
        ret, frame = cap.read()

    # Release the camera
        cap.release()


        new_width = 224
        new_height = 224

    # Resize the image

        framenew = cv2.resize(frame,(new_width, new_height))




    # Normalize pixel values if your model expects normalization
        image_rgb=cv2.cvtColor(framenew,cv2.COLOR_BGR2RGB)
        image_normalized = image_rgb / 255.0
        image_batch=np.expand_dims(image_normalized,axis=0)


        if ret:
        # Save the captured frame as an image
            prob=self.model.predict(image_batch)[0]
            predicted_class = np.argmax(prob)
    # Compare prediction with expected clas
    #play_sound(result)
            cv2.imwrite('action.png', framenew)

            class_labels={0:'hit',1:'split',2:'stay'}
            neuralclass=class_labels[predicted_class]

            self.action=neuralclass

        else:
            print("Error: Unable to capture picture")

        
        # get class from neural network and return it  
        # os.remove('action.png')

    def dealCard(self,handNumber):
        if handNumber ==11:  #dealer hand 
            randomnum=abs(random.randint(0,51))
            label_name = f"dcard{self.dhand.cardCount+1}"
            self.dhand.value+=cardValues[randomnum]
            self.dhand.cardCount+=1

            if self.dhand.cardCount==1:
                self.revealeddealervalue=cardValues[randomnum]

            if self.dhand.cardCount==2:
                self.ui.dcard2.setPixmap(QtGui.QPixmap('dickerson.png'))
                self.unrevealedcard=randomnum    
            else:
                getattr(self.ui, label_name).setPixmap(QtGui.QPixmap(imagePaths[randomnum]))

            if cardValues[randomnum]==11:
                self.dhand.numAces+=1
            
        else:
            
            randomnum=abs(random.randint(0,51))  
            label_name = f"pcard{self.playercardcount+1}" 

            getattr(self.ui, label_name).setPixmap(QtGui.QPixmap(imagePaths[randomnum]))
            self.hands[handNumber].value+=cardValues[randomnum]
            self.playercardcount+=1
            self.hands[handNumber].cardCount+=1
            
            if self.hands[handNumber].cardCount==1:
                self.hands[handNumber].card1val=cardValues[randomnum]
            elif self.hands[handNumber].cardCount==2:
                self.phand.card2val=cardValues[randomnum]

            if cardValues[randomnum]==11:
                self.hands[handNumber].numAces+=1

            if self.hands[handNumber].value>21 and self.hands[handNumber].numAces>=1:
                    self.hands[handNumber].numAces==0
                    self.hands[handNumber].value-=10

    def game(self):
        while self.ui.autodeal.checkState():
            self.split=False
            self.playerUp=True
            self.dealerDone=False
            self.dealertext='Good luck, emperor.'
            self.ui.dealertext.setText(self.dealertext)
            self.ui.playercards.setText('0')
            self.ui.dealercards.setText('0')

            self.hands.clear()

            self.playercardcount=0
            self.phand=Hand()

            self.dhand=Hand()
            self.dhand.playerhand=False

            self.hands.append(self.phand)
            
            self.ui.winnings.setText(str(self.winnings))
            self.gameInProgress=True

            self.numHands=0

            self.ui.dcard1.setPixmap(QtGui.QPixmap())
            self.ui.dcard2.setPixmap(QtGui.QPixmap())
            self.ui.pcard1.setPixmap(QtGui.QPixmap())
            self.ui.pcard2.setPixmap(QtGui.QPixmap())
            self.ui.dcard4.setPixmap(QtGui.QPixmap())
            self.ui.dcard3.setPixmap(QtGui.QPixmap())
            self.ui.pcard4.setPixmap(QtGui.QPixmap())
            self.ui.pcard3.setPixmap(QtGui.QPixmap())
            self.ui.dcard5.setPixmap(QtGui.QPixmap())
            self.ui.dcard6.setPixmap(QtGui.QPixmap())
            self.ui.pcard5.setPixmap(QtGui.QPixmap())
            self.ui.pcard6.setPixmap(QtGui.QPixmap())

            self.ui.dcard7.setPixmap(QtGui.QPixmap())

            self.ui.pcard7.setPixmap(QtGui.QPixmap())
            self.ui.pcard8.setPixmap(QtGui.QPixmap())
            self.ui.pcard9.setPixmap(QtGui.QPixmap())
            self.ui.pcard10.setPixmap(QtGui.QPixmap())
            self.ui.pcard11.setPixmap(QtGui.QPixmap())
            self.ui.pcard12.setPixmap(QtGui.QPixmap())
            self.ui.pcard13.setPixmap(QtGui.QPixmap())
            self.ui.pcard14.setPixmap(QtGui.QPixmap())
            self.ui.pcard15.setPixmap(QtGui.QPixmap())
            self.ui.pcard16.setPixmap(QtGui.QPixmap())



            QApplication.processEvents()
            time.sleep(.5)

            if True:
                
                #deal 2 cards to player and dealer
                self.dealCard(self.currenthand)
                self.ui.playercards.setText(str(self.hands[self.currenthand].value))
                QApplication.processEvents()
                time.sleep(1)
                self.dealCard(11)
                self.ui.dealercards.setText(str(self.dhand.value))
                QApplication.processEvents()
                time.sleep(1)
                self.dealCard(self.currenthand)
                self.ui.playercards.setText(str(self.hands[self.currenthand].value))
                QApplication.processEvents()
                time.sleep(1)
                self.dealCard(11)          
                self.ui.dealercards.setText(str(self.dhand.value))
                QApplication.processEvents()
                

                self.ui.dealertext.setText(self.dealertext)
                #blackjack?
                if (self.phand.value==21 and self.phand.cardCount==2) or (self.dhand.cardCount==2 and self.dhand.value==21):
                        self.playerUp=False #game is over
                        self.dealerDone=True
    
                        self.ui.dcard2.setPixmap(QtGui.QPixmap(imagePaths[self.unrevealedcard]))

                        if self.dhand.value>21 and self.dhand.numAces>=1: #check for ace
                            self.dhand.numAces-=1
                            self.dhand.value-=10
                    
                        if self.phand.value>21 and self.phand.numAces>=1:
                            self.phand.numAces-=1
                            self.phand.value-=10
                        self.ui.dealercards.setText(str(self.dhand.value))
                else:
                    self.ui.dealercards.setText(str(self.revealeddealervalue))

                if self.phand.value==21 and self.phand.cardCount==2: #player has bj
                    self.winnings+=1.5
                    self.gameInProgress=False
                    self.dealertext='You have blackjack. You are victorious, emperor.'
                    self.ui.dealertext.setText(self.dealertext)
                elif self.dhand.value==21 and self.dhand.cardCount==2: #dealer has bj
                    self.winnings-=1
                    self.gameInProgress=False
                    self.dealertext='Dealer has blackjack. You have lost, emperor.'
                    self.ui.dealertext.setText(self.dealertext)
                else:
                        #game continues and stays until done
                    #collect player input and then call function for phand and phand 1?
                    self.playerGoes()

    #DEALER LOGIC
                    if not self.playerUp:
                        time.sleep(.5)
                        self.ui.dcard2.setPixmap(QtGui.QPixmap(imagePaths[self.unrevealedcard]))
                        QApplication.processEvents()
                        time.sleep(.5)

                        while not self.dealerDone:
                            
                            self.ui.dealercards.setText(str(self.dhand.value))
                            QApplication.processEvents()
                            time.sleep(.5)
                            

                            if self.dhand.value>21 and self.dhand.numAces>=1: #check for ace
                                self.dhand.numAces-=1   #busts, but has an ace
                                self.dhand.value-=10
                                self.dealerDone=False
                            elif self.dhand.value>21 and self.dhand.numAces==0:
                                self.dealerDone=True #bust
                            elif self.dhand.value>=17:
                            #dealer stays when at or above a soft 17
                                self.dealerDone=True
                            else:
                            #dealer hits if not at 17
                                self.dealerDone=False
                                self.dealCard(11)
                                QApplication.processEvents()
                                time.sleep(.5)

    #DEAL OUT WINNINGS FOR PLAYER
                    if not self.playerUp and self.dealerDone:
                        for i in range(len(self.hands)):                       
                            if self.hands[i].value<=21 and (self.hands[i].value>self.dhand.value or self.dhand.value>21):
                #if player hasn't busted and dealer is done and (dealer has busted or has a lower card count)
                #condition for player winnings
                                self.winnings+=self.phand.multiplier*1
                                self.dealertext='Hand ' + str(i) + ': You are victorious, emperor.'
                                self.ui.dealertext.setText(self.dealertext)
                                

                            elif self.phand.value<=21 and self.dhand.value<=21 and self.phand.value==self.dhand.value:
                #if player and dealer are done and have cards <=21 and they equal each other than push
                #push condition     
                                self.winnings+=0
                                self.dealertext='Hand ' + str(i) + ': It is a push emperor.'
                                self.ui.dealertext.setText(self.dealertext)
                            else:
                    #anything else is a loss
                                self.winnings-=self.phand.multiplier*1
                                self.dealertext='Hand ' + str(i) + ': You lost, emperor.'
                                self.ui.dealertext.setText(self.dealertext)
                            
                            self.ui.winnings.setText(str(self.winnings))
                            QApplication.processEvents()
                            time.sleep(2)

                    #implement dealer logic and see for each hand whether they won or not                      


                self.ui.winnings.setText(str(self.winnings))
                QApplication.processEvents()
                time.sleep(1)


    def playerGoes(self):
        
        while self.playerUp:

            self.dealertext='Dealer: You can hit, stay, double down, or split. Press the button to take a picture or double down whenver you are ready.'
            self.ui.dealertext.setText(self.dealertext)

            #GET ACTION
            
            answer=input('proceed?')
            print(self.action)


            if self.action=='stay':
                if len(self.hands)==self.currenthand+1:
                    self.playerUp=False
                else:
                    self.currenthand+=1
                    self.playerUp=True

                self.dealertext='You have chosen to stay.'
                
            elif self.action=='double' and self.hands[self.currenthand].cardCount==2:
                if len(self.hands)==self.currenthand+1:
                    self.dealertext='You have chosen to double down.'
                    self.hands[self.currenthand].multiplier+=1
                    self.dealCard(self.currenthand)
                    self.playerUp=False
                else:
                    self.dealertext='You have chosen to double down.'
                    self.hands[self.currenthand].multiplier+=1
                    self.dealCard(self.currenthand)
                    self.currenthand+=1
                    self.playerUp=True


            elif self.action=='split' and self.hands[self.currenthand].cardCount==2 and self.hands[self.currenthand].card1val==self.hands[self.currenthand].card2val:
                #can split on first two cards of a hand
                
                self.temp=Hand()
                self.temp.card1val=self.hands[self.currenthand].card2val
                self.temp.value+=self.temp.card1val
                self.temp.cardCount=1

                self.hands[self.currenthand].value-=self.hands[self.currenthand].card2val
                self.hands[self.currenthand].card2val=0
                self.hands[self.currenthand].cardCount=1
                

                self.hands.append(self.temp)
                

                self.dealertext='You have chosen to split.'
                self.playerUp=True   

            elif self.action=='hit':
                self.dealertext='You have chosen to hit.'
                self.playerUp=True #player is to be dealt a card if action is not stay

                self.dealCard(self.currenthand)

                if self.hands[self.currenthand].value>21:
                    if (self.currenthand+1)==len(self.hands):
                        self.playerUp=False
                    else:
                        self.currenthand+=1
                        self.playerUp=True
            else:
                self.dealertext='You have chosen an illegal action.'
                self.ui.dealertext.setText(self.dealertext)
                QApplication.processEvents()
                time.sleep(5)
            

            self.ui.dealertext.setText(self.dealertext)
            self.ui.playercards.setText(str(self.hands[self.currenthand].value))
            QApplication.processEvents()
            time.sleep(5)



if __name__ == "__main__":
    game=BlackjackGame()
    game.init_ui()
    




    

 