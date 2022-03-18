import numpy as np
import pandas as pd
import os
import cv2
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose
from keras.models import Model
from keras.preprocessing import image               # advanced math library
from keras.layers.core import Dense, Dropout, Activation # Types of layers to be used in our model
from keras.utils import np_utils                         # NumPy related tools
import keras
import tensorflow as tf
from sklearn.model_selection import train_test_split


#!unzip celebA_test.zip

def load_images_from_folder(celebA_test):
  images = [ ]
  for filename in os.listdir(celebA_test):
    img = cv2.imread(os.path.join(celebA_test, filename))
    if img is not None:
      images.append(img)
  return images

X = load_images_from_folder('celebA_test/')
X=np.asarray(X)



celebA_path = "celebA_test/"

celebA = []
for filename in os.listdir(celebA_path):
    if filename.endswith(".jpg"):
        img = image.load_img(celebA_path+filename, target_size=(128, 128))
        celebA.append(image.img_to_array(img))
celebA = np.array(celebA)
print("Data Set", celebA.shape)


def show_celebA_data(X, n=10, title=""):
    plt.figure(figsize=(15, 5))
    for i in range(n):
        ax = plt.subplot(2,n,i+1)
        plt.imshow(image.array_to_img(X[i]))
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.suptitle(title, fontsize = 20)
    plt.show()

show_celebA_data(celebA, title="celebA")



X_train, X_test = train_test_split(celebA,
                                    test_size=0.2,
                                    random_state=0)


input_layer = Input(shape=(128, 128, 3), name="INPUT")
x =  Conv2D(16, (3, 3), activation='relu', padding='same')(input_layer)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)

code_layer = MaxPooling2D((2, 2), name="CODE")(x)
input_layer_d = Input(shape=(16,16,8), name="INPUT")

l1 = Conv2DTranspose(8, (3, 3), activation='relu', padding='same')
x = l1(code_layer)
x_d = l1(input_layer_d)

x = UpSampling2D((2, 2))(x)
x_d =  UpSampling2D((2, 2))(x_d)

l2 =  Conv2DTranspose(8, (3, 3), activation='relu', padding='same')

x = l2(x)
x_d = l2(x_d)

x = UpSampling2D((2, 2))(x)
x_d = UpSampling2D((2, 2))(x_d)

l3 = Conv2DTranspose(16, (3, 3), activation='relu', padding='same')
x = l3(x)
x_d = l3(x_d)

x = UpSampling2D((2,2))(x)
x_d = UpSampling2D((2, 2))(x_d)

lo =  Conv2D(3, (3, 3), padding='same', name="OUTPUT")
output_layer = lo(x)
output_layer_d = lo(x_d)


X_d = Model(input_layer_d,output_layer_d)
X_AE = Model(input_layer, output_layer)
X_d.compile(optimizer='adam', loss='mse')
X_AE.compile(optimizer='adam', loss='mse')
X_d.summary()
X_AE.summary()


X_AE.fit(X_train, X_train,
                epochs=3, #put 30 or more
                batch_size=32,
                shuffle=True,
                validation_data=(X_test, X_test))
X_AE.save("X_AE.h5")

def auto_encoder():
    get_encoded_X = Model(inputs=X_AE.input, outputs=X_AE.get_layer("CODE").output)

    encoded = get_encoded_X.predict(X_test)
    encoded = encoded.reshape((len(X_test), 16*16*8))
    encoded.shape

    reconstructed = X_AE.predict(X_test)
    return encoded, reconstructed

encoded, reconstructed=auto_encoder()

def show_data(X, n=10, height=28, width=28, title=""):
    plt.figure(figsize=(10, 3))
    for i in range(n):
        ax = plt.subplot(2,n,i+1)
        plt.imshow(X[i].reshape((height,width)))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.suptitle(title, fontsize = 20)
    plt.show()

def decoder(encodedPictures):
    encodedPictures.shape

    encodedRS = encodedPictures.reshape((len(X_test),16,16,8))
    encodedRS.shape

    decoded = X_d.predict(encodedRS)
    return decoded

#show_celebA_data(X_test, title="original")
#show_data(encoded, height=32, width=64, title="encoded")
#show_celebA_data(decoded, title="reconstructed")


if __name__ == "__main__":
    show_celebA_data(X_test, title="original")
    show_data(encoded, height=32, width=64, title="encoded")
    show_celebA_data(decoded, title="reconstructed")
