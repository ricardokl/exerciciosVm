
from problem_generator.main.Lists import ListOfQuestions
from problem_generator.main.Questions import Question


if __name__ == '__main__':
    Q = ListOfQuestions(path='src/templates/cinemática/velocidade-media', number_of_questions=2)
    for q in Q.questions:
        print(q)
        print(q.answer())
        print('\n')
