'''
Unit testing for task 3
'''

import unittest
from task3 import Task


class test_task1(unittest.TestCase):

    def test_main(self):
        self.assertEqual(Task('quick fox lazy dog quick donkey fire fox').main(), {
                         'quick': 2, 'fox': 2, 'lazy': 1, 'dog': 1, 'donkey': 1, 'fire': 1})
        self.assertEqual(Task('She was young the way an actual young person is young').main(), {
                         'she': 1, 'was': 1, 'young': 3, 'the': 1, 'way': 1, 'an': 1, 'actual': 1, 'person': 1, 'is': 1})
        self.assertEqual(Task('Almost nothing was more annoying than having our Wasted time wasted on something not worth wasting it on').main(),
                         {'almost': 1, 'nothing': 1, 'was': 1, 'more': 1, 'annoying': 1, 'than': 1, 'having': 1, 'our': 1, 'wasted': 2, 'time': 1, 'on': 2, 'something': 1, 'not': 1, 'worth': 1, 'wasting': 1, 'it': 1})
        self.assertEqual(Task('I felt happy because I saw the others were happy and because I knew I should feel happy, but I wasn’t really happy').main(),
                         {'i': 5, 'felt': 1, 'happy': 3, 'because': 2, 'saw': 1, 'the': 1, 'others': 1, 'were': 1, 'and': 1, 'knew': 1, 'should': 1, 'feel': 1, 'happy,': 1, 'but': 1, 'wasn’t': 1, 'really': 1})


if __name__ == '__main__':
    unittest.main()
