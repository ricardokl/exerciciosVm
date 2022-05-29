""" problem_generator.main.modifiers.Parser

"""

from problem_generator.main.modifiers.Base import Modifier
from problem_generator.main.modifiers.Random import RandomValue, RandomGroup


def modifier_parse(args: dict) -> Modifier:
    """ A simple parser to identify which modifier to use.

    TODO:
    - For now it's very simple and objective, but it tends to have a higher complexity by time.
    """
    if not args:
        return RandomValue()

    elif 'group' in args.keys():
        return RandomGroup(**args)

    else:
        return RandomValue(**args)

