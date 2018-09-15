from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Page1(Page):
    form_model = 'player'
    form_fields = ['answer1', 'answer2', 'answer3']

    def before_next_page(self):
        k = 0
        if self.player.answer1 == 5:
            k = k+1
        if self.player.answer2 == 5:
            k = k+1
        if self.player.answer3 == 47:
            k = k+1
        self.player.num_correct = k
        self.player.payoff = k*2


class Results(Page):
    pass


page_sequence = [
    Intro,
    Page1,
    Results
]
