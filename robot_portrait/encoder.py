import numpy as np                   # advanced math library
import matplotlib.pyplot as plt      # plotting routines
from keras.models import Model       # Model type to be used
from keras.layers.core import Dense, Dropout, Activation # Types of layers to be used in our model
from keras.utils import np_utils                         # NumPy related tools
import keras
import tensorflow as tf
from sklearn.model_selection import train_test_split



X_train, X_test = train_test_split(X,
                                   test_size=0.2,
                                   random_state=0)
