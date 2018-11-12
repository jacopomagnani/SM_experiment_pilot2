from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Part1Intro(Page):

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.initialize_player()


class MyWaitPage1(WaitPage):
    pass


class Page1(Page):

    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['bid']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.late = 1
            self.player.bid = random.uniform(0, 10)
        self.player.get_outcome()


class Page2(Page):

    timeout_seconds = 1120

    def vars_for_template(self):
        return {
            'ranks_set': [2, 1, 0],
            'match_payoff': self.player.type * self.player.partner_type,
            'market': self.participant.vars['practice_data']
        }


class PartEnd(Page):
    pass


page_sequence = [
    Part1Intro,
    MyWaitPage1,
    Page1,
    Page2,
    PartEnd
]
