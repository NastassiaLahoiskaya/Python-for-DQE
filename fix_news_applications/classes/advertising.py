import datetime


class Advertising:
    def __init__(self, adv_message, actual_until=None):
        self.adv_message = adv_message
        self.actual_until = actual_until
        self.message = f'Private Ad ------------------\n{self.adv_message}\n' \
                       f'Actual until: {self.actual_until}, ' \
                       f'{(datetime.datetime.strptime(self.actual_until, "%d/%m/%y") - datetime.datetime.now()).days} ' \
                       f'days left\n\n'

    def print_advertising_into_file(self):
        with open("list_of_actions.txt", "a") as opened_file:
            opened_file.write(self.message)
