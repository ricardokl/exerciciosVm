""" problem_generator.main.modifiers.Base


"""

from typing import Type


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

    def verify(self):
        as_string = [v for k, v in self.args.items() if isinstance(v, str)]
        return as_string

    @staticmethod
    def parse(value, type_: Type = int, **kwargs) -> any:
        if kwargs.get(value, False):
            return kwargs[value]

        return type_(value)
