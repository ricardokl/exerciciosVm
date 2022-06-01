""" problem_generator.main.modifiers.Random

"""

from random import randint, choice

from numpy import arange

from problem_generator.main.modifiers.Base import Modifier


class RandomValue(Modifier):
    """ A Random Value Generator """
    KWARGS = [
        'min',
        'max',
        'step',
        'div',
        'multi'
    ]

    FORMATTER_KWARGS = [
        'comma',
        'decimals'
    ]

    MIN_DEFAULT = 0
    MAX_DEFAULT = 1000
    STEP_DEFAULT = 1
    MULTI_DEFAULT = 1
    DIV_DEFAULT = 1

    COMMA_DEFAULT = True
    DECIMALS_DEFAULT = 1

    PARSER = 'default'

    def __init__(self, **kwargs) -> None:
        super(RandomValue, self).__init__(**kwargs)

    def generate(self, **kwargs) -> str:
        min_ = self.parse(self.args.get('min', self.MIN_DEFAULT), **kwargs)
        max_ = self.parse(self.args.get('max', self.MAX_DEFAULT), **kwargs)
        step = self.parse(self.args.get('step', self.STEP_DEFAULT), **kwargs)
        multi = self.parse(self.args.get('multi', self.MULTI_DEFAULT), **kwargs)
        div = self.parse(self.args.get('div', self.DIV_DEFAULT), **kwargs)
        if div == 0:
            div = 1

        return float(choice(arange(min_, max_, step))) * multi / div

    def formatter(self, value, **kwargs) -> str:
        comma = self.fmt_args.get('comma', self.COMMA_DEFAULT)
        decimals = self.parse(self.fmt_args.get('decimals', self.DECIMALS_DEFAULT), **kwargs)
        if decimals == 0:
            value = str(int(value))
        else:
            value = str(round(value, decimals))
        return value.replace('.', ',') if comma else value
