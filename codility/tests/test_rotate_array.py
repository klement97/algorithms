from unittest import TestCase
from rotate_array import solution


class TestRotateArray(TestCase):
    a = [3, 8, 9, 7, 6]

    def test_solution_k1(self):
        self.assertEqual(
            solution(self.a, 1),
            [6, 3, 8, 9, 7]
        )

    def test_solution_k2(self):
        self.assertEqual(
            solution(self.a, 2),
            [7, 6, 3, 8, 9]
        )

    def test_solution_k3(self):
        self.assertEqual(
            solution(self.a, 3),
            [9, 7, 6, 3, 8]
        )

    def test_solution_k4(self):
        self.assertEqual(
            [8, 9, 7, 6, 3],
            solution(self.a, 4)
        )

    def test_solution_k5(self):
        self.assertEqual(
            solution(self.a, 5),
            self.a
        )
