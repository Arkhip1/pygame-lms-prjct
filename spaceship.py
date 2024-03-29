import pygame as pg
from pygame.sprite import Sprite


class Spaceship(Sprite):

    def __init__(self, screen):
        super(Spaceship, self).__init__()
        self.screen = screen
        self.image = pg.image.load('assts/ship.png')
        self.image = pg.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def rendering(self):  # Отображение космолета
        self.screen.blit(self.image, self.rect)

    def update(self):  # Движение космолета
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_ship(self):  # Создание нового корабля
        self.center = self.screen_rect.centerx
