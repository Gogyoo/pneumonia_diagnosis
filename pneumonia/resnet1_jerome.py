"""Establishing the performance of the ResNetV2 pre-trained model"""

# Basic imports
import numpy as np
import time
import pandas as pd

# DL / Keras

from tensorflow.keras import Sequential, layers, models, optimizers
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet_v2 import ResNet50V2


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

#Load images in TFDS structures

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

def initialize_resnet():
    """Initializes a pre-trained model from the keras library"""
    transfer = ResNet50V2(
    include_top=False,
    weights='imagenet',
    input_shape=(256,256,3),
    pooling=None,
    classes=1000
    )
    transfer.trainable = False

    return transfer

def load_own_model(resnet):
    """Initializes a model with a the pre-trained model on top of it"""
   #TODO: find how to make a (256,256,1) fit in the input layer
    model = Sequential()

    model.add(resnet)
    model.add(layers.Flatten())
    model.add(layers.Dense(100, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    return model

def compile(model):
    """Compiles a model"""

    opt = optimizers.Adam(learning_rate=1e-4)
    model.compile(loss='binary_crossentropy',
                  optimizer=opt,
                  metrics=['accuracy'])
    return model


def save_model():
    #TODO: implement for portability
    pass


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
                        batch_size=16,
                        callbacks=stopit,
                        validation_data=val_generator,
                        verbose=True,
                        use_multiprocessing=True)

    print(f"--- {(time.time() - start_time)} ---")
    return history

resnet = initialize_resnet()
full_resnet = load_own_model(resnet)
full_resnet = compile(full_resnet)
history = fitting(full_resnet)
