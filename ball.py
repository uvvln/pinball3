from vector import Vector, distance
from draw import draw_circle
from shapes import *

GRAVITY_ACC = Vector(0, 0.00001)

class Ball():
    def __init__(self, center, velocity, radius, color):
        self.center = center     #starting point ball
        self.velocity = velocity
        self.radius = radius
        self.t_after_collision = 0.0
        self.color = color

    def intersection(self, shape):
            closest_point = shape.closest_point(self.center)
            if distance(closest_point, self.center) <= self.radius:
                return closest_point
            else:
                return None
    
    def draw(self, screen):
        draw_circle(screen, self.color, self.center, self.radius)

    def update_position(self):
        self.center = self.center +  self.velocity + GRAVITY_ACC * (self.t_after_collision ** 2)
        self.velocity = self.velocity + GRAVITY_ACC * self.t_after_collision
        self.t_after_collision += 1.0

    def collides_with(self, shapes):
        for shape in shapes:
            collision_point = self.intersection(shape)
            if collision_point:
                self.center -= self.velocity  # undo move
                if shape.is_extreme(collision_point):
                    self.velocity = shape.direction.reflect(self.velocity)
                else:
                    orthogonal = (collision_point - self.center).normal()
                    self.velocity = orthogonal.reflect(self.velocity)
                self.velocity = self.velocity * 0.7