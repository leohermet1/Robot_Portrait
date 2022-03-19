import tensorflow as tf
import keras
import numpy as np

#load the model
decoder = keras.models.load_model('data/decoder.h5')
#load the encoded vector (numpy.ndarray format)
encoded = np.load("data/encoded.npy")

def decoderFunction(encodedRS):
    #reshape the encoded vector from (100,2048) to (100,16,16,8)
    encodedRS = encodedRS.reshape((len(encodedRS),16,16,8))
    #decode the encoded vector using the load model
    decoded = decoder.predict(encodedRS)
    return decoded