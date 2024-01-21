import pygame as pg
import sys


def run():
    pg.init()
    screen = pg.display.set_mode((1200, 800))
    pg.display.set_caption("Пришельцы атакуют")
    bg_pic = pg.image.load('bg_pic.jpg')
    x, y = 1200, 800

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        new_bg_pic = pg.transform.scale(bg_pic, (x, y))
        screen.blit(new_bg_pic, (0, 0))
        pg.display.flip()


run()
