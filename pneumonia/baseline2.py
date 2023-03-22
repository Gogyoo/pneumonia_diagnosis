"""The goal of this file is to model the data in an unrefined way.
The files are
"""

# Basic imports
import numpy as np
import time


# DL / Keras

from tensorflow.keras import Sequential, layers, models
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# Data preprocessing and augmentation

train_datagen = ImageDataGenerator(
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    rescale=1.0/255.0,
    dtype='float32'
)

val_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    dtype='float32'
)

train_generator = train_datagen.flow_from_directory(
    directory=r"/home/jerome/code/Anya9889/pneumonia_diagnosis/train",
    target_size=(256, 256),
    color_mode="grayscale",
    batch_size=64,
    class_mode="binary",
    shuffle=True,
    seed=42
)

val_generator = val_datagen.flow_from_directory(
    directory=r"/home/jerome/code/Anya9889/pneumonia_diagnosis/val",
    target_size=(256, 256),
    color_mode="grayscale",
    batch_size=64,
    class_mode="binary",
    shuffle=True,
    seed=42
)



def initialize():
    """Creation of an NN architecture, followed by its compilation

    RETURNS a Sequential object"""


    model = Sequential()
    model.add(layers.Conv2D(16, (4,4), input_shape=(256, 256, 1), activation="relu"))
    #model.add(layers.Dense(8, activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

    return model

def fitting(model):
    """A passed model is being fitted across both train and validation sets,
    and the computation may be ended early through EarlyStopping.

    RETURNS the History object of the fitted model"""


    start_time = time.time()
    stopit = EarlyStopping(patience=5,
                           monitor="val_loss",
                           restore_best_weights=True)


    history = model.fit(train_generator,
                        epochs=20,
                        batch_size=128,
                        callbacks=stopit,
                        validation_data=val_generator,
                        verbose=True,
                        use_multiprocessing=True)

    print(f"--- {(time.time() - start_time)} ---")
    return history


base1 = initialize()
print(base1.summary())

history = fitting(base1)
print(history.history)
