#!/usr/bin/python3

# -*- coding: utf-8 -*- #


def score_game(throws):
    game = Game(throws)
    return sum(frame.score for frame in _frames(game))


def _frames(game):
    index = 0
    for frame_index in range(0, 10):
        frame = _create_frame(game, index)
        yield frame
        index += frame.length


def _create_frame(game, index):
    if _is_strike(game, index):
        return _create_strike(game, index)
    if _is_spare(game, index):
        return _create_spare(game, index)
    return _create_normal_frame(game, index)


def _create_strike(game, index):
    score = game.pins_knocked_down(index, 3)
    return Frame(score, 1)


def _create_spare(game, index):
    score = game.pins_knocked_down(index, 3)
    return Frame(score, 2)


def _create_normal_frame(game, index):
    score = game.pins_knocked_down(index, 2)
    return Frame(score, 2)


def _is_strike(game, index):
    return game.pins_knocked_down(index, 1) == 10


def _is_spare(game, index):
    return game.pins_knocked_down(index, 2) == 10


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
    def __init__(self, score, length):
        self.score = score
        self.length = length
