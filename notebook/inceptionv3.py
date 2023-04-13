import numpy as np
import pandas as pd

from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras import layers, models

from pneumonia.ml_logic.preprocessor import train_generator, val_generator, test_generator
from pneumonia.ml_logic.baseline import compile, fitting

from tensorflow.keras import Input

from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input


def inception_v3_pneunomia():
    # INITIALIZE INPUT LAYER
    input_layer = layers.Input(shape=(256,256,3))
    # PREPROCESSING
    preprocessed = preprocess_input(input_layer)
    # APPLYING CONVOLUTION OPERATIONS
    # OF THE PRETRAINED INCEPTIONNET ON THE PREPROCESSED IMAGE
    incep = InceptionV3(include_top = False,
        weights = 'imagenet')
    incep.trainable = False
    activated_img = incep(preprocessed)
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
inception_model = inception_v3_pneunomia()

#compile the model
inception_model = compile(inception_model)

# Fit the model
history_inceptionv3 = fitting(inception_model, use_multiprocessing=False)


evaluate_model(inception_model)

#Save the model
# path = '/Users/simrankaurvohra/Documents/28.03.23/model/model_1.h5'
# inception_model.save(path)


def predictions(model):
    return model.predict(test_generator())

#prediction = predictions(test_generator())
