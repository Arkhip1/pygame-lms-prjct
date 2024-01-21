import pygame as pg
import control
from spaceship import Spaceship
from pygame.sprite import Group
from stats import Statistics
from Scores import Scores


def run():  # Функция запуска игры
    pg.init()
    x, y = 700, 700
    screen = pg.display.set_mode((x, y))
    pg.display.set_caption("Пришельцы атакуют")
    bg_pic = pg.image.load('assts/bg_picture.jpeg')
    bg_pic = pg.transform.scale(bg_pic, (x, y))
    ship = Spaceship(screen)
    bullets = Group()
    aliens = Group()
    control.create_swarm(screen, aliens)
    stats = Statistics()
    sc = Scores(screen, stats)

    while True:
        control.events(screen, ship, bullets)
        if stats.run_game:
            ship.update()
            control.update(bg_pic, screen, stats, sc, ship, aliens, bullets)
            control.update_bullets(screen, stats, sc, aliens, bullets)
            control.update_aliens(stats, screen, sc, ship, aliens, bullets)


run()
