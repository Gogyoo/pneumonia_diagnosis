import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import image_dataset_from_directory


def train_generator():
    '''Loads images from train folder on disk, performs normalization on images.
    Returns images in train_generator'''

    train_generator = image_dataset_from_directory("../raw_data/train",
    color_mode='rgb',
    batch_size=32,
    image_size=(256, 256),
    label_mode='binary',
    shuffle=True,
    seed=42)

    return train_generator

def val_generator():
    ''' Loads images from val(validation) folder on disk, performs normalization on images.
    Returns images in val_generator'''

    val_generator = image_dataset_from_directory("../raw_data/val",
    color_mode='rgb',
    batch_size=32,
    image_size=(256, 256),
    label_mode='binary',
    shuffle=True,
    seed=42)

    return val_generator

def test_generator():
    ''' Loads images from test folder on disk, performs normalization on images.
    Returns images in test_generator'''

    test_generator = image_dataset_from_directory("../raw_data/test",
    color_mode='rgb',
    batch_size=32,
    image_size=(256, 256),
    label_mode='binary',
    shuffle=True,
    seed=42)

    return test_generator
