import pygame
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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.update()
    screen.fill((0,0,0)) # Change this to the pinball machine screen (resets to this)
    pygame.draw.rect(screen, (255,255,0), (202.5,520, 60,10)) # left flipper
    pygame.draw.rect(screen, (255,255,0), (288.5,520, 60,10)) # right flipper


    ball.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
