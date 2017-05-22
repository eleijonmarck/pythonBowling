#!/usr/bin/python3

# -*- coding: utf-8 -*- #


def _create_frame(game, index):
    if _is_strike(game, index):
        return _create_strike(game, index)
    if _is_spare(game, index):
        return _is_spare(game, index)
    return _create_normal_frame(game, index)


def _create_strike(game, index):
    look_ahead = 3
    score = game.pins_knocked_down(index, look_ahead)
    return Frame(score, 1)


class Game(object):
    def __init__(self, throws):
        self._throws = throws

    def _throw(self, index):
        if index < len(self._throws):
            return self._throws[index]
        return 0

    def pins_knocked_down(self, index, look_ahead):
        throws_to_sum = map(self._throw, range(index, index + look_ahead))
        return sum(throws_to_sum)


class Frame(object):
    def __init__(self, number_of_frames):
        self.frame_total = 0
        self.number_of_frames = number_of_frames

    def score_first(self, first_score):
        self.first = first_score

    def score_second(self, second_score):
        self.second = second_score
