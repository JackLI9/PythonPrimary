class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("查看帮助信息")


    @classmethod
    def show_top_score(cls):
        print("历史最高分：%d" % cls.top_score)

    def start_game(self):
        print("%s开始游戏..." % self.player_name)


Game.show_help()

Game.show_top_score()

game = Game("小明")
game.start_game()

