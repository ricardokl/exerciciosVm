""" problem_generator.main.Questions

This packages defines the Question object.

TODO:
- For now the templates are collected by a path or a list of paths, and with a databases? Or texts?
- Use another variables as modifiers boundaries (Queue system).
"""

from random import choice
from string import Formatter

from numexpr import evaluate

from problem_generator import METADATA_INIT
from problem_generator.main.modifiers.Parser import modifier_parse
from problem_generator.main.Utils import get_metadata, get_order_queue, get_all_templates


class Question:
    def __init__(self) -> None:
        """ Initialize a Question. """
        self._raw = None
        self.meta = None
        self.path = None
        self.func = None
        self.mods = {}
        self.vars = {}
        self.fmt_vars = {}
        self.order = []

    @property
    def raw(self) -> str:
        return self._raw

    @raw.setter
    def raw(self, value) -> None:
        values = value.split(METADATA_INIT)
        if len(values) <= 1:
            meta = None
            raw = values[0]
        else:
            meta = values[0]
            raw = values[1]

        self.meta = meta
        self._raw = raw
        self._get_args_and_variables()

    def choose(self, templates: list, **kwargs):
        """ Choose a Random Template of a List of Templates.

        Args:
            templates: A list of templates.
            **kwargs: [
                collect: Receives a path or a list of paths of templates and collect it. [Build Only]
            ]

        Returns:
            None
       """
        if kwargs.get('collect', False):
            templates = get_all_templates(templates)

        self.path = choice(templates)
        with open(self.path, 'r', encoding='utf-8') as file:
            self.raw = file.read().strip()

        return self

    def randomize(self) -> str:
        """ Randomize the Variables.

        Uses the modifiers generators to randomize the variables of the question.

        Returns:
            The question text with the randomized variables.
        """
        if not self.mods:
            raise Warning('Modifiers are not defined.')

        values = [self.mods[v] for v in self.order]
        for key, val in zip(self.order, values):
            self.vars[key] = val['generator'].generate(**self.vars)
            self.fmt_vars[key] = val['generator'].formatter(self.vars[key])

        return self.raw.format(**self.fmt_vars)

    def answer(self) -> str:
        if self.raw and self.vars:
            expr = self.func
            return evaluate(expr.format(**self.vars))

        return ''

    def _get_args_and_variables(self) -> None:
        """ [PRIVATE] Set the String Format Args to a Dictionary.

        Scrape all the variables and it's modifiers of the question text.

        Returns:
            None
        """
        if not self._raw:
            return

        global_args, global_fmts, func = get_metadata(metadata=self.meta)
        self.func = func
        self.mods.update(global_args)

        args = [fn for _, fn, _, _ in Formatter().parse(self._raw) if fn is not None]
        for arg in args:
            values = arg.split('|')
            if len(values) == 1 and not values[0]:
                self._raw = self._raw.replace('{' + values[0] + '}', '')
                continue

            if values[0] not in self.mods.keys():
                self.mods[values[0]] = {'modifiers': {}}

            self.mods[values[0]]['modifiers'].update(global_fmts)

            if len(values) > 1:
                self._raw = self._raw.replace(arg, values[0])
                mods = [i.split('=') for i in values[1].split(';')]
                mods_to_dict = {mod[0].strip(): mod[1] for mod in mods}
                if self.mods[values[0]].get('modifiers', None):
                    self.mods[values[0]]['modifiers'].update(mods_to_dict)

                else:
                    self.mods[values[0]]['modifiers'] = mods_to_dict

            self.mods[values[0]]['generator'] = modifier_parse(**self.mods[values[0]]['modifiers'])

        order_dict = {key: values['modifiers'] for key, values in self.mods.items()}
        self.order = get_order_queue(order_dict)
        self.randomize()

    def __copy__(self):
        new = type(self)()
        new.__dict__.update(self.__dict__)
        return new

    def __repr__(self):
        if self.raw and self.vars:
            return self.raw.format(**self.fmt_vars)

        return None
