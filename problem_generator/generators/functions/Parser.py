
from problem_generator.generators.functions.Base import Modifier
from problem_generator.generators.functions.Random import RandomValue, RandomGroup


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

