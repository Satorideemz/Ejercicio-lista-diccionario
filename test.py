


import unittest
from ListaDiccionario import repetidos

class Testdiccionario(unittest.TestCase):
   def testdiccionario_1(self):
       resultado = repetidos([2, 6, 1, 4, 1,  7, 2, 5, 9, 7])

       self.assertEqual(resultado, {2: 2, 6: 1, 1: 2, 4: 1, 7: 2, 5: 1, 9: 1})

   def testdiccionario_2(self):
       self.assertEqual(repetidos([4, 7, 1]), {4: 1, 7: 1, 1: 1})

   def testdiccionario_3(self):
       self.assertEqual(repetidos([7, 5, 7, 9, 5, 9, 1, 9, 8, 1]), {7: 2, 5: 2, 9: 3, 1: 2, 8: 1})

   def testdiccionario_4(self):
       self.assertEqual(repetidos([4, 2, 3, 1, 8, 9, 4, 7]), {4: 2, 2: 1, 3: 1, 1: 1, 8: 1, 9: 1, 7: 1})

   def testdiccionario_5(self):
       self.assertEqual(repetidos([9, 5, 1, 5, 9, 9]), {9: 3, 5: 2, 1: 1})

if __name__ == '__main__':
    unittest.main()