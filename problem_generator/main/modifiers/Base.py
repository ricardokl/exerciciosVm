""" problem_generator.main.modifiers.Base


"""

from typing import Type

from numexpr import evaluate


class Modifier:
    """ A Base Class to Create Modifiers. """
    KWARGS = []
    FORMATTER_KWARGS = []

    PARSER = 'base'

    def __init__(self, **kwargs):
        """ Initialize the Modifier. """
        self.args = {}
        self.fmt_args = {}
        self.set_args(**kwargs)

    def set_args(self, **kwargs):
        """ Set all given Args. """
        for key, value in kwargs.items():
            if key in self.KWARGS:
                self.args[key] = value

            if key in self.FORMATTER_KWARGS:
                self.fmt_args[key] = value

    def generate(self, **kwargs) -> str:
        """ Generates a Random Value Given the Args.

        Returns:
            A generated random value.
        """
        raise NotImplementedError('Needs to be Implemented.')

    def formatter(self, value) -> str:
        """ Change the Random Value to the Format.

        Args:
            value: The random value.

        Returns:
            A generated random value formatted.
        """
        return str(value)

    @staticmethod
    def parse(value, type_: Type = int, **kwargs) -> any:
        variables = [i for i in kwargs.keys() if i in str(value)]
        if kwargs.get(value, False):
            print(kwargs[value], '\n\n')
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
