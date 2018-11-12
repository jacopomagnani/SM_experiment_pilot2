from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Q1Page1(Page):

    form_model = 'player'
    form_fields = ['q1']


class Q1Page2(Page):
        pass


class Q2Page1(Page):

    form_model = 'player'
    form_fields = ['q2']


class Q2Page2(Page):
        pass


class Q3Page1(Page):

    form_model = 'player'
    form_fields = ['q3']


class Q3Page2(Page):
        pass


page_sequence = [
    Intro,
    Q1Page1,
    Q1Page2,
    Q2Page1,
    Q2Page2,
    Q3Page1,
    Q3Page2
]
