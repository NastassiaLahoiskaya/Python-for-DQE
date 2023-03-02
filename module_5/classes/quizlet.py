import random


class Quiz:
    def __init__(self, answer):
        self.answer = answer
        rand_num_list = [random.randrange(1, 100) for i in range(1)]
        self.question = f'How do you think? ----------\nWho will win the fight: Batman or Spider-Man\n{self.answer}\n' \
                        f'probability: {rand_num_list[0]} %\n\n'

    def print_question_into_file(self):
        ptf = open("list_of_actions.txt", "a")
        print(self.question, file=ptf)
        ptf.close()
