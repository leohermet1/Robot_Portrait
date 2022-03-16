from autoencoder import *
from GA import *
from Test_visual_interface import *


def askWitness():
    #event.listener click
    return 0

def main():
    
    numberOfGen=0
    numberMaxOfGen=10
    
    #encode (only use of the encoder)
    picturesEncoded, picturesReconstructed = encoder()
    randomseed=random()
    popCreated , indexPop = creationPop(picturesEncoded, randomseed) #to take 9 random faces from the clean and reduced database

    initialPop=visualInterface(picturesEncoded)#peut être gérer si jamais on ne sélectionne aucune image

    print()
    print("pop initiale")
    print(initialPop)
    print()

    population=[]
    for i in range (len(initialPop)):
        pos=initialPop[i]-1
        population.append(popCreated[pos])

    completePop=completePopulation(population, picturesEncoded, indexPop, randomseed)#this willbe the input of the decoder

    #decoder()
   
    #decode to show the pictures selected
    askWitness()#launch Visual interface 
    #popInitiale()#to create our intial population
    

   # for numberOfGen in range(0, numberMaxOfGen):
        #call GA
        #generate a new population = create new vectors based on the selected faces
        #decode to show to the witness
        #call visual interface
        #choice between 9 faces ( the created one and potentially some original one = extracted from the db)


if __name__=="__main__":
    main()  