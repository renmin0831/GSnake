import pygame

class Settings:
    def __init__(self) :
        # 屏幕背景填充色
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 230,230,230

        # 游戏次数
        self.snake_life = 2
        
        # 吃1个食物得分
        self.cookie_point = 1
       