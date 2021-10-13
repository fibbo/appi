class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"

    def __add__(self, rhs):
        if isinstance(rhs, ComplexNumber):
            result = ComplexNumber(0, 0)
            result.real = self.real + rhs.real
            result.imaginary = self.imaginary + rhs.imaginary
            return result
        elif isinstance(rhs, int):
            result = ComplexNumber(self.real, self.imaginary)
            result.real += rhs
            return result

    def __radd__(self, rhs):
        return self + rhs

    def __mul__(self, rhs):
        # Only supports multiplication with other complex numbers
        result = ComplexNumber(0, 0)
        result.real = self.real * rhs.real + self.imaginary * rhs.imaginary * (-1)
        result.imaginary = self.real * rhs.imaginary + self.imaginary * rhs.real
        return result


a = ComplexNumber(4, 3)
b = ComplexNumber(-1, -7)


c = a + b
print(c)

c = a * b
print(c)
