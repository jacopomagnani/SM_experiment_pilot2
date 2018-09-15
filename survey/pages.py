from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class page1(Page):

    form_model = 'player'
    form_fields = ['sex', 'major']


page_sequence = [
    Intro,
    page1
]
