from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Jacopo Magnani'

doc = """
Pilot Design for SM Asymmetric case
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = 5
    num_rounds = 50
    poll_round = 46
    part1_end = 45
    part2_end = 50
    type_space = [2, 10]
    side_space = [1, 1, 1, 2, 2]


class Subsession(BaseSubsession):

    part = models.IntegerField()
    round_number_in_part = models.IntegerField()

    def creating_session(self):
        if self.round_number == 1:
            for t in range(1, Constants.num_rounds+1):
                if t <= Constants.part1_end:
                    self.in_round(t).part = 1
                    self.in_round(t).round_number_in_part = self.in_round(t).round_number
                else:
                    self.in_round(t).part = 2
                    self.in_round(t).round_number_in_part = self.in_round(t).round_number - Constants.part1_end

class Group(BaseGroup):

    num_yes = models.IntegerField()
    num_no = models.IntegerField()

    def initialize_group(self):
        side_list = list(Constants.side_space)
        # assign type and side
        for p in self.get_players():
            p.type = random.uniform(Constants.type_space[0], Constants.type_space[1])
            p.type = round(p.type, 1)
            p.side = side_list.pop(random.randrange(0, len(side_list)))

    def get_outcome(self):
        # assign rankings
        side1_bids = [p.bid for p in self.get_players() if p.side == 1]
        side2_bids = [p.bid for p in self.get_players() if p.side == 2]
        side1_bids.sort(reverse=True)
        side2_bids.sort(reverse=True)
        for b in set(side1_bids):
            rank_set = [i for i, x in enumerate(side1_bids) if x == b]
            for p in [q for q in self.get_players() if q.side == 1]:
                if p.bid == b:
                    p.rank = rank_set.pop(random.randrange(0, len(rank_set)))
        for b in set(side2_bids):
            rank_set = [i for i, x in enumerate(side2_bids) if x == b]
            for p in [q for q in self.get_players() if q.side == 2]:
                if p.bid == b:
                    p.rank = rank_set.pop(random.randrange(0, len(rank_set)))
        # form matches
        for p in self.get_players():
            p.points = 0 - p.bid
            p.partner_type = 0
            for q in self.get_players():
                if p.rank == q.rank and p.side != q.side:
                    p.partner_type = q.type
                    p.points = p.type * q.type - p.bid
            p.points = round(p.points, 1)
            p.payoffs = p.points / Constants.num_rounds

    def get_poll_results(self):
        self.num_yes = sum([p.message for p in self.get_players()])
        self.num_no = sum([(1-p.message) for p in self.get_players()])


class Player(BasePlayer):
    type = models.FloatField()
    side = models.IntegerField()
    rank = models.IntegerField()
    partner_type = models.FloatField()
    bid = models.FloatField(min=0, max=50)
    late = models.IntegerField()
    points = models.FloatField()
    message = models.IntegerField(
        choices=[
            [1, 'I agree with the above statement and I pledge to bid 0 in the next rounds.'],
            [0, 'I do not agree with the above statement and I do not pledge to bid 0 in the next rounds.'],
        ],
        widget=widgets.RadioSelect
    )
