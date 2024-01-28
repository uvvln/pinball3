import pygame


def draw_line(display, p1, p2, color):
    pygame.draw.line(display, color, p1.int().tuple(), p2.int().tuple(), 1)


def draw_arrow(display, p1, p2):
    pygame.draw.line(display, 'red', p1.int().tuple(), p2.int().tuple(), 1)
    draw_circle(display, 'red', p2, 2)


def draw_circle(screen, color, center, radius):
    pygame.draw.circle(screen, color, center.int().tuple(), int(radius))