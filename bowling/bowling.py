#!/usr/bin/python3


class Game(object):
    def __init__(self):
        self.total = 0
        self.frame_total = 0
        self.throws = 0

    def score_game(self, played_game):
        if not played_game:
            return self.total
        else:
            for throw in played_game:
                self.throws += 1
                self.frame_total = throw
                if (self.frame_total == 10) and (self.throws % 2 == 0):
                    self.total += throw
                    self.frame_total = 0

                if (self.throws % 2 == 0):
                    self.frame_total = 0

                self.total += throw
            return self.total


class Frame(object):
    def __init__(self):
        self.first = 0
        self.second = 0

    def score_first(self, first_score):
        self.first = first_score

    def score_second(self, second_score):
        self.second = second_score
