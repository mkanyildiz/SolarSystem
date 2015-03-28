from Display import Sonnensystem

__author__ = 'Muhammed5'

import unittest

class TestDosplay(unittest.TestCase):

    def setUp(self):
        self.p1 = Sonnensystem()
        pass

    def tearDown(self):
        del self.p1
        pass

    def testMain(self):
        self.assertRaises(TypeError, self.p1.main("",
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]]
                                                  ,[[2.5,1.68],[2,5],[0.2,0.1]]))

    def testMainFloat(self):
        self.assertRaises(TypeError, self.p1.main(1.5,
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetAnz(self):
        self.assertRaises(ZeroDivisionError, self.p1.main(5,
                                                          [0,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                                                          [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetString(self):
        self.assertRaises(TypeError, self.p1.main(5,
                                                  ["",[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetSizeString(self):
        self.assertRaises(TypeError, self.p1.main(5,
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],["",""]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testMoonSizeString(self):
        self.assertRaises(TypeError, self.p1.main(5,
                    [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                    [[2.5,1.68],[2,5],["",""]]))

    def testMoonSizeNull(self):
        self.assertRaises(TypeError, self.p1.main(5,
                    [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                    [[2.5,1.68],[2,5],[0,0]]))

if __name__ == '__main__':
    unittest.main()