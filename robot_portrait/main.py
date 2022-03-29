import decoder 
from GA import *
from Test_visual_interface import *
from PIL import Image as im
import os
import tensorflow as tf
import keras
from keras.preprocessing import image as imK
import numpy as np



def main():
    #load the model
    decoderModel = keras.models.load_model('decoder.h5')
    #load the encoded vector (numpy.ndarray format)
    picturesEncoded = np.load("encoded.npy")
    numberOfGen=0
    numberMaxOfGen=10
    
    randomseed = random()
    popCreated, indexPop = creationPop(picturesEncoded, randomseed) #to take 9 random faces from the clean and reduced database
    popCreatedDecoded = decoder.decoderFunction(popCreated, decoderModel)

    for i in range (len(popCreatedDecoded)):
        image = imK.array_to_img(popCreatedDecoded[i])
        image.save("ImageBeginning\image" +str(i)+ ".jpg")

    visualInterface(picturesEncoded, decoderModel, popCreated, indexPop, randomseed)#launch the visual interface 



if __name__=="__main__":
    main()  
