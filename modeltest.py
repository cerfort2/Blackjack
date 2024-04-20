import time
import cv2
import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model=keras.models.load_model('my_image_model.h5')

def preprocess_frame(imagepath):
    image=cv2.imread(imagepath)
    # Resize frame to model's expected size
    image_resized = cv2.resize(image, (224, 224))
    # Normalize pixel values if your model expects normalization
    image_rgb=cv2.cvtColor(image_resized,cv2.COLOR_BGR2RGB)
    image_normalized = image_rgb / 255.0
    image_batch=np.expand_dims(image_normalized,axis=0)
    return image_batch



def assign_class(imagepath):
    image=preprocess_frame(imagepath)
    # Make prediction
    prob=model.predict(image)[0]
    predicted_class = np.argmax(prob)
    # Compare prediction with expected clas
    #play_sound(result)
    return predicted_class

def main():
    imagepath='images/testing/stay/stay.jpg'
    neuralclass=assign_class(imagepath)
    print('predicted class=',neuralclass)
    class_labels={0:'hit',1:'split',2:'stay'}
    neurallabel=class_labels[neuralclass]
    print('predicted label: ',neurallabel)

if __name__ == "__main__":
    main()