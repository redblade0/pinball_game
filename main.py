import pygame
import math
from ball import Ball
from pinballMachine import PinballMachine

pygame.init()
SCREEN_WIDTH = 550
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
pygame.display.set_caption("Pinball-Game")

WHITE = (255,255,255)
RADIUS = 9
ball = Ball(39,440, RADIUS, WHITE, 0, 0)
machine = PinballMachine(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, score = 0)
machine.ball = ball

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    machine.drawPinballMachine(screen)
    ball.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)



pygame.quit()
