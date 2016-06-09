# coding:utf-8
from unittest import TestCase
from unittest import TestSuite
from unittest import makeSuite
from src.fuga import Fuga


class HogeTest(TestCase):

    def setUp(self):
        print('setUp')

    def test_first(self):
        print('test_first')

    def test_fuga(self):
        fuga = Fuga()
        self.assertTrue(fuga.index())


def suite():
    suite = TestSuite()
    suite.addTests(makeSuite(HogeTest))
    return suite