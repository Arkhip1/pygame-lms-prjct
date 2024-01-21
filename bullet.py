import pygame as pg


class Bullet(pg.sprite.Sprite):

    def __init__(self, screen, ship):    # Инициализация
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect((0, 0, 5, 15))
        self.color = '#ffcc00'
        self.speed = 3.5
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)

    def update(self):    # Перемещение пули
        self.y -= self.speed
        self.rect.y = self.y

    def render_bullet(self):    # Отрисовка пули
        pg.draw.rect(self.screen, self.color, self.rect)
