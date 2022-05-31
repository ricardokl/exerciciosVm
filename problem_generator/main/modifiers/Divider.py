
from problem_generator.main.modifiers.Base import Modifier
from problem_generator.main.modifiers.Random import RandomValue


class DividerValue(Modifier):
    KWARGS = [
        'anchor',
        'div',
    ]

    FORMATTER_KWARGS = RandomValue.FORMATTER_KWARGS

    ANCHOR_DEFAULT = 0
    DIV_DEFAULT = 1

    PARSER = 'div'

    def __init__(self, **kwargs) -> None:
        super(DividerValue, self).__init__(**kwargs)

    def generate(self, **kwargs) -> str:
        anchor = self.parse(self.args.get('anchor', self.ANCHOR_DEFAULT), type_=float, **kwargs)
        div_ = self.parse(self.args.get('div', self.DIV_DEFAULT), type_=float, **kwargs)
        if div_ == 0:
            div_ = self.DIV_DEFAULT

        return anchor/div_

    def formatter(self, value) -> str:
        return RandomValue(**self.fmt_args).formatter(value=value)
