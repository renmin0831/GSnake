import pygame.font

class ScoreBoard:
    def __init__(self,screen,settings,stats) :
    
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats

        # 分数背景色和字体
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,40)

        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        # 将得分渲染成图像
        # round_score = int(round(self.stats.score,-1))
        # score_str = "{:,}".format(round_score)
 
        score_str = str(self.stats.score)
        print("score_str:", score_str)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        # 将得分放置在屏幕左上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 60

    def prep_high_score(self):
        score_str = str(self.stats.score)
        self.high_score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)

        # 将得分放置在屏幕左上角
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 20


    def blit(self):
        # 将分数绘制出来
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)



