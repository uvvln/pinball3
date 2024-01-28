import pygame
from menu import *
from vector import *
from ball import Ball
import shape_setups
from shapes import *


class Game():
    def __init__(self, shape_setup):
        pygame.init()
        self.create_Game(shape_setup)
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.RIGHT_KEY, self.RIGHT_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False, False
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        pygame.display.set_caption("Scuffed Pinball")
        self.font_name = pygame.font.get_default_font()
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.clock = pygame.time.Clock()
        

    def game_loop(self):

        while self.playing:
            
            self.check_events()
            self.updateElements()
            self.draw()

            pygame.display.update()
            self.reset_keys()

    def create_Game(self, setup):
        self.DISPLAY_W = setup['size']['width']
        self.DISPLAY_H = setup['size']['height']

        walls = shapes_from_rectangle(1, 1, self.DISPLAY_W - 2, self.DISPLAY_H - 2, 'green')

        # create a list with all obstacles in the game (walls and other shapes)
        self.shapes = walls
        for obstacle in setup['obstacles']:
            self.shapes.append(Shape(
                            Vector(*obstacle['from']),
                            Vector(*obstacle['to']),
                            'green'
                            )
            )
        
        # TODO: paddles
            
        # create Ball
        self.balls = [Ball(
            Vector(*setup['ball']['position']),
            Vector(*setup['ball']['velocity']),
            setup['ball']['radius'],
            setup['ball']['color']
            )]

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                    

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, 'white')
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw(self):
        self.window.blit(self.display, (0,0))   #switch surface
        self.display.fill('black')

        for shape in self.shapes:
            shape.draw(self.display)
        
        for ball in self.balls:
            ball.draw(self.display)

        pygame.display.flip()
    
    def updateElements(self):

        if self.BACK_KEY:       #solange kein andere art das game zu beenden existiert
                self.playing= False
        
        #for shape in self.shapes:       # später: auch andere shapes können geschwindigkeit haben -> müssen auch geupdated werden
        for ball in self.balls:
            ball.update_position()
            ball.collides_with(self.shapes)

