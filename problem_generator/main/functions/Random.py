
from random import randint, choice

from problem_generator import CONFIG
from problem_generator.main.functions.Base import Modifier


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
        """ Generates a random value given the args. """
        #
        self.set_args(**kwargs)

        # Gets all the variables from the args.
        min_value = int(self.args.get('min', self.MIN_DEFAULT))
        max_value = int(self.args.get('max', self.MAX_DEFAULT))

        # The base value is the step, all other come from above it.
        # To set all equally define only the step value.
        step_value = int(self.args.get('step', self.STEP_DEFAULT))
        lstep_value = int(self.args.get('lstep', step_value))
        rstep_value = int(self.args.get('rstep', step_value))
        ostep_value = int(self.args.get('ostep', step_value))

        return randint(min_value * lstep_value, max_value * rstep_value) / ostep_value


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
