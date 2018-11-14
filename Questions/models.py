from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Questions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q1 = models.FloatField()
    q2 = models.IntegerField(choices=[
        [1, 'Player B will earn 7 points.'],
        [2, 'Player B will earn either 7 points or 1 point.'],
        [3, 'Player B may earn any of the following amounts of points: 7, 1 or -3.'],
        ], widget=widgets.RadioSelect
    )
    q3 = models.IntegerField(choices=[
        [1, 'Player B will earn 12 points.'],
        [2, 'Player B will earn either 12 points or 4 points.'],
        [3, 'Player B may earn any of the following amounts of points: 12, 4 or -8.'],
        ], widget=widgets.RadioSelect
    )
