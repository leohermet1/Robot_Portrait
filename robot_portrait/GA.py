# Imports
import numpy as np
from PIL import Image 

imgHomme = Image.open('homme.jpg')
pixelImageH= np.asarray(imgHomme)
imgFemme = Image.open('femme.jpg')
pixelImageF= np.asarray(imgFemme) 

# Initialisation population
def creationPop() : 
    #we choose at random 9 faces in the entire database 

    imgHomme = Image.open('homme.jpg')
    pixelImageH= np.asarray(imgHomme)
    imgFemme = Image.open('femme.jpg')
    pixelImageF= np.asarray(imgFemme) 

    population = [pixelImageH,pixelImageF]

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
def crossingOver():
    #popInitial ordered with the faces
    #crossing over on the 3 best faces
    #returns the population that will be undergo mutation
    #if exactly 3 faces: the returned population is composed of the crossed faces and of the original ones
    #if more, only the crossed one and the others (less good)
    new_P=0
    return new_P 

# Mutation function
def mutationFunction():
    #using the population that underwent CO
    #if more than 3 faces: we mutate the one that didn't undergo CO
    #if exactly 3 faces: we mutate the 3 original ones
    #maybe try to mutate in an interval for each pixel defined by the faces chosen (from the best to the worst)
    #or/and take the average
    mutatedPop = 0              
    return mutatedPop

#to recreate a good population
def completePopulation():
    #checks if there are 9 faces
    #if not, adds faces from the db but close to the one selected
    populationToBeShown=0
    return populationToBeShown

# Main loop

creationPop() #data 20 faces at random
popInitiale() #reduced database with the faces choosen by the witness
#We ask for the 2 best
best1 = pixelImageH
best2 = pixelImageF

def main_genetic_algorithm ():
    crossingOver()
    mutationFunction()  
