# Imports
import numpy as np
from PIL import Image 

imgHomme = Image.open('homme.jpg')
pixelImageH= np.asarray(imgHomme)
imgFemme = Image.open('femme.jpg')
pixelImageF= np.asarray(imgFemme) 

# Initialisation population
def creationPop() : 
    #we choose at random 20 faces in the entire database 

    imgHomme = Image.open('homme.jpg')
    pixelImageH= np.asarray(imgHomme)
    imgFemme = Image.open('femme.jpg')
    pixelImageF= np.asarray(imgFemme) 

    population = [pixelImageH,pixelImageF]

    return population

def popInitiale(): 
    popInitiale = creationPop()
    return popInitiale

# Genome cost function
def costFunction():
    individusSortis= 0
    return individusSortis

# Population costs function
def populationCostFunction(): 
    costPop =0
    return costPop

# Selection function
def selectLowestGenomes():
    lowestGenomes = 0 
    return lowestGenomes

# Crossing over 
def crossingOver():
    new_P=0
    return new_P 

# Mutation function
def mutationFunction():
    mutatedPop = 0              
    return mutatedPop


# Main loop

creationPop() #data 20 faces at random
popInitiale() #reduced database with the faces choosen by the witness
#We ask for the 2 best
best1 = pixelImageH
best2 = pixelImageF

def main_genetic_algorithm ():
    crossingOver()
    mutationFunction()  
