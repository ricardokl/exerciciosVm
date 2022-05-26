

from typing import Union

from problem_generator.main.Questions import Question


class ExerciseList:
    def __init__(self, templates_path: Union[str, list], number_of_questions: int = 5):
        """ Initialize the Exercise List. """
        self.templates_path = templates_path
        self.questions = []
        self.number_of_questions = number_of_questions

    def generate(self) -> None:
        """"""
        self.questions.clear()
        for _ in range(self.number_of_questions):
            self.questions.append(Question(self.templates_path))


class MultipleLists:
    def __init__(self):
        pass


class MultipleVersionsLists:
    def __init__(self):
        pass
