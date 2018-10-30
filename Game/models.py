from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random
import numpy


author = 'Jacopo Magnani'

doc = """
Pilot Design for SM
"""


class Constants(BaseConstants):
    name_in_url = 'game'
    players_per_group = 6
    num_rounds = 2
    type_space = [2, 10]


class Subsession(BaseSubsession):

    def creating_session(self):
        # set paying round and game sequence
        if self.round_number == 1:
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
        # # form groups allowing for variable group size
        # group_matrix = []
        # players = self.get_players()
        # ppg = self.session.config['players_per_group']
        # for i in range(0, len(players), ppg):
        #     group_matrix.append(players[i:i + ppg])
        # self.set_group_matrix(group_matrix)


class Group(BaseGroup):

    def initialize_group(self):
        side_list = list([0, 0, 0, 1, 1, 1])
        # assign type and side
        for p in self.get_players():
            p.type = random.uniform(Constants.type_space[0], Constants.type_space[1])
            p.type = round(p.type, 1)
            p.side = side_list.pop(random.randrange(0, len(side_list)))

    def get_outcome(self):
        # assign rankings
        side0_bids = [p.bid for p in self.get_players() if p.side == 0]
        side1_bids = [p.bid for p in self.get_players() if p.side == 1]
        side0_bids.sort()
        side1_bids.sort()
        for b in set(side0_bids):
            rank_set = [i for i, x in enumerate(side0_bids) if x == b]
            for p in [q for q in self.get_players() if q.side == 0]:
                if p.bid == b:
                    p.rank = rank_set.pop(random.randrange(0, len(rank_set)))
        for b in set(side1_bids):
            rank_set = [i for i, x in enumerate(side1_bids) if x == b]
            for p in [q for q in self.get_players() if q.side == 1]:
                if p.bid == b:
                    p.rank = rank_set.pop(random.randrange(0, len(rank_set)))
        # form matches
        for p in self.get_players():
            p.points = 0 - p.bid
            for q in self.get_players():
                if p.rank == q.rank and p.side != q.side:
                    p.partner_type = q.type
                    p.points = p.type * q.type - p.bid
            p.points = round(p.points,2)
            if self.subsession.round_number == self.session.vars['paying_round']:
                p.payoff = p.points
            else:
                p.payoff = c(0)


class Player(BasePlayer):
    type = models.FloatField()
    side = models.IntegerField()
    rank = models.IntegerField()
    partner_type = models.FloatField()
    bid = models.FloatField(min=0, max=50)
    late = models.IntegerField()
    points = models.IntegerField()