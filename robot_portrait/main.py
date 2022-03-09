#main

from encoder import *
from GA import *

def creationPop():#inheritance
    return 0

def popInitiale():#inheritance
    return 0

def askWitness():
    #event.listener click
    return 0

def main():
    
    numberOfGen=0
    numberMaxOfGen=10
    
    #encode (only use of the encoder)
    picturesEncoded = encoder()
    population=[picturesEncoded[0], picturesEncoded[1],picturesEncoded[2],picturesEncoded[3],picturesEncoded[4]]
    completePop=completePopulation(population)#this willbe the input of the decoder
    decoder()
   # creationPop(picturesEncoded)#to take 9 random faces from the clean and reduced database
    #decode to show the pictures selected
    askWitness()#Visual interface 
    popInitiale()#to create our intial population
    

   # for numberOfGen in range(0, numberMaxOfGen):
        #call GA
        #generate a new population = create new vectors based on the selected faces
        #decode to show to the witness
        #call visual interface
        #choice between 9 faces ( the created one and potentially some original one = extracted from the db)


if __name__=="__main__":
    main()  