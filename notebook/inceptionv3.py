import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from keras import layers
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

from pneumonia.ml_logic.preprocessor import train_generator, val_generator, test_generator
from pneumonia.ml_logic.baseline import compile, fitting
from tensorflow.keras.layers import Rescaling
from tensorflow.keras import Input

from tensorflow.keras.applications.inception_v3 import InceptionV3


def initialize_inceptionv3():

    '''Initializes a pre-trained model from the keras library'''
    incep = InceptionV3(input_shape = (256, 256, 3), include_top = False, weights = 'imagenet')
    incep.trainable = False

    return incep

def load_own_model(model):
    """Initializes a model with a the pre-trained model on top of it"""
    input_dim = (256,256,3)
    scale = (1./255.)
    incep_model = initialize_inceptionv3()
    model = Sequential([
        incep_model,
        Input(shape=input_dim),
        Rescaling(scale),
        Flatten(),
        Dense(32, activation="relu"),
        Dropout(0.2),
        Dense(1, activation='sigmoid')
    ])

    return model

def save_model(model):
    """
    Persist trained model locally on hard drive at f"{LOCAL_REGISTRY_PATH}/models/{timestamp}.h5"
    - if MODEL_TARGET='gcs', also persist it on your bucket on GCS at "models/{timestamp}.h5"
    """
    pass


def evaluate_model(model, batch_size=32):
    '''Evaluate trained model performance'''

    evaluation = model.evaluate(test_generator(), batch_size=batch_size)
    print(f'Test Loss: {evaluation[0] * 100:.2f}%')
    print(f"Test Accuracy: {evaluation[1] * 100:.2f}%")
    print(f"Test Recall: {evaluation[2] * 100:.2f}%")

    return evaluation

#Instatiate model
inception_model = initialize_inceptionv3()
inception_model = load_own_model(inception_model)

#compile the model
compile(inception_model)

# Fit the model
#history_inceptionv3 = fitting(inception_model, use_multiprocessing=False)

evaluate_model(inception_model)

#Save the model
# path = '/Users/simrankaurvohra/code/anya9889/pneumonia_diagnosis/model.h5'
# inception_model.save(path)
