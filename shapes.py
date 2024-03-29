from vector import Vector
from draw import draw_line, draw_arrow


class Shape:

    def __init__(self, p1, p2, color):
        self.p1 = p1
        self.p2 = p2
        self.diff = p2 - p1
        self.length = self.diff.length()
        self.direction = self.diff.normalized()
        self.color = color

    def draw(self, display):
        draw_line(display, self.p1, self.p2, self.color)
        draw_arrow(display, (self.p1 + self.p2) * 0.5, (self.p1 + self.p2) * 0.5 + self.normal() * 10)

    # returns perpendicular vector
    def normal(self):
        return Vector(self.direction.y, -self.direction.x)

    def closest_point(self, point):
        plength = self.projected_length(point)
        if plength <= 0:
            return self.p1
        elif plength >= self.length:
            return self.p2
        else:
            return self.p1 + self.direction * plength

    def is_extreme(self, point):
        return point == self.p1 or point == self.p2

    def projected_length(self, point):
        return (point - self.p1) * self.direction

    def project(self, point):
        plength = self.projected_length(point)
        if 0 <= plength <= self.length:
            return self.p1 + self.direction * plength
        else:
            return None


def shapes_from_rectangle(x, y, w, h, color):
    corners = \
        [
            Vector(x, y),
            Vector(x + w, y),
            Vector(x + w, y + h),
            Vector(x, y + h)
        ]
    return [
        Shape(corners[0], corners[1], color),
        Shape(corners[1], corners[2], color),
        Shape(corners[2], corners[3], color),
        Shape(corners[3], corners[0], color)
    ]