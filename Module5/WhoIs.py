import random
from PrintMessage import PrintMessage


class WhoIs:
    def __init__(self, answer):
        self.answer = answer

    def ask_question(self):
        rand_num_list = [random.randrange(1, 100) for i in range(1)]
        question = f'How do you think? ----------\nWho will win the fight: Batman or Spider-Man\n{self.answer}\nprobability: {rand_num_list[0]} %\n\n'
        self.prt = PrintMessage(question)
        prt = self.prt
        prt.print_message()
