# autoencoder

## functions

* `get_pictures` - Returns a numpy array of the pixels of all the pictures.

Takes as parameters:

    - file_str(string) : String of the directory towards the file containing all the celebA pictures
Returns:

    - celebA (numpy.array): Numpy array of the pixels of each picture in the file


* `creat_train_data` - Returns the training part and the testing part of data of the pictures which will be used to train the model after.

Takes as parameters:

    - celebA (numpy.array) : Numpy array of the pixels of each picture in the file.

Returns:

    - X_train (numpy.array): Numpy array of the pictures of the training part
    - X_test (numpy.array): Numpy array of the pictures of the testing part

* `get_models` - Returns the autoencoder and decoder model (dercoder model with the same layers with that of autoencoder)

Takes as parameters:

    - None

Returns:

    - X_d ,X_AE (model) : autoencoder and decoder model

* `train_autoencoder_model` - Returns the trained autoencoder with our pictures

Takes as parameters:

    - X_train (numpy.array) : Numpy array of the pictures of the training part
    - X_test(numpy.array) : Numpy array of the pictures of the testing part

Returns:

    - X_AE (model) : trained autoencoder (decoder is trained automatically within the training of autoencoder) 


* `auto_encoder` - Returns the encoded pictures and the decoded pictures with the models

Takes as parameters:

    - None

Returns:

    - encoded(numpy.array) : Numpy array of the pixels of the encoded pictures  
    - reconstructed(numpy.array) : Numpy array of the pixels of the decoded pictures