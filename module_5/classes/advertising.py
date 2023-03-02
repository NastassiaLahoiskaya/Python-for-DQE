import datetime


class Advertising:
    def __init__(self, adv_message, actual_until=None):
        self.adv_message = adv_message
        self.actual_until = actual_until
        self.message = f'Private Ad ------------------\n{self.adv_message}\nActual until: {self.actual_until}, ' \
                       f'{(datetime.datetime.strptime(self.actual_until, "%d/%m/%y") - datetime.datetime.now()).days} days left\n\n'

    def print_advertising_into_file(self):
        ptf = open("list_of_actions.txt", "a")
        print(self.message, file=ptf)
        ptf.close()
