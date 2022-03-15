# Imports
from base64 import encode
from pickle import NONE
from random import *
import numpy as np
import math
from math import ceil
from PIL import Image 

# Initialisation population
def creationPop(encodedVectors, choosenSeed) :
    '''
    Returns a numpy array of the 9 random vectors among which the witness will have to choose the first time

            Parameters:
                    encodedVectors (numpy.array) : Numpy array of vectors corresponding to the encoded pictures from the databse

            Returns:
                    population (numpy.array): Numpy array of the 9 random vectors that are will be displayed to the witness for the first choice 
    '''
    #we choose at random 9 faces in the entire database 
    population=np.zeros((9,len(encodedVectors[0])))
    print()
    print("len(encodedVectors[0]")
    print(len(encodedVectors[0]))
    print()
    print()
    print("len(encodedVectors")
    print(len(encodedVectors))
    print()
    index =[] 

    for i in range (0,9): 
        seed(choosenSeed)
        randomIndex = randint(0,len(encodedVectors)-1)
        print(randomIndex)
        if (i!=0):
            seed(choosenSeed)
            while (randomIndex in index):
                randomIndex = randint(0,len(encodedVectors)-1)
            
            population[i]=encodedVectors[randomIndex]
            index.append(randomIndex) 
        else :
            population[i]=encodedVectors[randomIndex]
            index.append(randomIndex)
    
    return population, index

def popInitiale(): 
   # popInitiale = creationPop()
    #listen on what the witness clicks
    #at least 3 pictures, if he cannot select 3 pictures, there is a refresh button on which he can click to aks for new faces
    #if he takes more than 3 faces, we can ask him to rate each picture between 1 and the number of pictures
    #button ok when he is done selecting the pictures
    #button "it's him" when the witness recognizes the face
    #popInitiale=faces he chose
    popInitiale = 0
    return popInitiale

# Population costs function
def populationCostFunction():
    #either it's only 3 pictures and then they are all at the same cost (one)
    #or it's ordered with the grades
    costPop =0
    return costPop


# Crossing over 
def crossingOver(population):#vector of vector with the selected faces
    '''
    Returns a numpy array of the 6 crossed vectors 

            Parameters:
                    population (numpy.array) : Numpy array of vectors corresponding to the pictures that the witness chose

            Returns:
                    new_pop (numpy.array): Numpy array of the 6 vectors that are created by crossing the 3 first vectors of the population 
    '''
    #popInitial ordered with the faces
    #crossing over on the 3 best faces
    #returns the population that will be undergo mutation
    #if exactly 3 faces: the returned population is composed of the crossed faces and of the original ones
    #if more, only the crossed one and the others (less good)

    taille=len(population[0])
    half=math.ceil(taille/2)
    new_pop=np.zeros((6,len(population[0])))
    
    new_pop[0]=np.concatenate((population[0][0:half],population[1][half:]),axis=None)
    new_pop[1]=np.concatenate((population[1][0:half],population[0][half:]),axis=None)
    new_pop[2]=np.concatenate((population[1][0:half],population[2][half:]),axis=None)
    new_pop[3]=np.concatenate((population[2][0:half],population[1][half:]),axis=None)
    new_pop[4]=np.concatenate((population[0][0:half],population[2][half:]),axis=None)
    new_pop[5]=np.concatenate((population[2][0:half],population[0][half:]),axis=None)

    return new_pop

# Mutation function
def mutationFunction(population, choosenSeed):
    '''
    Returns a numpy array of the vectors mutated 

            Parameters:
                    population (numpy.array) : Numpy array of vectors corresponding to the pictures that the witness chose

            Returns:
                    popToMutate (numpy.array): Numpy array of vectors who may have undergone a mutation
    '''
        
    #using the population that underwent CO
    #if more than 3 faces: we mutate the one that didn't undergo CO
    #if exactly 3 faces: we mutate the 3 original ones
    #maybe try to mutate in an interval for each pixel defined by the faces chosen (from the best to the worst)
    #or/and take the average
    
    nbDePopToMute=0
    taille3=True
    if(len(population)==3):
        nbDePopToMute=3
    else:
        nbDePopToMute=len(population)-3
        taille3=False


    popToMutate=np.zeros((nbDePopToMute, len(population[0])))

    if(taille3):
        popToMutate[0]=population[0]
        popToMutate[1]=population[1]
        popToMutate[2]=population[2]

    else:
        j=0
        for i in range (3, 3 + nbDePopToMute):

            popToMutate[j]=population[i]
            j=j+1
    beginningMut2 = 0
    seed(choosenSeed)#uncomment for unitary test
    probaMut1 = random()
    if(probaMut1<0.99) and (nbDePopToMute>1):#if random <0.3 then the mutation appears and we need more than one vector to make a mean 
        popToMutate[0] = np.mean(popToMutate,axis=0)
        beginningMut2 = 1 #Thus the vector 0 will not be modified by the mutation 2  
    for i in range (beginningMut2,len(popToMutate)):
        for j in range(len(popToMutate[0])):
            seed(choosenSeed)#uncomment for unitary test
            value=random()#between 0 and 1
            if(value<0.5):#if random <0.5 then the mutation appears
                popToMutate[i][j] = uniform(1.0,100.0)            
    return popToMutate

#to recreate a good population
def completePopulation(population, encodedVectors, index, randomSeed):
    '''
    Returns a numpy array of the new population composed of the mutated vectors, the 6 crossed ones and potentially some other vectors from the database 

            Parameters:
                    population (numpy.array) : Numpy array of vectors corresponding to the pictures that the witness chose

            Returns:
                    populationToBeShown (numpy.array): Numpy array of "children" vectors that can be either crossed from the parents, mutated or taken from the database
    '''
    #checks if there are 9 faces
    #if not, adds faces from the db but close to the one selected
    populationToBeShown=np.zeros((9, len(population[0])))
    crossed_pop=crossingOver(population)
    mutatedPop=mutationFunction(population, randomSeed)
    for i in range(len(populationToBeShown)):
        if(i<len(crossed_pop)):
            populationToBeShown[i]=crossed_pop[i]
        elif((len(crossed_pop)<=i) and (i<(len(mutatedPop)+len(crossed_pop)))):
            populationToBeShown[i]=mutatedPop[i-6]
        elif(i>=(len(crossed_pop)+len(mutatedPop))):
            randomIndex = randint(0,len(encodedVectors)-1)
            while (randomIndex in index):
                randomIndex = randint(0,len(encodedVectors)-1)
           
            populationToBeShown[i]=encodedVectors[randomIndex]
            index.append(randomIndex)    

    return populationToBeShown

# Main loop

#creationPop() #data 9 faces at random
#popInitiale() #reduced database with the faces choosen by the witness


def main_genetic_algorithm ():

    population=[[0, 1, 2, 3, 4, 5, 6,7], [7,6, 5, 4, 3, 2, 1, 0], [6,7, 8, 9, 10, 11, 12, 0], [0, 3, 5, 7, 9, 11, 13, 15]] 
    
    #crossed_pop=crossingOver(population)
    #mutatedPop=mutationFunction(population)

    randomseed=random()
    popFinale=completePopulation(population)

    for i in range (len(popFinale)):
        for j in range (len(popFinale[i])):
            print(popFinale[i][j])
        print()

    #mutationFunction() 
if __name__=="__main__":
    main_genetic_algorithm()  
