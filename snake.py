"""
1.创建蛇类并继承精灵
2.单独设置蛇头,需要蛇头坐标判断碰撞
3.蛇身增加方法
4.蛇移动方法
5.内容更新方法
6.对象绘制方法
"""
import pygame
from time import sleep
from pygame.sprite import Sprite

class Snakes:
    def __init__(self,screen,settings) :

        # 初始化必要属性
        self.screen = screen
        self.setting = settings
        
        # 设置初始移动方向；右侧
        self.direction = "right"


        # 加载蛇头图像并获取其rect属性
        self.image = pygame.image.load('D:\PythonProject\GSnake\images\snake.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 初始化蛇头位置
        self.rect.x = self.screen_rect.centerx 
        self.rect.y = self.screen_rect.centery 

        # 创建存储蛇头蛇骨节的列表，直接给他仨；简单粗暴，直接存，我可真棒......
        self.snakes = [
             (self.rect.x,self.rect.y),
             (self.rect.x - self.rect.width,self.rect.y),
             (self.rect.x - self.rect.width * 2,self.rect.y)
        ]  

    def add_segment(self):
        # 添加一个新的蛇段到蛇身列表的末尾，位置与蛇尾相同
        last_segment = self.snakes[-1]
        self.snakes.append(last_segment)

    def update(self):  
        # 1.先更新蛇的身体部分  倒着找，会不包括首个0
        for i in range(len(self.snakes) - 1, 0, -1):
            self.snakes[i] = self.snakes[i - 1]
        # 2.根据事件返回的key，改变蛇头方向；
        if self.direction == "right":
            self.rect.x += self.rect.width
        elif self.direction == "left":
            self.rect.x -= self.rect.width
        elif self.direction == "up":
            self.rect.y -= self.rect.height
        elif self.direction == "down" :
            self.rect.y += self.rect.height
        # 3. 最后更新蛇头的位置
        self.snakes[0] = (self.rect.x, self.rect.y)    

    def center_snake(self):
        # 不知道咋搞，反正就再粘贴1次呗
        self.rect.x = self.screen_rect.centerx 
        self.rect.y = self.screen_rect.centery 
        self.snakes = [
             (self.rect.x,self.rect.y),
             (self.rect.x - self.rect.width,self.rect.y),
             (self.rect.x - self.rect.width * 2,self.rect.y)
        ]  
        

    def blit(self):
        for snake in self.snakes:
            # 元组画不出来，需要先取出来再画出来；x坐标snake[0]；
            body_rect = pygame.Rect(snake[0], snake[1],self.rect.width, self.rect.height)
            self.screen.blit(self.image, body_rect)



