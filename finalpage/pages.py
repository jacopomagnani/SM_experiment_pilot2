from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def vars_for_template(self):
        return {
            'rate_value': self.session.config['real_world_currency_per_point'],
            'fee': self.session.config['participation_fee']
        }


page_sequence = [
    MyPage
]
