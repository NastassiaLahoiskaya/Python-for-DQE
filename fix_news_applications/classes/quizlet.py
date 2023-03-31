import random


class Quiz:
    def __init__(self, answer, conclusion=None):
        self.answer = answer
        self.conclusion = conclusion or [random.randrange(1, 100) for i in range(1)]
        self.question = f'\n' \
                        f'How do you think? ----------\nWho will win the fight: Batman or Spider-Man\n{self.answer}\n' \
                        f'probability: {self.conclusion[0]} %\n\n'

    def print_question_into_file(self):
        with open("list_of_actions.txt", "a") as opened_file:
            opened_file.write(self.question)
