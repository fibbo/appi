import math
import unittest

from vector import Vector


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.vector_a = Vector(1.0, 1.0, 1.0)
        self.vector_b = Vector(3.0, 4.0, 5.0)

    def test_x_prop(self):
        self.assertEqual(self.vector_b.x, 3.0)

    def test_y_prop(self):
        self.assertEqual(self.vector_b.y, 4.0)

    def test_z_prop(self):
        self.assertEqual(self.vector_b.z, 5.0)

    def test_addition(self):
        c = self.vector_a + self.vector_b
        self.assertEqual(c, Vector(4.0, 5.0, 6.0))

    def test_subtraction(self):
        c = self.vector_a - self.vector_b
        self.assertEqual(c, Vector(-2.0, -3.0, -4.0))

    def test_division(self):
        c = self.vector_a / 3
        v = 1 / 3
        self.assertEqual(c, Vector(v, v, v))

    def test_equality(self):
        self.assertNotEqual(self.vector_a, self.vector_b)

    def test_dot_product(self):
        c = self.vector_a.dot(self.vector_b)
        self.assertEqual(c, 12.0)
        c = self.vector_b.dot(self.vector_a)
        self.assertEqual(c, 12.0)

    def test_norm(self):
        c = self.vector_a.norm()
        self.assertEqual(c, math.sqrt(3))

    def test_cross_product(self):
        c = self.vector_a.cross(self.vector_b)
        self.assertEqual(c, Vector(1, -2, 1))

    def test_normalize(self):
        c = self.vector_a.normalize()
        v = 1 / math.sqrt(3)
        self.assertEqual(c, Vector(v, v, v))

    def test_getitem(self):
        self.assertEqual(self.vector_a[0], 1.0)
        self.assertEqual(self.vector_a[1], 1.0)
        self.assertEqual(self.vector_a[2], 1.0)

        self.assertEqual(self.vector_b[0], 3.0)
        self.assertEqual(self.vector_b[1], 4.0)
        self.assertEqual(self.vector_b[2], 5.0)

    def test_additive_inverse(self):
        self.assertEqual(-self.vector_a, Vector(-1.0, -1.0, -1.0))

    def test_scalar_multiplication(self):
        c = self.vector_a * 3
        self.assertEqual(c, Vector(3.0, 3.0, 3.0))
        c = 3 * self.vector_a
        self.assertEqual(c, Vector(3.0, 3.0, 3.0))


if __name__ == "__main__":
    unittest.main()
