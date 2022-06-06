
import operator

from problem_generator.parser.Node import Node, TokenType
from problem_generator.parser.Parser import parse


operations = {
    TokenType.PLUS: operator.add,
    TokenType.MINUS: operator.sub,
    TokenType.MULTI: operator.mul,
    TokenType.DIV: operator.truediv,
    TokenType.POW: operator.pow
}


def compute(node: Node) -> float:
    if node.token_type == TokenType.NUM:
        return node.value

    left = compute(node.children[0])
    right = compute(node.children[1])
    operation = operations[node.token_type]

    return operation(left, right)


def evaluate(value: str) -> float:
    print(value)
    return compute(parse(value))
