import pygame
import sys
from cookies import Cookies
from snake import Snakes
from time import sleep
import game_functions as gf


def check_event(snakes,stats,play_button,cookies,screen,settings):
    # 检测键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event,snakes)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 返回鼠标点击坐标
            mouse_x, moouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x, moouse_y,cookies,screen,settings,snakes)

def check_play_button(stats,play_button,mouse_x, moouse_y,cookies,screen,settings,snakes):
    # 点击了play按钮游戏状态改为True；collidepoint点击范围是否在按钮内
    button_click = play_button.rect.collidepoint(mouse_x, moouse_y)
    # 开始又隐藏play按钮
    if button_click and not stats.game_active:
        # 重新开始会重置数据
        stats.reset_stats()
        stats.game_active = True
        # 清空食物并重随食物
        cookies.empty()
        create_cookie(screen,settings,cookies)
        #重置贪吃蛇的位置
        snakes.center_snake()
        #隐藏鼠标光标
        pygame.mouse.set_visible(False)

def check_key_down(event,snakes):
    # 检测按键，不能倒车
    if event.key == pygame.K_RIGHT :
        if snakes.direction == "up" or snakes.direction == "down":
            snakes.direction = "right"
    elif event.key == pygame.K_LEFT :
        if snakes.direction == "up" or snakes.direction == "down":
            snakes.direction = "left"
    elif event.key == pygame.K_UP :
        if snakes.direction == "right" or snakes.direction == "left":
            snakes.direction = "up"
    elif event.key == pygame.K_DOWN:
        if snakes.direction == "right" or snakes.direction == "left":
            snakes.direction = "down"
    elif event.key == pygame.K_TAB:
        sys.exit()

def create_cookie(screen,settings,cookies):
    # 创建食物实例，并将实例添加到食物精灵组
    cookie = Cookies(screen,settings)
    cookies.add(cookie)

def snake_cookie_collision(snakes,cookies,screen,settings,stats,scoreboard):
    # 精灵和编组碰撞，返回第一个碰撞的精灵并停止遍历，True为删除发生碰撞的精灵
    current_cookies_list = pygame.sprite.spritecollide(snakes,cookies,True)

    if current_cookies_list:
        for i in range(1,len(current_cookies_list)+1):
            # 增加分数和绘制分数
            stats.score += settings.cookie_point * i
            # print(settings.cookie_point)
            # print(stats.score)
            #分数绘制
            scoreboard.prep_score()
        # 更新最高分数
        check_high_score(stats,scoreboard)
        # 在尾巴处新增1骨节蛇段
        snakes.add_segment()
        # 重新随食物
        create_cookie(screen,settings,cookies)

def snake_edge_collision(snakes,stats,cookies,screen,settings):
    # 如果撞墙则游戏结束
    if snakes.rect.left < 0 or snakes.rect.right > snakes.screen_rect.right or \
        snakes.rect.top < 0 or snakes.rect.bottom > snakes.screen_rect.bottom:
        reset_stats(stats,cookies,snakes,screen,settings)
    
def snake_body_collision(snakes,stats,cookies,screen,settings):
    # 如果撞到自己则游戏结束
    snake_head = snakes.snakes[0]
    for snake_body in snakes.snakes[1:]:
        if  snake_head[0] == snake_body[0] and snake_head[1] == snake_body[1]:
            reset_stats(stats,cookies,snakes,screen,settings)
            break

def reset_stats(stats,cookies,snakes,screen,settings):
    if  stats.snake_life > 0:
        stats.snake_life -= 1
        # 清空食物并重随食物
        cookies.empty()
        create_cookie(screen,settings,cookies)
        #重置贪吃蛇的位置
        snakes.center_snake()
        # 强制等待1秒
        sleep(1)
    else:
        stats.game_active = False
        # 恢复鼠标光标可见
        pygame.mouse.set_visible(True)

def check_high_score(stats,scoreboard):
    if stats.score > stats.high:
        stats.high = stats.score
        scoreboard.prep_high_score()


def update_snake(snakes):
    # 更新蛇头和身体骨节移动
    snakes.update()
     
def update_screen(cookies,snakes,screen,play_button,stats,scoreboard):
    # 屏幕中显示食物
    cookies.draw(screen)
    # 屏幕中显示分数
    scoreboard.blit()
    # 屏幕中显示蛇头蛇身体骨节
    snakes.blit()
    if not stats.game_active:
        play_button.draw()
    # 绘制内容可见
    pygame.display.flip()


