from PrintMessage import PrintMessage
import datetime


class News:
    def __init__(self, news_msg, location):
        self.news_msg = news_msg
        self.location = location

    def news_message(self):
        message = f'News -------------------------\n{self.news_msg}\n{self.location}, {datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n\n'
        self.prt = PrintMessage(message)
        prt = self.prt
        prt.print_message()
