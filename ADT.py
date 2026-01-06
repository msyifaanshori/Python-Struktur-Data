class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def tranlate(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

    def midpoint(self, other):
        return Point2D((self.x + other.x)/2, (self.y + other.y)/2)

p1 = Point2D(1, 2)
p2 = Point2D(3, 4)
print(p1)
print(p2)
p1.tranlate(1, 1)
print(p1)
print(p1.distance(p2))
print(p1.midpoint(p2))

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def kali(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def bandingkan(self, other):
        return self.numerator * other.denominator > self.denominator * other.numerator

r1 = Rational(3, 4)
r2 = Rational(2, 4)
print(r1)
print(r2)
print(r1.kali(r2))
print(r1.bandingkan(r2))
