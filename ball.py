from vector import Vector, distance
from draw import draw_circle


GRAVITY_ACC = Vector(0, 0.00001)

class Ball():
    def __init__(self, center, velocity, radius):
        self.center = center     #starting point ball
        self.velocity = velocity
        self.radius = radius
        self.t_after_collision = 0.0
        self.color = 'red'

    def intersection(self, segment):
            closest_point = segment.closest_point(self.center)
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