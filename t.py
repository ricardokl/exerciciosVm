
from problem_generator.main.Lists import ListOfQuestions

if __name__ == '__main__':
    Q = ListOfQuestions(path='src/templates/cinemática/velocidade-media', number_of_questions=2)
    for q in Q.questions:
        print(q)
        print('\n')
