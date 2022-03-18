import numpy as np
import os
from keras.datasets import mnist
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose
from keras.models import Model
from keras.preprocessing import image
import keras
import tensorflow as tf
from sklearn.model_selection import train_test_split

#unzip pictures
!unzip celebA_test.zip

#Get the pictures as np.array
celebA_path = "celebA_test/"
celebA = []
for filename in os.listdir(celebA_path):
    if filename.endswith(".jpg"):
        img = image.load_img(celebA_path+filename, target_size=(128, 128))
        celebA.append(image.img_to_array(img))
celebA = np.array(celebA)

#Create the train and test data set
X_train, X_test = train_test_split(celebA,
                                    test_size=0.2,
                                    random_state=0)

#definition of the model
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

#train the model
X_AE.fit(X_train, X_train,
                epochs=50,
                batch_size=32,
                shuffle=True,
                validation_data=(X_test, X_test))
