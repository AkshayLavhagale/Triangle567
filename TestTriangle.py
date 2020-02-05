# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def test_input(self):
        # This function will check whether all the data points are present in correct format or not
        with self.assertRaises(ValueError):
            classifyTriangle("Akshay", 1, 2)
            classifyTriangle("a", "b", "c")
            classifyTriangle("A", "B", "C")

    def test_equilateral(self):
        # This function will tell us whether the triangle is equilateral triangle or not
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 is an equilateral')
        self.assertNotEqual(classifyTriangle(3, 3, 12), 'Equilateral', '3,3,12 is an isosceles')
        self.assertEqual(classifyTriangle(15.5, 15.5, 15.5), 'Equilateral', '15.5, 15.5, 15.5 is an equilateral')

    def test_isosceles(self):
        # This function will tell us whether the triangle is isosceles triangle or not
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles', '2, 2, 3 is an isosceles triangle')
        self.assertEqual(classifyTriangle(12, 13, 12), 'Isosceles', '12, 13, 12 is an isosceles triangle')
        self.assertEqual(classifyTriangle(10, 10, 8), 'Isosceles', '10, 10, 8 is an isosceles triangle')
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Isosceles', '10, 10, 10 should be Equilateral')

    def test_scalene(self):
        # This function will tell us whether the triangle is scalene triangle or not
        self.assertEqual(classifyTriangle(10, 20, 12), 'Scalene', '10, 20, 12 is a scalene triangle')
        self.assertNotEqual(classifyTriangle(10, 10, 3), 'Scalene', '10, 10, 3 is an isosceles triangle')

    def test_isosceles_right(self):
        pass
        # This function will tell us whether the triangle is isosceles and right triangle or not
        # self.assertEqual(classifyTriangle(2, 2, 2.828), 'Isosceles and Right Triangle',
        # '2, 2, 2.828 is an isosceles and right triangle')

    def test_scalene_right(self):
        # This function will tell us whether the triangle is scalene and right triangle or not
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right and Scalene Triangle',
                         '3, 4, 5 is a scalene and right Triangle')

    def test_not_triangle(self):
        # This function will tell us whether this is triangle or not
        # self.assertEqual(classifyTriangle(1, 1, 3), 'This is not a triangle', '1, 1, 3 is not a triangle')
        self.assertEqual(classifyTriangle(15.5, 15.5, -15.5), 'This is not a triangle',
                         '15.5, 15.5, -15.5 is not a triangle')
        self.assertEqual(classifyTriangle(0, 0, 0), 'This is not a triangle', '0, 0, 0 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

