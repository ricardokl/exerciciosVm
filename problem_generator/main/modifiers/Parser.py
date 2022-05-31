""" problem_generator.main.modifiers.Parser

"""

from problem_generator.main.modifiers.Base import Modifier

DEFAULT_MODIFIERS = {cls.PARSER: cls for cls in Modifier.__subclasses__()}


def modifier_parse(**kwargs) -> Modifier:
    """ Identifiers the Modifier to use given the Args. """
    keys = kwargs.keys()
    mods = [i for i in keys if i in DEFAULT_MODIFIERS.keys()]
    if len(mods) > 0:
        return DEFAULT_MODIFIERS[mods[0]](**kwargs)
    else:
        return DEFAULT_MODIFIERS['default'](**kwargs)
