from tiny_raytracer.src.vector import Vector


def tests():
    a = Vector(1, 0, 0)
    b = Vector(2, 1, 1)
    c = Vector(3, 4, 5)

    assert a == Vector(1, 0, 0)

    res1 = 2 * b
    res2 = b * 2

    assert res1 == Vector(4, 2, 2)
    assert res1 == res2

    assert -b == Vector(-2, -1, -1)
    assert b == Vector(2, 1, 1)

    n = a.normalize()

    assert n.norm() == 1.0

    assert a.dot(c) == c.dot(a)

    assert b.cross(c) == Vector(1, -7, 5)
    assert c.cross(b) == -b.cross(c)

    assert a + b == Vector(3, 1, 1)

    d = Vector(1, 2, 3, 4)
    e = d * 2
    assert e == Vector(2, 4, 6, 8)
    assert e / 2 == d


tests()
