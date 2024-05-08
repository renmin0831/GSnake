import pygame
from settings import Settings
import game_functions as gf
from snake import Snakes
from game_stats import GameStats
from time import sleep
from button import Button
from scoreboard import ScoreBoard
# 创建 Clock
clock = pygame.time.Clock()

def rungame():
    # 初始化pygame库
    pygame.init()
    # 设置窗口标题
    pygame.display.set_caption("贪吃蛇")
    # 创建设置实例，获取属性
    settings = Settings()
    # 创建屏幕对象
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_height))
    # 创建食物精灵组实例
    cookies = pygame.sprite.Group()
    # 创建统计信息实例
    stats = GameStats(settings)
    # 创建蛇头蛇身实例
    snakes = Snakes(screen,settings)
    # 创建食物实例
    gf.create_cookie(screen,settings,cookies)
    # 创建按钮实例，并给出按钮上显示的文字
    play_button = Button(screen,settings,'Play')
    # 创建分数实例
    scoreboard= ScoreBoard(screen,settings,stats)


    while True :
        # 检测键盘事件
        gf.check_event(snakes,stats,play_button,cookies,screen,settings)
        screen.fill(settings.bg_color)
        # 更新活动状态
        if stats.game_active:
            # 更新蛇头和身体骨节移动
            gf.update_snake(snakes)
            # 蛇和边缘碰撞检测
            gf.snake_edge_collision(snakes,stats,cookies,screen,settings)
            # 蛇和自己的碰撞检测
            gf.snake_body_collision(snakes,stats,cookies,screen,settings)
            # 蛇和食物的碰撞检测
            gf.snake_cookie_collision(snakes,cookies,screen,settings,stats,scoreboard)
            # 设置更新帧率,时间是毫秒
            clock.tick(15)
        # 更新屏幕上的对象
        gf.update_screen(cookies,snakes,screen,play_button,stats,scoreboard)
    
rungame()



