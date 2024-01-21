class Statistics():  # Статистика

    def __init__(self):
        self.reset_st()
        self.run_game = True
        with open('high_score.txt', 'r') as fl:
            self.hi_score = int(fl.readline())

    def reset_st(self):  # Изменение статистики в игре
        self.lives_left = 3
        self.score = 0

