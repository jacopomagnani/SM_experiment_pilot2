from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Part1Intro(Page):
    def is_displayed(self):
        return self.round_number == 1


class Part2Intro(Page):
    def is_displayed(self):
        return self.round_number == Constants.poll_round

    def vars_for_template(self):
        return {
            'rate_value': self.session.config['real_world_currency_per_point'],
        }


class Poll1(Page):

    form_model = 'player'
    form_fields = ['message']

    def is_displayed(self):
        return self.round_number == Constants.poll_round


class PollWaitPage(WaitPage):

    def is_displayed(self):
        return self.round_number == Constants.poll_round

    def after_all_players_arrive(self):
        self.group.get_poll_results()


class Poll2(Page):
    def is_displayed(self):
        return self.round_number == Constants.poll_round


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

    timeout_seconds = 120

    def vars_for_template(self):
        return {
            'ranks_list': [1, 2, 3],
            'match_payoff': self.player.type * self.player.partner_type
        }


class PartEnd(Page):

    def is_displayed(self):
        return self.round_number == Constants.part1_end or self.round_number == Constants.part2_end


page_sequence = [
    Part1Intro,
    Part2Intro,
    Poll1,
    PollWaitPage,
    Poll2,
    MyWaitPage1,
    Page1,
    MyWaitPage2,
    Page2,
    PartEnd
]
