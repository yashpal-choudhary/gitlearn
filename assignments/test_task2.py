'''
Unit testing for task 2
'''

import unittest
from task2 import Task


class test_task1(unittest.TestCase):

    def test_main(self):
        self.assertEqual(Task(2).main(), [1, 1])
        self.assertEqual(Task(5).main(), [1, 1, 2, 3, 5])
        self.assertEqual(Task(10).main(), [
            1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(Task(20).main(), [
            1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765])


if __name__ == '__main__':
    unittest.main()
