# Visual Interface

## Functions


* `visualInterface` - This function permits to define a dynamic graphical interface and to show it. 

Takes as parameters:

    - encodedVectors (numpy.array) : Numpy array of vectors corresponding to the encoded pictures from the database
    - decoderModel (keras model) : Model previously trained to decode images 
    - popCreated (numpy.array) : Numpy array of vectors corresponding to the 9 encoded pictures choosen from the database at random
    - indexPop (numpy.array) : Numpy array of values corresponding to the index of the images choosen from the database
    - randomseed (float) : Float number to fix a seed for random numbers in order to be reproductible for the unitary test

Returns: 

    - None        

* `popCreatedInsideFunction` - This function permits to create the population that is created at the beginning and to update it in case of refresh

Takes as parameters:

    - popCreatedGiven (numpy.array) : Numpy array of vectors corresponding to the encoded pictures

Returns: 

    - None



* `CreationPopUsed` - This function permits to know if the initial population was already use or not, usefull at the beginning and at each call of the refresh button

Takes as parameters:

    - popCreatedUsed (numpy.array) : Numpy array of vectors corresponding to the encoded pictures
                
Returns: 

    - boolean value depending on the case 

* `refreshFunction` - This function permits to define the new 9 pictures that will be put on the graphical interface after the click on the button Refresh

Takes as parameters:

    - encodedVectors (numpy.array) : Numpy array of vectors corresponding to the encoded pictures from the database

Returns: 
    - None        

* `update_image` - This function permits to define the action of the refresh button : it put 9 new pictures on the graphical interface.

Takes as parameters:

    - event (event) : Action collected when the button is clicked #à vérifier

Returns:
    - None 


* `FunctionimageToShow2` - This function permits to update the canvas with the new pictures, so that the pictures don't get garbage collected

Takes as parameters:

    - imageToShow2 (numpy.array) : Numpy array corresponding to the images that will be put in the canvas

Returns:  

    -None

* `defineCompletePop` - This function permits to be able to access and update completePop (to avoid again the garbage collection event)

Takes as parameters:
                        
    - population (numpy.array) : Numpy array of vectors corresponding to the encoded pictures from the database
    - encodedVectors (numpy.array) : Numpy array of vectors corresponding to the encoded pictures from the database
    - indexPop (numpy.array) : Numpy array of values corresponding to the index of the images choosen from the database
    - randomseed (float) : Float number to fix a seed for random numbers in order to be reproductible for the unitary test
    - completePop (numpy.array) : Numpy array of vectors 
                
Returns: 

    - None

* `launchGA` - This function permits to launch the genetic algorithm

Takes as parameters:
    
    - event (event) : Action collected when the button is clicked#à vérifier

Returns:         

    -None