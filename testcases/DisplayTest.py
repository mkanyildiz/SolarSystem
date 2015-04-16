from docutils.utils.roman import OutOfRangeError
from dynamic.Display import Sonnensystem

__author__ = 'Muhammed5'

import unittest

class DisplayTest(unittest.TestCase):

    def setUp(self):
        self.p1 = Sonnensystem()
        pass

    def tearDown(self):
        del self.p1
        pass

    def testMain(self):
        self.assertRaises(TypeError, lambda: self.p1.main("xy",
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]]
                                                  ,[[2.5,1.68],[2,5],[0.2,0.1]]))

    def testMainNull(self):
        self.assertRaises(ZeroDivisionError, self.p1.main(0,
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testMainNeg(self):
        self.assertRaises(ZeroDivisionError, self.p1.main(-3,
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]]
                                                  ,[[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetAnz(self):
        self.assertRaises(ZeroDivisionError, lambda: self.p1.main(5,
                                                          [0,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                                                          [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                                                  ["",[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetSizeString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],["",""]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetSizeNull(self):
        self.assertRaises(ZeroDivisionError, lambda: self.p1.main(5,
                                                  [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0,0]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))
    def testPlanetAbstandString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                                                  [2,["",""],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[1,1]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetSpeedString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                                                  [2,[1,1],["",""],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[1,1]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetMondeString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                                                  [2,[1,1],[1,1],["./textures/erde.jpg","./textures/merkur.jpg"],["",""],[1,1]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testPlanetMondeOutOfRange(self):
        self.assertRaises(OutOfRangeError, lambda: self.p1.main(5,
                                                  [2,[1,1],[1,1],["./textures/erde.jpg","./textures/merkur.jpg"],[-3,-3],[1,1]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))
    def testPlanetTextureInt(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                                                  [2,[10.7,16.3],[2,5],[1,1],[1,2],[1,1]],
                                                  [[2.5,1.68],[2,5],[0.2,0.1]]))

    def testMoonSizeString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                    [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                    [[2.5,1.68],[2,5],["",""]]))

    def testMoonSizeNull(self):
        self.assertRaises(ZeroDivisionError, lambda: self.p1.main(5,
                    [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                    [[2.5,1.68],[2,5],[0,0]]))


    def testMoonDistanzString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                    [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                    [["",""],[2,5],[1,1]]))
    def testMoonSpeedString(self):
        self.assertRaises(TypeError, lambda: self.p1.main(5,
                    [2,[10.7,16.3],[2,5],["./textures/erde.jpg","./textures/merkur.jpg"],[1,2],[0.91,0.49]],
                    [[1,1],["",""],[1,1]]))

    def testOk(self):
        self.assertRaises(SystemExit, lambda:self.p1.main(5,
        [3,[10.7,16.3,25],[2,5,3],["./textures/erde.jpg","./textures/merkur.jpg","./textures/erde.jpg"],[1,2,2],[0.91,0.49,2]],
        [[2.5,1.68,1],[2,5,3],[0.2,0.1,0.1]]))

if __name__ == '__main__':
    unittest.main()