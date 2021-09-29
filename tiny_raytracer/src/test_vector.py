import unittest

from vector import Vector


class VectorTests(unittest.TestCase):
    def setUp(self):
        self.a = Vector(1.0, 1.0, 1.0)
        self.b = Vector(3.0, 4.0, 5.0)

    def test_addition(self):
        c = self.a + self.b
        self.assertEqual(c, Vector(4.0, 5.0, 6.0))
    
    def test_cross_product(self):
        c = self.a.cross(self.b)
        self.assertEqual(c, Vector(1, -2, 1))

    def test_getitem(self):
        self.assertEqual(self.a[0], 1.0)
        self.assertEqual(self.a[1], 1.0)
        self.assertEqual(self.a[2], 1.0)

        self.assertEqual(self.b[0], 3.0)
        self.assertEqual(self.b[1], 4.0)
        self.assertEqual(self.b[2], 5.0)

    def test_additive_inverse(self):
        self.assertEqual(-self.a, Vector(-1.0, -1.0, -1.0))

    def test_scalar_multiplication(self):
        c = self.a * 3
        self.assertEqual(c, Vector(3.0, 3.0, 3.0))
        c = 3 * self.a
        self.assertEqual(c, Vector(3.0, 3.0, 3.0))




unittest.main()
