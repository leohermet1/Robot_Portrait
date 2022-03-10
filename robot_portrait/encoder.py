import numpy as np                   # advanced math library
import matplotlib.pyplot as plt      # plotting routines
import tensorflow as tf
from tensorflow import keras
from keras.models import Model       # Model type to be used
from keras.layers.core import Dense, Dropout, Activation # Types of layers to be used in our model
from keras.utils import np_utils                         # NumPy related tools


from sklearn.datasets import fetch_olivetti_faces # Olivetti faces dataset
dataset = fetch_olivetti_faces()
X = dataset["data"]
X

from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(X,
                                   test_size=0.2,
                                   random_state=0)

input_shape = (64,64,1)
encoded_dim = 10

input_img = keras.Input(shape=input_shape)
x = keras.layers.Conv2D(64, (3, 3),strides=1,activation='relu', padding='same')(input_img)
x = keras.layers.MaxPooling2D((2, 2), padding='same')(x)
x = keras.layers.Dropout(0.2)(x)
x = keras.layers.Flatten()(x)
x = keras.layers.Dense(64,"relu")(x)
encoded = keras.layers.Dense(encoded_dim,activation='relu')(x)

# at this point the representation is (16, 16, 4) i.e. 128-dimensional
x = keras.layers.Dense(64,"relu")(encoded)
x = keras.layers.Dense(32*32*8,"relu")(x)
x = keras.layers.Reshape((32,32,8))(x)
x = keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same')(x)
x = keras.layers.UpSampling2D((2, 2))(x)
decoded = keras.layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = keras.Model(input_img, decoded)
encoder = keras.Model(input_img, encoded)

autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

X_train = X_train.reshape(-1,64,64,1)
X_test = X_test.reshape(-1,64,64,1)

autoencoder.fit(X_train, X_train,
                epochs=10,#need to put 100  
                batch_size=32,
                shuffle=True,
                validation_data=(X_test, X_test))

def encoder():
    encoder = keras.Model(input_img, encoded)
    encoded_imgs = encoder.predict(X_test)
    return encoded_imgs

def decoder():
    decoded_imgs = autoencoder.predict(X_test)
    n = 9  # How many faces we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        #Display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(X_test[i].reshape(64, 64))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        #Display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_imgs[i].reshape(64, 64))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()
    return 0