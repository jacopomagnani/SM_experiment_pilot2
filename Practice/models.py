from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Jacopo Magnani'

doc = """
Pilot Design for SM
"""


class Constants(BaseConstants):
    name_in_url = 'practice_round'
    players_per_group = 6
    num_rounds = 1
    part1_end = 1
    type_space = [2, 10]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    type = models.FloatField()
    side = models.IntegerField()
    rank = models.IntegerField()
    partner_type = models.FloatField()
    bid = models.FloatField(min=0, max=50)
    late = models.IntegerField()
    points = models.FloatField()

    def initialize_player(self):
        self.type = round(random.uniform(Constants.type_space[0], Constants.type_space[1]),1)
        self.side = 0

    def get_outcome(self):
        me_list = [1, 0, 0, 0, 0, 0]
        side_list = [0, 0, 0, 1, 1, 1]
        type_list = [round(random.uniform(Constants.type_space[0], Constants.type_space[1]), 1) for i in range(6)]
        type_list[0] = self.type
        bid_list = [random.uniform(0, 10) for i in range(6)]
        bid_list[0] = self.bid
        rank_list = [0, 0, 0, 0, 0, 0]
        side0_bids = [bid_list[i] for i in range(6) if side_list[i] == 0]
        side1_bids = [bid_list[i] for i in range(6) if side_list[i] == 1]
        side0_bids.sort()
        side1_bids.sort()
        for b in set(side0_bids):
            rank_set = [i for i, x in enumerate(side0_bids) if x == b]
            for i in range(6):
                if side_list[i] == 0 and bid_list[i] == b:
                    rank_list[i] = rank_set.pop(random.randrange(0, len(rank_set)))
        for b in set(side1_bids):
            rank_set = [i for i, x in enumerate(side1_bids) if x == b]
            for i in range(6):
                if side_list[i] == 1 and bid_list[i] == b:
                    rank_list[i] = rank_set.pop(random.randrange(0, len(rank_set)))
        self.rank = rank_list[0]
        self.participant.vars['practice_data'] = [{"id": me_list[i], "side": side_list[i], "type": type_list[i], "bid": bid_list[i], "rank": rank_list[i]} for i in range(6)]
        self.points = 0 - self.bid
        self.partner_type = 0
        for q in self.participant.vars['practice_data']:
            if self.rank == q['rank'] and self.side != q['side']:
                self.partner_type = q['type']
                self.points = self.type * q['type'] - self.bid
        self.points = round(self.points, 1)
        self.participant.vars['j'] = 1