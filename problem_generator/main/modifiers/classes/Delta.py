""" problem_generator.main.modifiers.Delta

"""

from problem_generator.main.modifiers.Base import Modifier
from problem_generator.main.modifiers.classes.Random import RandomValue


class DeltaValue(Modifier):
    KWARGS = [
        'anchor',
        'delta'
    ]

    FORMATTER_KWARGS = RandomValue.FORMATTER_KWARGS

    ANCHOR_DEFAULT = 0
    DELTA_DEFAULT = 0

    PARSER = 'delta'

    def __init__(self, **kwargs) -> None:
        super(DeltaValue, self).__init__(**kwargs)

    def generate(self, **kwargs) -> str:
        anchor = self.parser(self.args.get('anchor', self.ANCHOR_DEFAULT), type_=float, **kwargs)
        delta = self.parser(self.args.get('delta', self.DELTA_DEFAULT), type_=float, **kwargs)
        return anchor + delta

    def formatter(self, value) -> str:
        return RandomValue(**self.fmt_args).formatter(value=value)
