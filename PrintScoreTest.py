#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

import task1

class PrintScoreTest(unittest.TestCase):

    def test_print_score(self):
        checkscore = task1.PostalCode().print_code(80, 10)
        self.assertEqual(checkscore, "80-010")

    def test_print_score1(self):
        checkscore1 = task1.PostalCode().print_code(1, 9)
        self.assertEqual(checkscore1, "01-009")

    def test_print_score3(self):
        checkscore2 = task1.PostalCode().print_code(2, 3)
        self.assertNotEqual(checkscore2, "2-3", "Wrong Value!")

if __name__ == '__main__':
    unittest.main()