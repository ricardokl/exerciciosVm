""" problem_generator.main.modifiers.Utils

This package contains useful and important functions to deal with modifiers.

TODO:
- Functions without brackets!
"""


from string import Formatter
from typing import Tuple, Union, Dict, Type

from problem_generator import MOD_INIT, MOD_EQUAL, MOD_SEPARATOR, FUNC_INIT
from problem_generator.main.Utils import get_connections
from problem_generator.main.modifiers.Base import Modifier
from problem_generator.main.modifiers.Parser import parse_variable_modifiers


def parse_argument(value, type_: Type = float, **kwargs) -> any:
    """ Parser the Argument Value to a Type.

    This method parser a string value to another type, and changes the
    other variables names to it's random value.

    Args:
        value: The argument value.
        type_: The desired type.

    Kwargs:
        The other variables modifiers.

    Returns:
        [float or type_]
    """
    connections = get_connections(value, list(kwargs.keys()), index=False)
    for c in connections:
        value = value.replace(c, str(kwargs[c]))

        return type_()

    return type_(value)


    variables = [i for i in kwargs.keys() if i in str(value)]
    if kwargs.get(value, False):
        try:
            return float(kwargs[value])
        except ValueError:
            return kwargs[value]

    elif variables:
        expression = value
        for var in variables:
            expression = expression.replace(var, str(kwargs[var]))

        return float(evaluate(expression))

    return type_(value)


def get_metadata(text: str) -> Tuple[dict, dict, str]:
    """ Get all Values in the Metadata Section.

    This method will collect all the information contained in metadata section, including variables
    definitions, global modifiers and a answer function.

    Args:
        text: The text containing the variables.

    Returns:
        [dict, dict, str] The clean text and all variables.

    """
    variables = {}
    modifiers = {}
    function = ''

    lines = text.split('\n')

    for line in lines:
        if MOD_INIT in line:
            values = line.split(MOD_INIT)

            if len(values) == 1 or not values[0]:
                continue

            name = values[0].strip()
            variables[name] = {'modifiers': {}}

            modifiers = [i.split('=') for i in values[1].split(MOD_SEPARATOR)]
            modifiers_to_dict = {mod[0].strip(): mod[1].strip() for mod in modifiers}
            variables[name]['modifiers'] = modifiers_to_dict

        elif line.startswith(FUNC_INIT):
            function = line[2:].strip()

        elif MOD_EQUAL in line:
            values = line.split(MOD_EQUAL)
            if len(values) == 1 or not values[0]:
                continue

            modifier = values[0].strip()
            value = values[1].strip()
            modifiers[modifier] = value

        else:
            continue

    return variables, modifiers, function


def get_clean_text_and_variables(text: str) -> Tuple[str, Dict[str, Union[dict, Modifier]]]:
    """ Get all Variables and Clean the Text.

    This method will gather all variables defined within brackets, and clean the text of the
    variables modifiers.

    Args:
        text: The text containing the variables.

    Returns:
        [str, dict] The clean text and all variables.
    """
    clean_text = text
    variables = {}

    variables_in_text = [fn for _, fn, _, _ in Formatter().parse(text) if fn is not None]

    for var in variables_in_text:
        values = var.split(MOD_INIT)
        name = values[0].strip()

        if len(values) == 1 or not name:
            clean_text = clean_text.replace('{'+values[0]+'}', '')
            continue

        if name not in variables.keys():
            variables[name] = {'modifiers': {}}

        if len(values) > 1:
            clean_text = clean_text.replace(var, name)

            modifiers = [i.split('=') for i in values[1].split(MOD_SEPARATOR)]
            modifiers_to_dict = {mod[0].strip(): mod[1].strip() for mod in modifiers}

            if variables[name].get('modifiers', {}):
                variables[name]['modifiers'].update(modifiers_to_dict)
            else:
                variables[name]['modifiers'] = modifiers_to_dict

    for name in variables:
        variables[name]['generator'] = parse_variable_modifiers(**variables[name]['modifiers'])

    return clean_text, variables
