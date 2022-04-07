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
#!unzip celebA_test.zip


#Get the pictures as np.array
def get_pictures(file_str):
    '''
    Returns a numpy array of the pixels of all the pictures

            Parameters:
                    file_str(string) : String of the directory towards the file containing all the celebA pictures

            Returns:
                    celebA (numpy.array): Numpy array of the pixels of each picture in the file
    '''
    celebA_path = file_str
    celebA = []
    for filename in os.listdir(celebA_path):
        if filename.endswith(".jpg"):
            img = image.load_img(celebA_path+filename, target_size=(128, 128))
            celebA.append(image.img_to_array(img))
    celebA = np.array(celebA)
    return celebA

celebA = get_pictures("~/Robot_Portrait/robot_portrait/celebA_10000/")



#Create the train and test data set
def creat_train_data(celebA):
    '''
    Returns the training part and the testing part of data of the pictures which will be used to train the model after

            Parameters:
                    celebA (numpy.array) : Numpy array of the pixels of each picture in the file

            Returns:
                    X_train, X_test (numpy.array): Numpy array of the pictures of the training part and testing part
    '''
    X_train, X_test = train_test_split(celebA,
                                        test_size=0.2,
                                        random_state=0)
    return X_train, X_test

X_train, X_test = creat_train_data(celebA)



#definition of the model
def get_models():
    '''
    Returns the autoencoder and decoder model (dercoder model with the same layers with that of autoencoder)

            Parameters:
                    No parameters

            Returns:
                    X_d ,X_AE (model) : autoencoder and decoder model
    '''
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
    return X_d,X_AE

X_d,X_AE = get_models()



#train the model
def train_autoencoder_model(X_train,X_test):
    '''
    Returns the trained autoencoder with our pictures

            Parameters:
                    X_train, X_test(numpy.array) : Numpy array of the pictures of the training part and testing part

            Returns:
                    X_AE (model) : trained autoencoder(decoder is trained automatically within the training of autoencoder)
    '''
    X_AE.fit(X_train, X_train,
                    epochs=50,
                    batch_size=32,
                    shuffle=True,
                    validation_data=(X_test, X_test))
    return X_AE

X_AE = train_autoencoder_model(X_train,X_test)



#save the models
X_AE.save("auto_encoder.h5")
X_d.save("decoder.h5")



#get the encoded vector
def auto_encoder():
    '''
    Returns the encoded pictures and the decoded pictures with the models

            Parameters:
                    No parameters

            Returns:
                    encoded, reconstructed(numpy.array) : Numpy array of the pixels of the encoded pictures and the decoded pictures
    '''
    get_encoded_X = Model(inputs=X_AE.input, outputs=X_AE.get_layer("CODE").output)

    encoded = get_encoded_X.predict(X_test)
    encoded = encoded.reshape((len(X_test), 16*16*8))

    reconstructed = X_AE.predict(X_test)
    return encoded, reconstructed

encoded, reconstructed=auto_encoder()

#save the encoded vector
np.save("encoded.npy", encoded)
