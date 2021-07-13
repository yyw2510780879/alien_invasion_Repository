import sys
import pygame
import game_functions as gy
from settings import Settings
from mali import Mali

class SuperMali():
    """创建一个背景为蓝色的pygame窗口，并将超级玛丽图片打印在中央"""

    def __init__(self, screen_color):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Aline Invasion")

        # 创建一艘飞船
        self.Mali = Mali(self)

        # 设置开始背景色
        self.bg_color = screen_color


    def rungame(self):
        """开始游戏的主循环"""
        while True:
            gy.check_events()
            gy.update_screen(self.settings, self.screen, self.Mali)

screen_color = (255, 255, 255)
super_mail = SuperMali(screen_color)
super_mail.rungame()