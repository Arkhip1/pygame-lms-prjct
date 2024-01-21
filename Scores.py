import pygame.font
from spaceship import Spaceship
from pygame.sprite import Group


class Scores():  # Вывод счёта
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_hi_score()
        self.image_lives()

    def image_score(self):  # Отображение текущего счёта
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_hi_score(self):  # Отображение рекорда
        self.hi_score_image = self.font.render(str(self.stats.hi_score), True, self.text_color,
                                               (0, 0, 0))
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.centerx = self.screen_rect.centerx
        self.hi_score_rect.top = self.screen_rect.top + 20

    def image_lives(self):  # Отображение оставшихся жизней
        self.lives = Group()
        for live_num in range(self.stats.lives_left):
            ship = Spaceship(self.screen)
            ship.rect.x = 15 + live_num * ship.rect.width
            ship.rect.y = 20
            self.lives.add(ship)

    def show_score(self):  # Отображение текущего счёта
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.lives.draw(self.screen)
