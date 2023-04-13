
# Basic imports
import numpy as np
import time
import os

# DL / Keras
import tensorflow as tf
from tensorflow.keras import Sequential, layers, models
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.metrics import Recall
from tensorflow.keras.optimizers import Adam
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from tensorflow.keras import Sequential, layers
from tensorflow.keras.layers import Rescaling
from tensorflow.keras import Input

from pneumonia.ml_logic.preprocessor import train_generator, val_generator, test_generator

# Balancing the weights to give the minority class (pneumonia images) a higher weight
num_pneumonia = len(os.listdir(r"../raw_data/train/PNEUMONIA"))
num_normal = len(os.listdir(r'../raw_data/train/NORMAL'))

weight_for_0 = num_pneumonia / (num_normal + num_pneumonia)
weight_for_1 = num_normal / (num_normal + num_pneumonia)

class_weight = {0: weight_for_0, 1: weight_for_1}


def initialize():
    """Creation of an NN architecture, followed by its compilation
       Returns a Sequential object"""
    input_dim = (256,256,3)
    scale = (1./255.)

    model = Sequential([
        Input(shape=input_dim),
        Rescaling(scale),
        layers.Conv2D(16, (4,4), input_shape=input_dim, activation='relu'),
        layers.Flatten(),
        layers.Dense(1, activation='sigmoid')
    ])

    return model


def compile(model):
    #Compile the model
    opt = Adam(learning_rate=0.001)
    print(model.summary())
    model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy',Recall()])

    return model


def fitting(model,use_multiprocessing=True):
    """A passed model is being fitted across both train and validation sets,
    and the computation may be ended early through EarlyStopping.
    Returns the History object of the fitted model"""

    start_time = time.time()
    stopit = EarlyStopping(patience=5)

    history = model.fit(train_generator(),
                        epochs=20,
                        batch_size=32,
                        callbacks=stopit,
                        class_weight=class_weight,
                        validation_data=val_generator(),
                        verbose=True,
                        use_multiprocessing=use_multiprocessing)

    print(f"--- {(time.time() - start_time)} ---")
    return model, history


# base1 = initialize()

# compile(base1)

# history = fitting(base1, use_multiprocessing=False)
# print(history.history)
