

class GameStats:
    def __init__(self,settings):
        self.settings = settings
        self.high = 0
        self.reset_stats()

    def reset_stats(self):
        # 在游戏期间重置的信息
        self.snake_life = self.settings.snake_life
        # 游戏状态
        self.game_active = False
        #初始分数
        self.score = 0