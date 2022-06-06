""" problem_generator.main.modifiers.Parser

This package defines a parser function to return a modifier given it's values.

- Accept multiple variables o
"""

from problem_generator.main.modifiers.Base import Modifier

DEFAULT_MODIFIERS = {cls.PARSER: cls for cls in Modifier.__subclasses__()}


def parse_variable_modifiers(**kwargs):
    """ Identifiers the Modifier to use given the Args.
     
     Kwargs:
        The modifiers of the variable.
        
     Returns:
        A Modifier.
     """
    keys = kwargs.keys()
    mods = [i for i in keys if i in DEFAULT_MODIFIERS.keys()]
    if len(mods) > 0:
        return DEFAULT_MODIFIERS[mods[0]](**kwargs)
    else:
        return DEFAULT_MODIFIERS['default'](**kwargs)
