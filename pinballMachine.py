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
        self.drawMachine(screen)
        self.drawSmallBalls(screen)
        self.drawBigBall(screen)
        self.drawFlippers(screen)
        self.drawLauncher(screen)

    
    def drawMachine(self, screen):
        # background
        screen.fill((115, 147, 179))
        THICKNESS = 8
        YELLOW = (255, 255, 0)

        # launcher walls
        pygame.draw.rect(screen, YELLOW, (20, 270, THICKNESS, 380))  # left
        pygame.draw.rect(screen, YELLOW, (50, 320, THICKNESS, 330))  # right

        # left slanted wall
        points1 = [(58,320), (50, 320), (200,650), (208,650)]
        pygame.draw.polygon(screen, (255,255,0), points1, 0)

        # right slanted wall
        points2 = [(525,272), (450,360), (450,352), (525,262)]
        pygame.draw.polygon(screen, (255,255,0), points2,0)

        # right wall
        pygame.draw.rect(screen, (255,255,0), (450,350,8,160))
        
        # 2nd right slanted wall
        points3 = [(457,510), (449, 510), (340,650), (348,650)]
        pygame.draw.polygon(screen, (255,255,0), points3,0)

        # top semi-circle
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
        GRAY = (105,105,105)
        pygame.draw.rect(screen, GRAY, (35,450,8,200)) # Pipe
        pygame.draw.rect(screen, GRAY, (29,450,20,20)) # Block

    
    def drawFlippers(self, screen):
        # draw flippers
        GRAY = (105,105,105)
        pygame.draw.rect(screen, GRAY, (180,400,8,75)) # left pole
        pygame.draw.rect(screen, GRAY, (370,400,8,75)) # right pole
        RED = (255,0,0)
        pointsLeftFipper = [(188, 470), (260, 510), (230, 510)]
        pygame.draw.polygon(screen, RED, pointsLeftFipper,0) # left flipper
        pointsRightFlipper = [(370, 470),(298, 510), (328, 510)]
        pygame.draw.polygon(screen, RED, pointsRightFlipper,0) # right flipper


    def drawBigBall(self, screen):
        # draw big ball at the top (purple)
        DARKPURPLE = (48, 25, 52)
        pygame.draw.circle(screen, DARKPURPLE, (275, 150), 60)

    def drawSmallBalls(self, screen):
        # draw small balls around the big ball
        HOTPINK = (255, 105, 180)
        pygame.draw.circle(screen, HOTPINK, (275, 275), 20)
        pygame.draw.circle(screen, HOTPINK, (190, 240), 20)
        pygame.draw.circle(screen, HOTPINK, (360, 240), 20)
        pygame.draw.circle(screen, HOTPINK, (400, 170), 20)

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