"""
1.创建食物类 并 继承精灵
2.加载指定的食物资源图片
3.在屏幕内随机生成
"""
import pygame
import random 
from pygame.sprite import Sprite


class Cookies(Sprite):
    def __init__(self,screen,settings):
        # 初始化精灵类
        super().__init__()
        #初始化属性
        self.screen = screen
        self.setting = settings

        #加载食物图片并获取其rect属性
        self.image = pygame.image.load('./GSnake/images/cookie.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将食物随机显示在屏幕上
        self.rect.x = random.randint(0,self.screen_rect.width - self.rect.width)
        self.rect.y = random.randint(0,self.screen_rect.height - self.rect.height)

    def update(self):
    # 更新
        pass

    def blit(self):
    # 在屏幕内绘制食物
        self.screen.blit(self.image,self.rect)

        