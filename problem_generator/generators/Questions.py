
from os import listdir
from os.path import isfile, join
from random import randint, choice
from string import Formatter

from problem_generator.generators.functions.Parser import modifier_parse


class Question:
    def __init__(self, template_path: str, initialize: bool = True):
        """ Initialize the Question.

        TODO:
        - Remove the templates variable to another function.
        - Accept modifiers variables as values from other variables (Queue system)
        """
        self.templates = [join(template_path, x) for x in listdir(template_path) if isfile(join(template_path, x))]
        self.question_path = None
        self.question_raw = None
        self.question_with_values = None
        self.args = {}
        self.variables = {}

        if initialize:
            self.choose()

    def choose(self, force: bool = False) -> None:
        """ Choose a Random Question on Template Path.

        Args:
            force: Force the Object to Select a New Question (Use it as Last Resource).
        """
        if not self.question_raw or force:
            self.question_path = choice(self.templates)
            with open(self.question_path, 'r') as file:
                self.question_raw = file.read().strip()

            self.get_args_and_variables()

    def get_args_and_variables(self) -> None:
        """ Set the String Format Args to a Dictionary. """
        if self.question_raw:
            args = [fn for _, fn, _, _ in Formatter().parse(self.question_raw) if fn is not None]
            for arg in args:
                values = arg.split('|')
                if not values[0] in self.args.keys():
                    self.args[values[0]] = {'modifiers': None}

                if len(values) > 1:
                    self.question_raw = self.question_raw.replace(arg, values[0])
                    mods = [i.split('=') for i in values[1].split(';')]
                    mods_to_dict = {mod[0].strip(): mod[1] for mod in mods}
                    if self.args[values[0]].get('modifiers', None):
                        self.args[values[0]]['modifiers'].update(mods_to_dict)

                    else:
                        self.args[values[0]]['modifiers'] = mods_to_dict

                self.variables[values[0]] = {'value': None}
                self.variables[values[0]]['generator'] = modifier_parse(self.args[values[0]]['modifiers'])

    def randomize(self) -> None:
        """ Randomize the Variables. """
        if self.question_raw and self.args:
            for variable, values in self.variables.items():
                self.variables[variable]['value'] = values['generator'].generate()

    def mrv(self, vmax: int = 100, xmax: int = 500, dtmax: int = 6) -> None:
        self.variables['v0'] = randint(-vmax, vmax)
        self.variables['t0'] = randint(0, 18*4) / 4
        self.variables['deltat'] = randint(1, dtmax*4) / 4
        self.variables['tf'] = self.variables['t0'] + self.variables['deltat']
        self.variables['x0'] = randint(-xmax*4, xmax*4)/4
        self.variables['x1'] = self.variables['v0'] * self.variables['deltat'] + self.variables['x0']
        self.variables['obj'] = choice(['carro', 'trem', 'moto', 'caminhão'])
        self.variables['deltax'] = self.variables['x1'] - self.variables['x0']

        self.apply()

    def apply(self) -> None:
        """ Apply the variables to the question. """
        variables = {key: value['value'] for key, value in self.variables.items()}
        self.question_with_values = self.question_raw.format(**variables)


