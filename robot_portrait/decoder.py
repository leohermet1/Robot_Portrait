import tensorflow as tf
import keras
import numpy as np

#load the model
decoder = keras.models.load_model('decoder.h5')
#load the encoded vector (numpy.ndarray format)
encoded = np.load("encoded.npy")

def decoderFunction(encodedRS, decoderModel):
    '''
    Returns the decoded pictures with the decoder model

            Parameters:
                    encodedRS (numpy.array) : Numpy array of the modified vectors after genetic algorithm

            Returns:
                    decoded (numpy.array) : Numpy array of the decoded pictures
    '''
    #reshape the encoded vector from (9,2048) to (9,16,16,8)
    encodedRS = encodedRS.reshape((len(encodedRS),16,16,8))
    #decode the encoded vector using the load model
    decoded = decoder.predict(encodedRS)
    return decoded
