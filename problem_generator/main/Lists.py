

from typing import Union

from problem_generator.main.Questions import Question


class QuestionList:
    def __init__(self, templates: Union[str, list], n_questions: int = 5, init: bool = True):
        """ Initialize the Question List.

        Args:
            templates: A Template Path or a List of Templates Path containing the Questions.
            n_questions: Number of Questions of the List
        """
        self.templates = templates
        self.questions = []
        self.n_questions = n_questions

        if init:
            self.generate()

    def generate(self) -> list:
        """ Generates a List of Questions.

        Returns:
            A List containing the Generated Questions.
        """
        self.questions.clear()

        for _ in range(self.n_questions):
            self.questions.append(Question(self.templates))

        return self.questions

    def randomize(self) -> list:
        """ Randomizes the Questions of the List.

        Returns:
            A List containing the Questions Randomized.
        """
        for question in self.questions:
            question.randomize()

        return self.questions

    def copy_questions(self, questions: list) -> None:
        paths = [q.question_path for q in questions]
        new_questions = []

        for path in paths:
            q = Question(templates_path='')


class MultipleVersions:
    def __init__(self, templates: Union[str, list], n_questions: int = 5, n_versions: int = 2, init: bool = True):
        self.templates = templates
        self.questions = []
        self.n_questions = n_questions
        self.n_versions = n_versions
        self.lists = []

        if init:
            self.init()

    def init(self, apply: bool = True) -> QuestionList:
        """ Generates a Base Question List.

        All the versions will use the same questions from the base question list, but with random variables.

        TODO:
        - This may be not the best method to generates all the versions, or how it's stored, but for now it's
        enough, and will generate great randomized question lists.

        Args:
            apply: If True generates all the other question lists.

        Returns:
            The Base Question List.
        """
        self.lists.clear()

        base = QuestionList(templates=self.templates, n_questions=self.n_questions)
        self.lists.append(base)
        self.questions = base.questions

        if apply:
            self.generate()

        return self.lists[0]

    def randomize(self) -> list:
        pass

    def generate(self) -> list:
        """ Generates all the Question Lists Versions. """
        if not self.lists:
            self.init(apply=False)

        base = self.lists[0]
        questions = base.questions.copy()
        for _ in range(self.n_versions - 1):
            version = QuestionList(templates=self.templates, init=False)
            version.questions = base.questions.copy()
            version.randomize()

            self.lists.append(version)

        return self.lists
