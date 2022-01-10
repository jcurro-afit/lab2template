import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical

print("Running hellomnist.py")

# Load data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


# Build 3blue1brown model

# Print 3blue1brown model accuracy

# Build better model

# Print better model accuracy

# Build 3blue1brown model again but shuffle data
def mixupdata(input_data, shuffle_data_indices=None):
    """
    Mixes up the input numpy array according to the given shuffle_data_indices or makes up a new random shuffle

    :param input_data: the numpy array to shuffle the data for
    :param shuffle_data_indices: the shuffled index to apply, if not given makes up a new mixed up indexing
    :return: a tuple of the mixed up data and the indexing applied
    """
    shuffle_data = np.array(input_data)
    shuffle_data = np.reshape(shuffle_data, (shuffle_data.shape[0], np.product(shuffle_data.shape[1:])))

    if shuffle_data_indices is None:
        shuffle_data_indices = np.arange(np.product(shuffle_data.shape[1:]))
        np.random.shuffle(shuffle_data_indices)

    shuffle_data = shuffle_data[:, shuffle_data_indices]
    shuffle_data = np.reshape(shuffle_data, input_data.shape)
    return shuffle_data, shuffle_data_indices


# mix up the images
train_images_mixup, mixup = mixupdata(train_images)
test_images_mixup, _ = mixupdata(test_images, mixup)

# show mixed up images

# Predict performance of 3blue1brown model with mixed up images
# I predict ...

# rebuild that 3blue1brown model again from scratch and then retrain with mixed up images
# print 3blue1brown model with mixed up images accuracy

# Compare performance of original 3blue1brown model to the new one trained on the mixed up images
# Comparing the two models ...

