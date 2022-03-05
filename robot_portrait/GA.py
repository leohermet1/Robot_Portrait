# Imports
from pickle import NONE
import random
from random import *
import numpy as np
import math
from math import ceil
from PIL import Image 

#imgHomme = Image.open('homme.jpg')
#pixelImageH= np.asarray(imgHomme)
#imgFemme = Image.open('femme.jpg')
#pixelImageF= np.asarray(imgFemme) 

# Initialisation population
def creationPop() : 
    #we choose at random 9 faces in the entire database 

    #population = [pixelImageH,pixelImageF]
    population =0

    return population

def popInitiale(): 
    popInitiale = creationPop()
    #listen on what the witness clicks
    #at least 3 pictures, if he cannot select 3 pictures, there is a refresh button on which he can click to aks for new faces
    #if he takes more than 3 faces, we can ask him to rate each picture between 1 and the number of pictures
    #button ok when he is done selecting the pictures
    #button "it's him" when the witness recognizes the face
    #popInitiale=faces he chose
    return popInitiale

# Genome cost function (suppr)

# Population costs function
def populationCostFunction():
    #either it's only 3 pictures and then they are all at the same cost (one)
    #or it's ordered with the grades
    costPop =0
    return costPop

# Selection function (suppr: the cost relies on the witness, it doesn't need to be computed)

# Crossing over 
def crossingOver(population):#vector of vector with the selected faces
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
def mutationFunction(population):
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

    print(nbDePopToMute)
    print(len(population[0]))
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

    #average=average(population)

    for i in range (len(popToMutate)):
        for j in range(len(popToMutate[0])):
            value=random()#between 0 and 1
            if(value<0.3):#if random <0.3 then the mutation appears
                popToMutate[i][j]=randrange(1,100,1)
                print("mutation occurs")
            #elif(0.3<value<0.5):
            
    return popToMutate

#to recreate a good population
def completePopulation(population):
    #checks if there are 9 faces
    #if not, adds faces from the db but close to the one selected
    populationToBeShown=np.zeros((9, len(population[0])))
    crossed_pop=crossingOver(population)
    mutatedPop=mutationFunction(population)
    for i in range(6+len(mutatedPop)):
        if(i<6):
            populationToBeShown[i]=crossed_pop[i]
        else:
            populationToBeShown[i]=mutatedPop[i-6]


    return populationToBeShown

# Main loop

#creationPop() #data 9 faces at random
#popInitiale() #reduced database with the faces choosen by the witness


def main_genetic_algorithm ():

    population=[[0, 1, 2, 3, 4, 5, 6,7], [7,6, 5, 4, 3, 2, 1, 0], [6,7, 8, 9, 10, 11, 12, 0], [0, 3, 5, 7, 9, 11, 13, 15]] 
    
    #crossed_pop=crossingOver(population)
    #mutatedPop=mutationFunction(population)

    popFinale=completePopulation(population)

    for i in range (len(popFinale)):
        for j in range (len(popFinale[i])):
            print(popFinale[i][j])
        print()

    #mutationFunction() 
if __name__=="__main__":
    main_genetic_algorithm()  
