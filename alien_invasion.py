"""This is a playgame: alien invasion"""
import pygame

import game_functions as gy
from settings import Settings
from ship import Ship
from pygame.sprite import Group


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 创建一艘飞船
        self.ship = Ship(self)
        # 创建一个用于存储子弹的编组
        self.bullets = Group()

        # 设置开始背景色
        self.bg_color = self.settings.bg_color

    def rungame(self):
        """开始游戏的主循环"""

        while True:
            gy.check_events(self)
            gy.update_screen(self.settings, self.screen, self.ship, self.bullets)


if __name__ == '__main__':
    """创建游戏实例并运行游戏。"""
    ai = AlienInvasion()
    ai.rungame()
