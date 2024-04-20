import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

from keras.preprocessing.image import ImageDataGenerator

# Define parameters for data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)

# Define model parameters
num_classes = 3  # hit, stay, split
input_shape = (224, 224, 3)  # Input shape (height, width, channels)

train_generator = train_datagen.flow_from_directory(
    'images/training',
    target_size=(224, 224),
    batch_size=5,
    class_mode='categorical',
    subset='training')  # set as training data

validation_generator = train_datagen.flow_from_directory(
    'images/training',  # same directory as training data
    target_size=(224, 224),
    batch_size=5,
    class_mode='categorical',
    subset='validation')  # set as validation data

# Build the model
model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(num_classes, activation='softmax')
])

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Display model summary
model.summary()

# Define the number of training and validation samples
num_train_samples = train_generator.samples
num_validation_samples = validation_generator.samples

# Fit the model
history = model.fit(
    train_generator,
    steps_per_epoch=num_train_samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=num_validation_samples // validation_generator.batch_size,
    epochs=15)

# Save the model
model.save('my_image_model.h5')

# Convert model to TensorFlow Lite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TensorFlow Lite model
with open('model_image.tflite', 'wb') as f:
    f.write(tflite_model)
