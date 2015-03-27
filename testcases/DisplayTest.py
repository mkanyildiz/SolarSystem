from dynamic.Display import Sonnensystem

__author__ = 'Muhammed5'
__author__ = '$USER'

import unittest

class TestDosplay(unittest.TestCase):

    def setUp(self):
        self.p1 = Sonnensystem
        pass

    def tearDown(self):
        del self.p1
        pass

    def testMain(self):
        self.assertRaises(TypeError, self.p1.main)

if __name__ == '__main__':
    unittest.main()