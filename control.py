import pygame as pg
import sys
import time

import pygame.sprite

from bullet import Bullet
from alien import Alien


def events(screen, ship, bullets):  # Управление
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                ship.mright = True
            elif event.key == pg.K_a:
                ship.mleft = True
            elif event.key == pg.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                ship.mright = False
            elif event.key == pg.K_a:
                ship.mleft = False


def update(bg_pic, screen, stats, sc, ship, aliens, bullets):
    screen.blit(bg_pic, (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.render_bullet()
    ship.rendering()
    aliens.draw(screen)
    pg.display.flip()


def update_bullets(screen, stats, sc, aliens, bullets):  # Движение снарядов
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 1 * len(aliens)
        stats.score += 1
        sc.image_score()
        check_rec(stats, sc)
        sc.image_lives()
    if len(aliens) == 0:
        bullets.empty()
        create_swarm(screen, aliens)


def ship_destroyed(stats, screen, sc, ship, aliens, bullets):  # Уничтожение космолета
    if stats.lives_left > 0:
        stats.lives_left -= 1
        sc.image_lives()
        aliens.empty()
        bullets.empty()
        create_swarm(screen, aliens)
        ship.create_ship()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_aliens(stats, screen, sc, ship, aliens, bullets):  # Движение пришельцев
    aliens.update()
    if pg.sprite.spritecollideany(ship, aliens):
        ship_destroyed(stats, screen, sc, ship, aliens, bullets)
    chek_aliens(stats, screen, sc, ship, aliens, bullets)


def chek_aliens(stats, screen, sc, ship, aliens, bullets):  # Действия пришельцев
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_destroyed(stats, screen, sc, ship, aliens, bullets)
            break


def create_swarm(screen, aliens):  # Создание роя пришельцев
    alien = Alien(screen)
    alien_w = alien.rect.width
    count_aliens_x = int((700 - 2 * alien_w) / alien_w)
    alien_h = alien.rect.height
    count_aliens_y = int((700 - 75 - 2 * alien_h) / alien_h)

    for row_num in range(count_aliens_y - 1):
        for alien_count in range(count_aliens_x):
            alien = Alien(screen)
            alien.x = alien_w + (alien_w * alien_count)
            alien.y = alien_h + (alien_h * row_num)
            alien.rect.x = alien.x * 1.05
            alien.rect.y = alien.rect.height + 1.05 * alien.rect.height * row_num
            aliens.add(alien)


def check_rec(stats, sc):  # Проверка рекорда
    if stats.score > stats.hi_score:
        stats.hi_score = stats.score
        sc.image_hi_score()
        with open('high_score.txt', 'w') as fl:
            fl.write(str(stats.hi_score))
