#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_normal_list(self):
        list_test = [1, 2, 3, 10]
        self.assertEqual(max_integer(list_test), 10)
        list_test = [230, 555, 2902, 287]
        self.assertEqual(max_integer(list_test), 2902)

    def test_empty(self):
        list_test = []
        self.assertIsNone(max_integer(list_test))

    def test_single(self):
        list_test = [29]
        self.assertEqual(max_integer(list_test), 29)

    def test_with_string(self):
        with self.assertRaises(TypeError):
            list_test2 = [1, "Joe", 3, 10]
            max_integer(list_test2)
        with self.assertRaises(TypeError):
            max_integer(["joe", 4, "5", -6, 9])
        with self.assertRaises(TypeError):
            max_integer(2, 9)

    def test_negatif_number(self):
        list_test = [5, 4, 3, -2, 1]
        list_test2 = [-5, -4, -3, 2, -1]
        list_test3 = [9, 9, -9, -9]
        self.assertEqual(max_integer(list_test), 5)
        self.assertEqual(max_integer(list_test2), 2)
        self.assertEqual(max_integer(list_test3), 9)
