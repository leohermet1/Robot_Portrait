import unittest
from unittest import mock
import GA
from random import *
import numpy as np

class test_ga_class(unittest.TestCase):
    import numpy as np

    def test_crossingOver(self):
        population = [[0, 1, 2, 3], [4, 5, 6, 7],[8, 9, 10, 11]] 
        result = GA.crossingOver(population)
        expectedResult = np.array([[0, 1, 6, 7], [4, 5, 2, 3],[4, 5, 10, 11], [8, 9, 6, 7],[0, 1, 10, 11], [8, 9, 2, 3]])
        self.np.testing.assert_array_equal(result,expectedResult)

    def test_mutation(self):
        population = [[0, 1, 2, 3], [4, 5, 6, 7],[8, 9, 10, 11]]
        expectedResult=np.zeros((3, 4))
        expectedResult[0]=population[0]
        expectedResult[1]=population[1]
        expectedResult[2]=population[2]

        seed(0.3)
        result=GA.mutationFunction(population)
              
        probaMut1 = random()
        if(probaMut1<0.99):
            expectedResult[0] = [4, 5, 6, 7]
            for i in range (1,len(population)):
                for j in range(len(population[0])):
                    seed(0.3)
                    value=random()#between 0 and 1
                    if(value<0.5):#if random <0.5 then the mutation appears
                        expectedResult[i][j] = uniform(1.0,100.0) 
        self.np.testing.assert_array_equal(result,expectedResult)       


    def test_creationPop(self):

            
        fakeEncodedPictures=np.zeros((20,4))
        for i in range(20):
            for j in range(4):
                fakeEncodedPictures[i][j]=i*j
        result1, result2=GA.creationPop(fakeEncodedPictures)
        #population=np.zeros((9, 4))
        index =[] 
        for i in range (0,9):
            seed(0.3) 
            randomIndex = randint(0,len(fakeEncodedPictures))
            if (i!=0):
                seed(0.3)
                while (randomIndex in index):
                    randomIndex = randint(0,len(fakeEncodedPictures))
            
                #population[i]=fakeEncodedPictures[randomIndex]
                index.append(randomIndex) 
            else :
                #population[i]=fakeEncodedPictures[randomIndex]
                index.append(randomIndex)  
            #result=[result1, result2]
            #expectedResult=[population, index]      
        self.np.testing.assert_array_equal(result2,index)

if __name__ == "__main__":
    unittest.main()