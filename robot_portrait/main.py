#main

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
    creationPop()#to take 9 random faces from the clean and reduced database
    #decode to show the pictures selected
    askWitness()#Visual interface 
    popInitiale()#to create our intial population
    

    for numberOfGen in range(0, numberMaxOfGen):
        #call GA
        #generate a new population = create new vectors based on the selected faces
        #decode to show to the witness
        #call visual interface
        #choice between 9 faces ( the created one and potentially some original one = extracted from the db)
