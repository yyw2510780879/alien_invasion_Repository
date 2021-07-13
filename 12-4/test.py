import pygame
import sys

class PrintEventKey:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Print event.key")

    def rungame(self):
        """开始游戏的主循环"""
        while True:
            check_events(self.screen)
            pygame.display.flip()

def check_events(screen):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            print(event.key)
    

print_event_key = PrintEventKey()
print_event_key.rungame()