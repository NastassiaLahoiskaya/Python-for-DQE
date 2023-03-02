import datetime


class News:
    def __init__(self, news_msg, location):
        self.news_msg = news_msg
        self.location = location
        self.news = f'News -------------------------\n{self.news_msg}\n{self.location}, ' \
                    f'{datetime.datetime.now().strftime("%d/%m/%y %H:%M")}\n\n'

    def print_news_into_file(self):
        ptf = open("list_of_actions.txt", "a")
        print(self.news, file=ptf)
        ptf.close()
