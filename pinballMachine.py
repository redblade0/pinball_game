import pygame
import math
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

    
    def drawMachine(self, screen):
        # background
        screen.fill((115, 147, 179))
        THICKNESS = 8
        YELLOW = (255, 255, 0)

        # launcher walls
        pygame.draw.rect(screen, YELLOW, (20, 270, THICKNESS, 380))  # left
        pygame.draw.rect(screen, YELLOW, (50, 320, THICKNESS, 330))  # right

        # right wall
        pygame.draw.rect(screen, YELLOW, (450, 20, THICKNESS, 300))

        # semi-circle
        points = []
        radius = 250
        center_x = 23 + radius        
        center_y = 20 + radius   

        for angle in range(180, 361, 4):
            rad = math.radians(angle)
            x = center_x + radius * math.cos(rad)
            y = center_y + radius * math.sin(rad)
            points.append((int(x), int(y)))

        for i in range(len(points) - 1):
            pygame.draw.line(screen, YELLOW, points[i], points[i + 1], THICKNESS)


    def drawLauncher(self, screen):
        # draw launcher + ball in intial state
        pass
    
    def drawFlippers(self, screen):
        # draw flippers
        pass

    def drawShelves(self, screen):
        # draw shelves, 2 gray things in the picture
        pass

    def drawBigBall(self, screen):
        # draw big ball at the top (purple)
        pass

    def drawSmallBalls(self, screen):
        # draw small balls around the big ball
        pass

    def handle_launcher(self, keys):
        # handles launching the ball at the start
        # launcher_power will increase based on how long the down key is pressed for
        pass

    def handle_left_flipper(self, keys):
        #pygame.draw.rect(screen, (255,255,0), (202.5,520, 60,10)) # left flipper
        # handles the animation for the left flipper
        # is adjusted for the left arrow key is pressed
        pass

    def handle_right_flipper(self, keys):
        #pygame.draw.rect(screen, (255,255,0), (202.5,520, 60,10)) # left flipper
        # handles the animation for the right flipper
        # is adjusted for the right arrow key is pressed
        pass

    # WILL NEED COLLSION CHECKING
    # WILL NEED TO ADD OBSTACLES