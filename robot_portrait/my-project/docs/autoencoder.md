# autoencoder

## functions

* `get_pictures` - Returns a numpy array of the pixels of all the pictures. 
Takes as parameters:
    - file_str(string) : String of the directory towards the file containing all the celebA pictures

* `creat_train_data` - Returns the training part and the testing part of data of the pictures which will be used to train the model after.
Takes as parameters:
    - celebA (numpy.array) : Numpy array of the pixels of each picture in the file.