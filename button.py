import pygame.font


class Button:
    def __init__(self,screen,settings,msg) :
        self.screen = screen
        self.settings = settings

        #获取屏幕属性
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的大小，颜色，以及文字和字体
        self.width = 200
        self.height = 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,50)

        # 创建按钮并将按钮放置到屏幕中间
        self.rect = pygame.Rect(0 , 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.prep_msg(msg)
    
    def prep_msg(self,msg):
        # 将文字渲染成图像，
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        # 将文字在按钮上剧中显示
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        # 将按钮和文字绘制出来
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)