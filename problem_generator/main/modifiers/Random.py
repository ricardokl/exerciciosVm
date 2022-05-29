""" problem_generator.main.modifiers.Random

"""

from random import randint, choice

from problem_generator import CONFIG
from problem_generator.main.modifiers.Base import Modifier


GROUPS = CONFIG['GROUPS']


class RandomValue(Modifier):
    """ A Random Value Generator """

    DEFAULT = True
    NAME = 'RandomValue'
    KWARGS = [
        'min',
        'max',
        'step',
        'lstep',
        'rstep',
        'ostep'
    ]

    MIN_DEFAULT = 0
    MAX_DEFAULT = 1000
    STEP_DEFAULT = 1

    def __init__(self, **kwargs) -> None:
        """ Initialize the Modifier. """
        super(RandomValue, self).__init__(**kwargs)

    def generate(self, **kwargs) -> float:
        """ Generates a Random Value Given the Args.

        Returns:
            A Random Value
        """
        min_value = self.parse(self.args.get('min', self.MIN_DEFAULT), **kwargs)
        max_value = self.parse(self.args.get('max', self.MAX_DEFAULT), **kwargs)
        step_value = self.parse(self.args.get('step', self.STEP_DEFAULT), **kwargs)
        left_step_value = self.parse(self.args.get('lstep', step_value), **kwargs)
        right_step_value = self.parse(self.args.get('rstep', step_value), **kwargs)
        outer_step_value = self.parse(self.args.get('ostep', step_value), **kwargs)

        return randint(min_value * left_step_value, max_value * right_step_value) / outer_step_value


class RandomGroup(Modifier):

    DEFAULT = False
    NAME = 'RandomGroup'
    KWARGS = [
        'group'
    ]

    GROUP_DEFAULT = ''

    def __init__(self, **kwargs):
        """ Initialize the Modifier. """
        super(RandomGroup, self).__init__(**kwargs)

    def generate(self, **kwargs) -> str:
        """ Choose a random value inside a given group. """
        #
        self.set_args(**kwargs)

        #
        key = self.args.get('group', self.GROUP_DEFAULT)
        if key not in GROUPS.keys():
            key = self.GROUP_DEFAULT
        #
        group = GROUPS[key]

        return choice(group)


if __name__ == '__main__':
    x = RandomValue(min='x0', max='x1')
    print(x.generate(x0=1))

