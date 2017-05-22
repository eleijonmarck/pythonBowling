#!/usr/bin/python3

import unittest

from bowling.bowling import Game


class TestBowlingMethods(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_empty_game_has_score_of_zero(self):
        self.assert_game_score(0, self.game.score_game([]))

    def test_one_game_with_specific_set_throws(self):
        self.assert_game_score(17, [5, 4, 1, 6, 1])

    def test_one_spare_gives_additional_points_in_frame_before(self):
        self.assert_game_score(13, [5, 5, 3])

    def test_two_strikes_in_a_row(self):
        self.assert_game_score(30, [10, 10])

    def test_perfect_game(self):
        self.assert_game_score(300, [10] * 12)

    def assert_game_score(self, expected_score, game_played):
        self.assertEqual(
            expected_score, self.game.score_game(game_played))


if __name__ == '__main__':
    unittest.main()
