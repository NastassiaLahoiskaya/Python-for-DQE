from News import News
from Advertising import Advertising
from WhoIs import WhoIs


class Choice:
    def __init__(self, flag):
        self.flag = flag

    def choose_message_type(self):
        if self.flag == '1':
            self.news = News(input('Please enter news text\n'), input('Please enter location\n'))
            news_msg = self.news
            news_msg.news_message()
        elif self.flag == '2':
            self.advng = Advertising(input('Please enter advertisement text\n'), input('Please enter expire date in the format dd/mm/yy\n'))
            adv_message = self.advng
            adv_message.advertising()
        elif self.flag == '3':
            self.question = WhoIs(input('Who will win the fight: Batman or Spider-Man? Please enter your assumption\n'))
            question_mess = self.question
            question_mess.ask_question()
        else:
            print('Your choice is not correct')
