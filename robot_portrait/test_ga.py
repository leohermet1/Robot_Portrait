import unittest
import GA
import numpy as np

class test_ga_class(unittest.TestCase):
    import numpy as np

    def test_crossingOver(self):
        population = [[0, 1, 2, 3], [4, 5, 6, 7],[8, 9, 10, 11]] 
        result = GA.crossingOver(population)
        expectedResult = np.array([[0, 1, 6, 7], [4, 5, 2, 3],[4, 5, 10, 11], [8, 9, 6, 7],[0, 1, 10, 11], [8, 9, 2, 3]])
        self.np.testing.assert_array_equal(result,expectedResult)

if __name__ == "__main__":
    unittest.main()