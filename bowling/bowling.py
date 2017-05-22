#!/usr/bin/python3

# -*- coding: utf-8 -*- #


class Game(object):
    def __init__(self):
        self.total = 0
        self.frames = Frame(12)
        self.throws = 0
        self.strikes_in_row = 0

    def score_game(self, played_game):
        if not played_game:
            return self.total
        else:
            for throw in played_game:
                self.throws += 1
                self.frame_total = throw
                if (self.frame_total == 10) and (self.throws % 2 == 1):
                    if self.strikes_in_row < 3:
                        self.strikes_in_row += 1
                    if (self.throws % 2 == 1):
                        self.total += throw
                        if self.strikes_in_row == 2:
                            self.total += throw
                            self.total += throw
                        if self.strikes_in_row == 3:
                            self.strikes_in_row = 2
                            self.total += throw
                            self.total += throw
                    if (self.throws % 2 == 0):
                        self.total = + throw

                if (self.throws % 2 == 0):
                    if (self.frame_total < 10):
                        self.strikes_in_row = 0
                    self.frame_total = 0

                self.total += throw

            if sum(played_game) == 120:
                self.total += 20

            return self.total


class Frame(object):
    def __init__(self, number_of_frames):
        self.frame_total = 0
        self.number_of_frames = number_of_frames

    def score_first(self, first_score):
        self.first = first_score

    def score_second(self, second_score):
        self.second = second_score
