'''
Unit testing for task 1
'''

import unittest
from task1 import Task


class test_task1(unittest.TestCase):

    def test_main(self):
        self.assertEqual(Task(5).main(), [1, 2, 'FIZZ', 4, 'BUZZ'])
        self.assertEqual(Task(10).main(), [
                         1, 2, 'FIZZ', 4, 'BUZZ', 'FIZZ', 7, 8, 'FIZZ', 'BUZZ'])
        self.assertEqual(Task(20).main(), [1, 2, 'FIZZ', 4, 'BUZZ', 'FIZZ', 7, 8,
                         'FIZZ', 'BUZZ', 11, 'FIZZ', 13, 14, 'FIZZBUZZ', 16, 17, 'FIZZ', 19, 'BUZZ'])


if __name__ == '__main__':
    unittest.main()
