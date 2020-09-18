# -*- coding: utf-8 -*-

import unittest

from tennis import TennisGame1

test_cases = [
    (0, 0, "Love-All", '0-0', 'player1', 'player2'),
    (1, 1, "Fifteen-All", '0-0', 'player1', 'player2'),
    (2, 2, "Thirty-All", '0-0', 'player1', 'player2'),
    (3, 3, "Deuce", '0-0', 'player1', 'player2'),
    (4, 4, "Deuce", '0-0', 'player1', 'player2'),

    (1, 0, "Fifteen-Love", '0-0', 'player1', 'player2'),
    (0, 1, "Love-Fifteen", '0-0', 'player1', 'player2'),
    (2, 0, "Thirty-Love", '0-0', 'player1', 'player2'),
    (0, 2, "Love-Thirty", '0-0', 'player1', 'player2'),
    (3, 0, "Forty-Love", '0-0', 'player1', 'player2'),
    (0, 3, "Love-Forty", '0-0', 'player1', 'player2'),
    (4, 0, "Love-All", '1-0', 'player1', 'player2'),
    (0, 4, "Love-All", '0-1', 'player1', 'player2'),

    (2, 1, "Thirty-Fifteen", '0-0', 'player1', 'player2'),
    (1, 2, "Fifteen-Thirty", '0-0', 'player1', 'player2'),
    (3, 1, "Forty-Fifteen", '0-0', 'player1', 'player2'),
    (1, 3, "Fifteen-Forty", '0-0', 'player1', 'player2'),
    (4, 1, "Love-All", '1-0', 'player1', 'player2'),
    (1, 4, "Love-All", '0-1', 'player1', 'player2'),

    (3, 2, "Forty-Thirty", '0-0', 'player1', 'player2'),
    (2, 3, "Thirty-Forty", '0-0', 'player1', 'player2'),
    (4, 2, "Love-All", '1-0', 'player1', 'player2'),
    (2, 4, "Love-All", '0-1', 'player1', 'player2'),

    (4, 3, "Advantage player1", '0-0', 'player1', 'player2'),
    (3, 4, "Advantage player2", '0-0', 'player1', 'player2'),
    (5, 4, "Advantage player1", '0-0', 'player1', 'player2'),
    (4, 5, "Advantage player2", '0-0', 'player1', 'player2'),
    (15, 14, "Advantage player1", '0-0', 'player1', 'player2'),
    (14, 15, "Advantage player2", '0-0', 'player1', 'player2'),

    (6, 4, 'Love-All', '1-0', 'player1', 'player2'),
    (4, 6, 'Love-All', '0-1', 'player1', 'player2'),
    (16, 14, 'Love-All', '1-0', 'player1', 'player2'),
    (14, 16, 'Love-All', '0-1', 'player1', 'player2'),

    (6, 4, 'Love-All', '1-0', 'One', 'player2'),
    (4, 6, 'Love-All', '0-1', 'player1', 'Two'),
    (6, 5, 'Advantage One', '0-0', 'One', 'player2'),
    (5, 6, 'Advantage Two', '0-0', 'player1', 'Two'),

    (15, 0, 'Forty-Love', '3-0', 'player1', 'Two')
    ]


def play_game(TennisGame, p1Points, p2Points, p1Name, p2Name):
    game = TennisGame(p1Name, p2Name)
    for i in range(max(p1Points, p2Points)):
        if i < p1Points:
            game.won_point(p1Name)
        if i < p2Points:
            game.won_point(p2Name)
    return game


class TestTennis(unittest.TestCase):
     
    def test_current_game_scores(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, game_score, p1Name, p2Name) = testcase
            game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(score, game.score())

    def test_games_scores(self):
        for testcase in test_cases:
            (p1Points, p2Points, score, game_score, p1Name, p2Name) = testcase
            game = play_game(TennisGame1, p1Points, p2Points, p1Name, p2Name)
            self.assertEqual(game_score, game.games_score())


if __name__ == "__main__":
    unittest.main() 
