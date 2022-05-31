
from problem_generator.main.modifiers.Base import Modifier
from problem_generator.main.modifiers.Random import RandomValue


class MultiplierValue(Modifier):
    KWARGS = [
        'anchor',
        'multi',
    ]

    FORMATTER_KWARGS = RandomValue.FORMATTER_KWARGS

    ANCHOR_DEFAULT = 0
    MULTI_DEFAULT = 1

    PARSER = 'multi'

    def __init__(self, **kwargs) -> None:
        super(MultiplierValue, self).__init__(**kwargs)

    def generate(self, **kwargs) -> str:
        anchor = self.parse(self.args.get('anchor', self.ANCHOR_DEFAULT), type_=float, **kwargs)
        multi = self.parse(self.args.get('div', self.MULTI_DEFAULT), type_=float, **kwargs)
        return anchor * multi

    def formatter(self, value) -> str:
        return RandomValue(**self.fmt_args).formatter(value=value)
