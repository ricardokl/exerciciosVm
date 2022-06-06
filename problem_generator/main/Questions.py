""" problem_generator.main.Questions

This packages contains the Question object.

TODO:
- Databases implementation.
- Own Parser
"""

from random import choice

from problem_generator import METADATA_INIT
from problem_generator.main.modifiers.Utils import get_clean_text_and_variables, get_metadata
from problem_generator.main.Utils import get_order_queue, get_all_templates
from problem_generator.parser.Compute import evaluate


class Question:
    def __init__(self) -> None:
        """ Initialize the Question Object. """
        self.text = None
        self.path = None
        self.function = None
        self.variables = {}
        self.values = {}
        self.values_formatted = {}
        self.order = []

        self._raw = None
        self._raw_metadata = None

    @property
    def raw(self) -> str:
        return self._raw

    @raw.setter
    def raw(self, value) -> None:
        values = value.split(METADATA_INIT)
        meta, raw = [None, *values] if len(values) <= 1 else [*values[:2]]

        self._raw_metadata = meta
        self._raw = raw
        self._set_variables()
        self._set_metadata(text=meta)
        self._set_order()
        self.randomize()

    def choose(self, templates: list, **kwargs) -> None:
        """ Choose a Random Template of a List of Templates.

        Args:
            templates: A list of templates.

        Kwargs:
            collect: Set True to collect all templates of a path or list of paths.
       """
        if kwargs.get('collect', False):
            templates = get_all_templates(templates)

        self.path = choice(templates)
        with open(self.path, 'r', encoding='utf-8') as file:
            self.raw = file.read().strip()

    def randomize(self) -> str:
        """ Randomize the Variables.

        Returns:
            [str] The text with the variables value.
        """
        if not self.variables:
            raise Warning('Modifiers are not defined.')

        values = [self.variables[v] for v in self.order]
        for key, val in zip(self.order, values):
            self.values[key] = val['generator'].generate(**self.values)
            self.values_formatted[key] = val['generator'].formatter(self.values[key])

        return self.text.format(**self.values_formatted)

    def answer(self) -> str:
        """ Given the Function and the Variables Values Returns the Answer.

        Returns:
            [str] The Formatted Answer.
        """
        if self.raw and self.values:
            expr = self.function
            return str(evaluate(expr.format(**self.values)))

        return ''

    def _set_variables(self) -> None:
        """ Get and Set the Variables and the Clean Text. """
        text, variables = get_clean_text_and_variables(self.raw)
        self.text = text
        self.variables = variables

    def _set_metadata(self, text: str) -> None:
        """ Get and Set the Metadata Information. """
        if not text:
            return

        variables, modifiers, function = get_metadata(text)
        self.function = function
        self.variables.update(variables)

        for var in self.variables.keys():
            for key, value in modifiers.items():
                if key not in self.variables[var]['modifiers'].keys():
                    self.variables[var]['modifiers'][key] = value

    def _set_order(self) -> None:
        """ Get and Set the Variables Definition Order. """
        order_dict = {key: values['modifiers'] for key, values in self.variables.items()}
        self.order = get_order_queue(order_dict)

    def __copy__(self):
        new = type(self)()
        new.__dict__.update(self.__dict__)
        return new

    def __repr__(self):
        if self.raw and self.values:
            return self.text.format(**self.values_formatted)

        return None


if __name__ == '__main__':
    x = Question()
    x.raw = """
    decimals=0\nf={x}+{v}*{t0}
    ---
    Velocidade {v|min=t0;max=20} e Posição {x|min=0;max=v+20}. Tempo {t0|max=5}
    """
    print(x)
    print(x.answer())
