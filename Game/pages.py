from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyWaitPage1(WaitPage):

    def after_all_players_arrive(self):
        self.group.initialize_group()


class Page1(Page):

    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['bid']

    def before_next_page(self):
        if self.timeout_happened:
            self.player.late = 1
            self.player.bid = random.uniform(0, 10)


class MyWaitPage2(WaitPage):

    def after_all_players_arrive(self):
        self.group.get_outcome()


class Page2(Page):

    timeout_seconds = 60

    def vars_for_template(self):
        return {'ranks_set': [2, 1, 0]}


class FinalPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'total_payoff': sum([p.payoff for p in self.player.in_all_rounds()]),
            'paying_round': self.session.vars['paying_round']
        }


page_sequence = [
    Intro,
    MyWaitPage1,
    Page1,
    MyWaitPage2,
    Page2,
    FinalPage
]
