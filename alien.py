import pygame as pg


class Alien(pg.sprite.Sprite):  # Создание 1 пришельца

    def __init__(self, screen):    # Инициализация
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pg.image.load('assts/aliens.png')
        self.image = pg.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):   # Отрисовка пришельца
        self.screen.blit(self.image, self.rect)

    def update(self):   # Движение пришельцев
        self.y += 0.1
        self.rect.y = self.y

