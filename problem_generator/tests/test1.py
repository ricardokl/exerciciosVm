
from pprint import pprint
from problem_generator.generators import Questions


if __name__ == '__main__':
    q = Questions.Question('t')
    q.choose()
    q.randomize()
    pprint(q.variables)
    q.apply()
    pprint(q.question_with_values)
