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
        [1, 'Player B will earn 10 points.'],
        [2, 'Player B will earn either 10 points or 14 points.'],
        [3, 'Player B may earn any of the following amounts of points: 10, 14 or 4.'],
        ], widget=widgets.RadioSelect
    )
    q3 = models.IntegerField(choices=[
        [1, 'Player B will earn 0 points.'],
        [2, 'Player B will earn either 0 points or 6 points.'],
        [3, 'Player B may earn any of the following amounts of points: 0, 6 or 24.'],
        ], widget=widgets.RadioSelect
)