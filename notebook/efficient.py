import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout
from keras import layers, models
import matplotlib.pyplot as plt
import tensorflow as tf
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

from pneumonia.ml_logic.preprocessor import train_generator, val_generator, test_generator
from pneumonia.ml_logic.baseline import compile, fitting
from tensorflow.keras.layers import Rescaling
from tensorflow.keras import Input
from tensorflow.keras import regularizers

from tensorflow.keras.applications.efficientnet import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input


def efficient():
    # INITIALIZE INPUT LAYER
    input_layer = layers.Input(shape=(256,256,3))
    # PREPROCESSING
    preprocessed = preprocess_input(input_layer)
    # APPLYING THE CONVOLUTIONS OPERATIONS
    # OF THE PRETRAINED INCEPTIONNET ON THE THE PREPROCESSED IMG
    eff_net = EfficientNetB0(include_top = False,
                             weights = 'imagenet')
    eff_net.trainable = False
    activated_img = eff_net(preprocessed)
    # FLATTEN THE ACTIVATED IMG
    flattened = layers.Flatten()(activated_img)
    # HIDDEN DENSE LAYERS
    transfo_1 = layers.Dense(32,activation="gelu")(flattened)
    transfo_1_dropped = layers.Dropout(0.4)(transfo_1)
    prediction = layers.Dense(1,activation="sigmoid")(transfo_1_dropped)
    model = models.Model(inputs=input_layer, outputs=prediction)
    return model


def evaluate_model(model, batch_size=32):
    '''Evaluate trained model performance'''

    evaluation = model.evaluate(test_generator(), batch_size=batch_size)
    print(f'Test Loss: {evaluation[0] * 100:.2f}%')
    print(f"Test Accuracy: {evaluation[1] * 100:.2f}%")
    print(f"Test Recall: {evaluation[2] * 100:.2f}%")

    return evaluation

#Instatiate model
efficient_model = efficient()

#compile the model
efficient_model = compile(efficient_model)

# Fit the model
history_eff = fitting(efficient_model, use_multiprocessing=False)

evaluate_model(efficient_model)

#Save the model
path = '/Users/simrankaurvohra/Documents/28.03.23/model/model_2.h5'
efficient_model.save(path)
