"""用于实现alien_invasion的主要功能的模块"""

import sys
import pygame
from bullet import Bullet


def check_events(ai_game):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_game)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_game)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 每次循环时都重新绘制飞船
    ship.blitme()
    # 每次循环时都需要更新飞船位置，绘制飞船和更新位置两个不分先后
    ship.update()
    # 每次循环都重新绘制子弹编组
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 每次循环都更新子弹编组中所有子弹的位置
    bullets.update()
    # 每次循环都需要检查编组bullets中的子弹是否超出屏幕
    # 如果超出屏幕则需要撤销它，这里需要注意的是bullets.copy()，如果我们不这样做，会导致错误
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))，核实子弹确实被删除了

    # 让最近绘制的屏幕可见。
    pygame.display.flip()


def check_keydown_events(event, ai_game):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ai_game.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ai_game.ship.moving_left = True
    elif event.key == pygame.K_UP:
        ai_game.ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ai_game.ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_game)


def check_keyup_events(event, ai_game):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ai_game.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ai_game.ship.moving_left = False
    elif event.key == pygame.K_UP:
        ai_game.ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ai_game.ship.moving_down = False


def fire_bullet(ai_game):
    """如果屏幕上的子弹数量没有达到上限，就创建一颗子弹"""
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(ai_game.bullets) < ai_game.settings.bullets_allowed:
        new_bullet = Bullet(ai_game)
        ai_game.bullets.add(new_bullet)
