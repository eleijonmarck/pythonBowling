#!/usr/bin/python3

import unittest

from bowling.bowling import Game


class TestBowlingMethods(unittest.TestCase):
    def test_empty_game_has_score_of_zero(self):
        self.assertEqual(0, Game().score_game([]))

    def test_one_strike_has_score_of_ten(self):
        self.assert_game_score(10, [10])

    def test_one_spare_gives_additional_points_in_frame_before(self):
        self.assert_game_score(13, [5, 5, 3])

    def test_two_strikes_in_a_row(self):
        self.assert_game_score(30, [10, 10])

    def assert_game_score(self, expected_score, game_played):
        self.assertEqual(expected_score, Game().score_game(game_played))


if __name__ == '__main__':
    unittest.main()
