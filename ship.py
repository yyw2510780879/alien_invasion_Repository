"""实现ship对象的模块"""
import pygame


class Ship:
    """docstring for Ship"""

    def __init__(self, ai_game):
        """初始化飞船并设置其初始位置"""
        # ai_game参数只是提供一个参数让飞船的坐标能依据屏幕的坐标移动
        self.screen = ai_game.screen
        self.ai_settings = ai_game.settings

        # 加载飞船头像并获取其外接矩形"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        # 将每艘新飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 因为self.rect.centerx中只能存整数值，所以另外初始化一个属性center存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.bottom)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象，虽然还会有0.5的截断，但至少只截断0.5
        self.rect.centerx = self.centerx
        self.rect.bottom = self.centery
