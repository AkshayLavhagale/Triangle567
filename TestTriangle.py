# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle_Fixed import classifyTriangle


class TestTriangles(unittest.TestCase):
    # This class will test all the triangle specification and classify them as per their characteristics.
    def test_input(self):
        # This function will check whether all the data points are present in correct format or not
        self.assertEqual(classifyTriangle("Akshay", 1, 2), 'InvalidInput', '"Akshay", 1, 2 is an InvalidInput')
        self.assertEqual(classifyTriangle("a", "b", "c"), 'InvalidInput', '"a", "b", "c", 1, 2 is an InvalidInput')
        self.assertEqual(classifyTriangle("A", "B", "C"), 'InvalidInput', '"A", "B", "C", 1, 2 is an InvalidInput')

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
        self.assertEqual(classifyTriangle(3, 3, 3.000000000000001), 'Isosceles')

    def test_scalene(self):
        # This function will tell us whether the triangle is scalene triangle or not
        self.assertEqual(classifyTriangle(10, 20, 12), 'Scalene', '10, 20, 12 is a scalene triangle')
        self.assertNotEqual(classifyTriangle(10, 10, 3), 'Scalene', '10, 10, 3 is an isosceles triangle')

    def test_isosceles_right(self):
        # This function will tell us whether the triangle is isosceles and right triangle or not
        self.assertEqual(classifyTriangle(2, 2, 2.828), 'Right Isosceles',
                         '2, 2, 2.828 is an isosceles and right triangle')
        self.assertEqual(classifyTriangle(3, 3, 4.242640687119285146), 'Right Isosceles')
        self.assertEqual(classifyTriangle(1, 1, 2 ** 0.5), 'Right Isosceles')

    def test_scalene_right(self):
        # This function will tell us whether the triangle is scalene and right triangle or not
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right Scalene',
                         '3, 4, 5 is a scalene and right Triangle')
        self.assertEqual(classifyTriangle(3, 5, 4), 'Right Scalene')


    def test_not_triangle(self):
        # This function will tell us whether this is triangle or not
        self.assertEqual(classifyTriangle(1, 1, 3), 'NotATriangle', '1, 1, 3 is not a triangle')
        self.assertEqual(classifyTriangle(15.5, 15.5, -15.5), 'InvalidInput',
                         '15.5, 15.5, -15.5 is InvalidInput')
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0, 0, 0 is InvalidInput')
        self.assertEqual(classifyTriangle(3000, 3000, 4000), 'InvalidInput', '0, 0, 0 is InvalidInput')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
