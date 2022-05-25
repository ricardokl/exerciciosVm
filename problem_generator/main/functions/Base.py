"""
__PATH__ = problem_generator/main/functions/Base.py

This file creates an abstract class to create another modifiers to be applied on variables.

"""


class Modifier:
    """ A Base Class to Create Modifiers. """
    KWARGS = []

    def __init__(self, **kwargs):
        """ Initialize the Modifier. """
        self.args = {}
        self.set_args(**kwargs)

    def set_args(self, **kwargs):
        """ Set all Given Args. """
        for key, value in kwargs.items():
            if key in self.KWARGS:
                self.args[key] = value

    def generate(self, **kwargs):
        """ Generates a Random Value. """
        raise NotImplementedError('Needs to be Implemented.')
