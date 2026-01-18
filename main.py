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


ball = Ball(275,520, 10, (0,0,255), 0, 0)
machine = PinballMachine(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, score = 0)
machine.ball = ball

points = [(188, 470), (200, 550), (188, 550)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    machine.drawMachine(screen)
    machine.drawSmallBalls(screen)
    machine.drawBigBall(screen)
    machine.drawFlippers(screen)
    pygame.draw.polygon(screen, (255,0,0),points,0)
    pygame.display.flip()
    clock.tick(FPS)



pygame.quit()
