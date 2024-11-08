import pygame
import math
from pygame.locals import *
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([5, 5])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = 0, 0
        self.velocity = [10, 0]

    def update(self):
        acceleration_angle = self.get_angle()
        acceleration_x = (6.6743 / (10 ** 11)) * (2 * 10 ** 30) / (10 ** 10 * (self.get_distance_to_centre()) ** 2) * math.cos(acceleration_angle) 
        acceleration_y = (6.6743 / 10 ** 11) * (2 * 10 ** 30) / (10 ** 10 * (self.get_distance_to_centre()) ** 2) * math.sin(acceleration_angle) 
        self.rect.x = self.rect.x + self.velocity[0] * dt + 0.5 * acceleration_x * dt ** 2
        self.rect.y = self.rect.y + self.velocity[1] * dt + 0.5 * acceleration_y * dt ** 2

    def get_distance_to_centre(self):
        return ((500 - self.rect.x) ** 2 + (500 - self.rect.y) ** 2) ** 0.5
    def get_angle(self):
        return math.atan((500 - self.rect.x) / (500 - self.rect.y))
    
def main():
    global dt
    # Initialise screen
    pygame.init()
    b = Bullet()
    bs = pygame.sprite.Group()
    bs.add(b)
    screen = pygame.display.set_mode((1000, 1000))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    clock = pygame.time.Clock()
    # Event loop
    while True:
        dt = clock.tick(60)
        print(b.rect.x, b.rect.y)
        screen.blit(background, (0, 0))
        bs.update()
        bs.draw(screen)
        pygame.draw.circle(screen, (255, 0, 0), (500, 500), 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        pygame.display.flip()





if __name__ == '__main__': main()
