from encoder import *
from GA import *
from Test_visual_interface import *


def askWitness():
    #event.listener click
    return 0

def main():
    
    numberOfGen=0
    numberMaxOfGen=10
    
    #encode (only use of the encoder)
    picturesEncoded = encoder()
    popCreated, indexPop = creationPop(picturesEncoded) #to take 9 random faces from the clean and reduced database
    #print(popCreated)
    #print()
    initialPop=visualInterface(picturesEncoded)
    #print(initialPop)
    population=[]
    for i in range (len(initialPop)):
        pos=initialPop[i]-1
        population.append(popCreated[pos])
    #print()
    #print(population)
    #print()
    completePop=completePopulation(population, picturesEncoded, indexPop)#this willbe the input of the decoder
    #print()
    print(completePop)
    decoder()
   
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