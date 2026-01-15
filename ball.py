import pygame

class Ball:
    
    def __init__(self, x, y, radius, color, velocity_x, velocity_y):
        self.pos = pygame.math.Vector2(x,y)
        self.radius = radius
        self.color = color # might change this to be a png (sprite), for now it will be a color
        self.vel = pygame.math.Vector2(velocity_x, velocity_y)
    
    def update(self):
        self.pos += self.vel

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)
    
