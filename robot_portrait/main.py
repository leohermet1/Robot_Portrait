import decoder 
from auto_encoder import *
from GA import *
from Test_visual_interface import *
from PIL import Image as im
import os


def askWitness():
    #event.listener click
    return 0

def main():
    
    numberOfGen=0
    numberMaxOfGen=10
    
    #encode (only use of the encoder)
    picturesEncoded = decoder.encoded
    randomseed=random()
    popCreated , indexPop = creationPop(picturesEncoded, randomseed) #to take 9 random faces from the clean and reduced database

    initialPop=visualInterface(picturesEncoded)#peut être gérer si jamais on ne sélectionne aucune image

    population=[]
    for i in range (len(initialPop)):
        pos=initialPop[i]-1
        population.append(popCreated[pos])

    completePop=completePopulation(population, picturesEncoded, indexPop, randomseed) # this will be the input of the decoder

    decodedPictures = decoder.decoderFunction(completePop)

    print(decodedPictures)

   

    #os.mkdir("C:\\Users\\mario\\Documents\\GitHub\\Robot_Portrait\\robot_portrait\\ImageUpdated")

    #peut être moyen de tout mettre dans une boucle
    for i in range (len(decodedPictures)):
        image = im.fromarray(np.uint8(decodedPictures[i]))
        image.save("ImageUpdated\image" +str(i)+ ".jpg")

    """image0 = im.fromarray(np.uint8(decodedPictures[0]))
    image0.save("ImageUpdated/image0.jpg")
    image1 = im.fromarray(np.uint8(decodedPictures[1]))
    image1.save("ImageUpdated/image1.jpg")
    image2 = im.fromarray(np.uint8(decodedPictures[2]))
    image2.save("ImageUpdated/image2.jpg")
    image3 = im.fromarray(np.uint8(decodedPictures[3]))
    image3.save("ImageUpdated/image3.jpg")
    image4 = im.fromarray(np.uint8(decodedPictures[4]))
    image4.save("ImageUpdated/image4.jpg")
    image5 = im.fromarray(np.uint8(decodedPictures[5]))
    image5.save("ImageUpdated/image5.jpg")
    image6 = im.fromarray(np.uint8(decodedPictures[6]))
    image6.save("ImageUpdated/image6.jpg")
    image7 = im.fromarray(np.uint8(decodedPictures[7]))
    image7.save("ImageUpdated/image7.jpg")
    image8 = im.fromarray(np.uint8(decodedPictures[8]))
    image8.save("ImageUpdated/image8.jpg")"""


   #removing all pictures, peut être moyen aussi de mettre dans une boucle 
    """os.remove("ImageUpdated/image0.jpg")
    os.remove("ImageUpdated/image1.jpg")
    os.remove("ImageUpdated/image2.jpg")
    os.remove("ImageUpdated/image3.jpg")
    os.remove("ImageUpdated/image4.jpg")
    os.remove("ImageUpdated/image5.jpg")
    os.remove("ImageUpdated/image6.jpg")
    os.remove("ImageUpdated/image7.jpg")
    os.remove("ImageUpdated/image8.jpg")"""



    #show_celebA_data(decodedPictures, title="reconstructed")
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