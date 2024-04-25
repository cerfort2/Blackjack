# Blackjack


##Important files:

- game.py: the main script of the Blackjack game that contains the blackjack logic, communication with the tflite model, pi camera, and GPIO pins
- blackjackUi.py: my QT designer user interface file exported into python code. I run this file to be able to communicate with my UI
- neural.py: This file was used to train a neural network to correctly classify the blackjack actions. This file was too large to upload to github. I also did not upload the training data I used because this file was also very large. One could train this network by collecting training data, put the images of each desired class into separate folders, and point the training code to the paths of these folders.
- modeltest.py: This file was used to obtain the output classification from the neural network. Modified code of this file can be found in game.py
- button.py: This file was used to obtain GPIO inputs from the Raspberry Pi. This code can also be found in game.py and threads are defined in game.py to connect a button press to a python function.
- picam.py: This file was used to capture and process a picture from the Raspberry Pi

## Other files:
- Files not mentioned were used to either scale images to a different size or are images that are displayed in my User Interface.

##Installation:

- The below libraries are used to communicate with the neural network and process the images. In addition, one could choose to make this completely software by adding buttons on to the User Interface in the Qt designer app and substituting in code to take a picture with your computer camera rather than the Raspberry Pi's camera.

```bash
pip install tensorflow==2.15
pip install opencv-python
pip install PyQt6
pip install numpy
```


