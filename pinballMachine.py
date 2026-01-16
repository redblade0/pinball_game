import pygame
from ball import Ball
class PinballMachine:        

    def __init__(self, width, height, score):
        self.width = width
        self.height = height
        self.score = 0
        self.gravity = pygame.math.Vector2(0, 0.1)  # simulates gracity
        self.ball = None # used if player gets a high enough score (more balls can spawn in)
        self.obstacles = []
        self.launch_power = 0 # power for when ball is push at start

    def update(self):
        self.ball.vel += self.gravity
        self.ball.update()
        # something to check collisions
    
    def drawPinballMachine(self, screen):
        # draw pinball machine and background
        # draw flippers in start state
        # draw ball in start state
        # draw obstacles
        pass

    def handle_launcher(self, keys):
        # handles launching the ball at the start
        # launcher_power will increase based on how long the down key is pressed for
        pass

    def handle_left_flipper(self, keys):
        pygame.draw.rect(screen, (255,255,0), (202.5,520, 60,10)) # left flipper
        # handles the animation for the left flipper
        # is adjusted for the left arrow key is pressed
        pass

    def handle_right_flipper(self, keys):
        pygame.draw.rect(screen, (255,255,0), (202.5,520, 60,10)) # left flipper
        # handles the animation for the right flipper
        # is adjusted for the right arrow key is pressed
        pass

    # WILL NEED COLLSION CHECKING
    # WILL NEED TO ADD OBSTACLES