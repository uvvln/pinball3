import math

# relative distance of two vectors
def distance(v1, v2):
    return (v1 - v2).length()


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # operator-overload: addition of two vectors
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # operator-overload: subtraction of two vectors
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # operator-overload: multiplication with scalar or other vector
    def __mul__(self, other):
        if isinstance(other, Vector):   # with vector
            return self.x * other.x + self.y * other.y
        else:   #with scalar
            return Vector(self.x * other, self.y * other)

    def rotate_around(self, center, angle):
        t = self - center
        return center + \
            Vector(
                t.x * math.cos(angle) - t.y * math.sin(angle),
                t.x * math.sin(angle) + t.y * math.cos(angle)
            )

    # returns the vector with its arguments as integer type
    def int(self):
        return Vector(int(self.x), int(self.y))

    # returns [x, y] - form
    def tuple(self):
        return self.x, self.y

    # returns length of vector "sqrt(x ** 2 + y ** 2)"
    def length(self):
        return math.hypot(self.x, self.y)

    # 
    def projected_length(self, v):
        return (v * self) / self.length()
    
    # tranforms vector in unit vector
    def normalized(self):
        l = self.length()
        return Vector(self.x / l, self.y / l)

    # returns a unit vector which is perpendicular to original one
    def normal(self):
        return Vector(-self.y, self.x).normalized()

    def __str__(self):
        return "[" + str(self.x) + ", " + str(self.y) + "]"

    def reflect(self, other):
        assert abs(self.length() - 1.) < 0.00001
        dot = self * other
        return self * dot * 2 - other