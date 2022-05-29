""" problem_generator.main.Utils

This package contains useful functions to use on the project.

TODO:
- Accept multiple variables on modifiers.
"""

import numpy as np

from os import listdir
from os.path import isfile, join
from typing import Union


def get_all_templates(path: Union[str, list]):
    if isinstance(path, (list, tuple)):
        templates = []
        for p in path:
            templates.extend([
                join(p, x) for x in listdir(p) if isfile(join(p, x))
            ])

    elif isinstance(path, str):
        templates = [
            join(path, x) for x in listdir(path) if isfile(join(path, x))
        ]

    else:
        templates = []

    return templates


def order_queue(mods: dict) -> list:
    """ Get the order to generate the modifiers values.

    Args:
       mods: The modifiers dictionary.

    Returns:
        A list containing the modifiers order.
    """
    if not verify_modifiers(mods=mods):
        raise ValueError('Variables are creating a Loop.')

    variables = list(mods.keys())
    queue = []
    for var in mods.keys():
        values = mods[var].values()
        bounds = [i for i in values if i in variables]
        if bounds:
            if var in bounds:
                raise ValueError(f'{var} depends on it self.')

            indexes = [queue.index(i) for i in bounds if i in queue]
            if indexes:
                queue.insert(max(indexes)+1, var)
            else:
                queue.insert(-1, var)
        else:
            queue.insert(0, var)

    return queue


def verify_modifiers(mods: dict) -> bool:
    """ Verify the Modifiers Values if it's not Create a Loop.

    This function creates a correlation matrix with the variables from the modifier dictionary, and
    calculates it's determinant. If the determinant is zero, it will create a loop.

    Args:
        mods: The modifiers dictionary.

    Returns:
        True if it's verified, else False
    """
    variables = list(mods.keys())
    n = len(variables)
    connections = np.diag(np.full(n, 1))
    for i, var in enumerate(variables):
        values = mods[var].values()
        connections[i][i] = 1
        connects_to = [variables.index(i) for i in values if i in variables]
        for c in connects_to:
            connections[i][c] = 1

    det = np.linalg.det(connections)
    if det == 0:
        return False

    return True
