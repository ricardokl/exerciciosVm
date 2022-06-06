""" problem_generator.main.modifiers.Base

This package contains the base Modifier.

TODO:
-
-
-
"""

from typing import Type

from numexpr import evaluate


class Modifier:
    """ A Base Class to Create Modifiers. """
    KWARGS = []
    FORMATTER_KWARGS = []

    PARSER = 'base'

    def __init__(self, **kwargs):
        """ Initialize the Modifier.

        Kwargs:
            The modifier arguments and it's values.
        """
        self.args = {}
        self.fmt_args = {}
        self.set_args(**kwargs)

    def set_args(self, **kwargs) -> None:
        """ Set All Given Variables.

        Kwargs:
            The modifier arguments and it's values.
        """
        for key, value in kwargs.items():
            if key in self.KWARGS:
                self.args[key] = value

            if key in self.FORMATTER_KWARGS:
                self.fmt_args[key] = value

    def generate(self, **kwargs) -> str:
        """ Generates a Random Value.

        [Abstract Method]
        Needs to be implemented.

        Returns:
            A random value.
        """
        raise NotImplementedError('Needs to be Implemented.')

    def formatter(self, value) -> str:
        """ Returns the Random Value Formatted.

        Args:
            value: The random value.

        Returns:
            [str] A random value formatted.
        """
        return str(value)

    @staticmethod
    def parser(value, type_: Type = int, **kwargs) -> any:
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
