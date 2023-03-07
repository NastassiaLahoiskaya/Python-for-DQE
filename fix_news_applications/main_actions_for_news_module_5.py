import os

from classes.advertising import Advertising
from classes.news import News
from classes.quizlet import Quiz
from fix_news_applications.main_write_new_news_module_6 import NewsReader


if __name__ == "__main__":
    while True:
        print('What do you want to choose?', '1 - News', '2 - Private Ad', '3 - Quizlet',
              '4 - Copying messages from file', '5 - Nothing', sep='\n')
        flag = input('Choose the appropriate number: ')
        if flag == '1':
            news = News(input('Please enter news text\n'), input('Please enter location\n'))
            news.print_news_into_file()
        elif flag == '2':
            advng = Advertising(input('Please enter advertisement text\n'), input('Please enter expire date in the format dd/mm/yy\n'))
            advng.print_advertising_into_file()
        elif flag == '3':
            question = Quiz(input('Who will win the fight: Batman or Spider-Man? Please enter your assumption\n'))
            question.print_question_into_file()
        elif flag == '4':
            f_contents, path_for_remove = NewsReader().read_news_from_another_file()
            with open("new_message.txt", "a", encoding='utf-8') as file:
                for line in f_contents:
                    file.write(line)
            print(f'This file {path_for_remove} will be removed now\n')
            os.remove(path_for_remove)
        elif flag == '5':
            print('Stop')
            break
        else:
            print('Try again')

