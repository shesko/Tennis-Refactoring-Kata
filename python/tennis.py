# -*- coding: utf-8 -*-
from enum import Enum


class TennisGame1:
    def __init__(self, player_one_name, player_two_name):
        self.player_one = Player(player_one_name)
        self.player_two = Player(player_two_name)
        self.score_formatter = ScoreFormatter(self.player_one, self.player_two)

    def won_point(self, player_name):
        if player_name == self.player_one.name:
            self._player_won_point(self.player_one, self.player_two)
        else:
            self._player_won_point(self.player_two, self.player_one)

    def _player_won_point(self, player, opponent):
        player.win_point()
        if player.has_won(opponent):
            player.win_game()
            player.reset_points()
            opponent.reset_points()

    def score(self):
        return self.score_formatter.get_formatted_score()

    def games_score(self):
        return "{}-{}".format(self.player_one.won_games, self.player_two.won_games)


class Player:
    REQUIRED_POINT_DIFFERENCE_TO_WIN = 2
    ADVANTAGE_POINT_DIFFERENCE = 1

    def __init__(self, name):
        self._name = name
        self._points = 0
        self._games = 0

    @property
    def name(self):
        return self._name

    @property
    def points(self):
        return self._points

    @property
    def won_games(self):
        return self._games

    def win_point(self):
        self._points += 1

    def win_game(self):
        self._games += 1

    def reset_points(self):
        self._points = 0

    def has_won(self, opponent):
        return self._points >= 4 and \
               self._points - opponent.points >= self.REQUIRED_POINT_DIFFERENCE_TO_WIN

    def is_draw(self, opponent):
        return self._points == opponent.points

    def has_advantage(self, opponent):
        return self._points >= 4 and \
               self._points - opponent.points == self.ADVANTAGE_POINT_DIFFERENCE

    def is_winning(self, opponent):
        return self._points > opponent.points


class TennisTerms(Enum):
    LOVE = "Love"
    FIFTEEN = "Fifteen"
    THIRTY = "Thirty"
    FORTY = "Forty"
    ADVANTAGE = "Advantage"
    WIN = "Win"
    ALL = "All"
    DEUCE = "Deuce"


class ScoreFormatter:

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def get_formatted_score(self):
        if self.player_one.is_draw(self.player_two):
            return self.get_draw_text()
        elif self.player_one.has_advantage(self.player_two):
            return self._get_advantage_text(self.player_one)
        elif self.player_two.has_advantage(self.player_one):
            return self._get_advantage_text(self.player_two)
        else:
            return self.get_mid_game_score_text()

    def get_draw_text(self):
        if self.player_one.points < 3:
            return "{}-{}".format(
                self._get_point_name(self.player_one.points),
                TennisTerms.ALL.value
            )
        return TennisTerms.DEUCE.value

    def get_mid_game_score_text(self):
        return "{}-{}".format(
            self._get_point_name(self.player_one.points),
            self._get_point_name(self.player_two.points)
        )

    def _get_point_name(self, score):
        return {
            0: TennisTerms.LOVE.value,
            1: TennisTerms.FIFTEEN.value,
            2: TennisTerms.THIRTY.value,
            3: TennisTerms.FORTY.value,
        }[score]

    def _get_advantage_text(self, player):
        return "{} {}".format(
            TennisTerms.ADVANTAGE.value,
            player.name
        )
