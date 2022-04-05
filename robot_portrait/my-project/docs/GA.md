# Genetic Algorithm

## Functions

* `createPop` - Create a population taking 9 random faces from the database.

Takes as parameters:

    - encodedVectors (numpy.array) : Numpy array of vectors corresponding to the encoded pictures from the database
    - X_test(numpy.array) : Numpy array of the pictures of the testing part

Returns:

    - population (numpy.array): Numpy array of the 9 random vectors that are will be displayed to the witness for the first choice 


* `crossingOver` - Take the 3 first choosen pictures and merge the top of one of them with the bottom of the other one.

Takes as parameters:

    - population (numpy.array) : Numpy array of vectors corresponding to the pictures that the witness chose

Returns:

    - new_pop (numpy.array): Numpy array of the 6 vectors that are created by crossing the 3 first vectors of the population 


* `mutationFunction` - Mutate the choosen pictures in a range.

Takes as parameters:

    - population (numpy.array) : Numpy array of vectors corresponding to the pictures that the witness chose

Returns:
                    
    - popToMutate (numpy.array): Numpy array of vectors who may have undergone a mutation

* `completePop` - Using the crossed and mutated pictures, generate a new population with if needed pictures from the databse.

Takes as parameters:

    - population (numpy.array) : Numpy array of vectors corresponding to the pictures that the witness chose

Returns:
    - populationToBeShown (numpy.array): Numpy array of "children" vectors that can be either crossed from the parents, mutated or taken from the database