from PrintMessage import PrintMessage
import datetime


class Advertising:
    def __init__(self, adv_message, actual_until=None):
        self.adv_message = adv_message
        self.actual_until = actual_until

    def advertising(self):
        message = f'Private Ad ------------------\n{self.adv_message}\nActual until: {self.actual_until}, {(datetime.datetime.strptime(self.actual_until, "%d/%m/%y") - datetime.datetime.now()).days} days left\n\n'
        self.prt = PrintMessage(message)
        prt = self.prt
        prt.print_message()