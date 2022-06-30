def add(a,b):
    return a+b

import unittest
class SimpleTest(unittest.TestCase):
  
    # Returns True or False. 
    def test(self): 
        result=add(7,4)
        self.assertEqual(result,11)
        

if __name__ == '__main__':
    unittest.main()
