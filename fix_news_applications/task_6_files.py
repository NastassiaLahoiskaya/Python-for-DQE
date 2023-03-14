import os

from classes.advertising import Advertising
from classes.file_reader import FileHandler
from classes.news import News
from classes.quizlet import Quiz
from classes.words_count import WordsCount
from classes.letters_count import LettersCount


def main():
    while True:
        print('What do you want to choose?', '1 - News', '2 - Private Ad', '3 - Quizlet',
              '4 - Copying messages from file', '5 - Nothing', sep='\n')
        flag = input('Choose the appropriate number: ')
        if flag == '1':
            news = News(input('Please enter news text\n'), input('Please enter location\n'))
            news.print_news_into_file()
        elif flag == '2':
            advng = Advertising(input('Please enter advertisement text\n'),
                                input('Please enter expire date in the format dd/mm/yy\n'))
            advng.print_advertising_into_file()
        elif flag == '3':
            question = Quiz(input('Who will win the fight: Batman or Spider-Man? Please enter your assumption\n'))
            question.print_question_into_file()
        elif flag == '4':
            input_file_path = input('Input file name where to read from: ')
            while os.path.exists(input_file_path) is False:
                input_file_path = input("File doesn't exists - input another file name: ")
            answer = 0
            while (answer == 1 or answer == 2) is False:
                answer = int(input(
                    f'If you want to ingest your file from default directory - enter 1, '
                    f'if you want to change it - enter 2: '))
            if answer == 1:
                output_file_path = f'{os.getcwd()}/list_of_actions.txt'
            else:
                output_file_path = input('Input file name where to write: ')
            file_handler = FileHandler(input_file_path, output_file_path)
            file_handler.read_file()
            file_handler.normalize_text()
            file_handler.write_to_file()
            file_handler.delete_input_file()
        elif flag == '5':
            print('Stop')
            break
        else:
            print('Try again')


if __name__ == "__main__":
    main()
