import os
import json
from classes.advertising import Advertising
from classes.file_reader import FileHandler
from classes.json_reader import JsonHandler
from classes.news import News
from classes.quizlet import Quiz
from classes.words_count import WordsCount
from classes.letters_count import LettersCount
from classes.xml_reader import XmlHandler


def main():
    while True:
        print('What do you want to choose?', '1 - News', '2 - Private Ad', '3 - Quizlet',
              '4 - Copying messages from file', '5 - Calculate number of words and letters',
              '6 - Add data from json file', '7 - Add data from xml file', '8 - Nothing', sep='\n')
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
                    f'If you want to ingest your file to default directory - '
                    f'C:/Users/Nastassia_Lahoiskaya/PycharmProjects/Python-for-DQE/'
                    f'fix_news_applications/list_of_actions.txt - enter 1,\n '
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
            word_count = WordsCount("list_of_actions.txt", 'word_count.csv')
            word_count.read_file()
            word_count.count_words()
            word_count.write_to_csv()
            letters_count = LettersCount("list_of_actions.txt", 'letter_count.csv')
            letters_count.read_file()
            letters_count.count_letters()
            letters_count.write_to_csv()
            print('word_count.csv and letter_count.csv files are updated')
            break
        elif flag == '6':
            input_file_path = input('Input file name where to read from: ')
            while os.path.exists(input_file_path) is False:
                input_file_path = input("File doesn't exists - input another file name: ")
            answer = 0
            while (answer == 1 or answer == 2) is False:
                answer = int(input(
                    f'If you want to ingest your file to default directory - '
                    f'C:/Users/Nastasia_Lahoiskaya/PycharmProjects/Python-for-DQE/'
                    f'fix_news_applications/list_of_actions.txt - enter 1,\n '
                    f'if you want to change it - enter 2: '))
            if answer == 1:
                output_file_path = f'{os.getcwd()}/list_of_actions.txt'
            else:
                output_file_path = input('Input file name where to write: ')
            json_reader = JsonHandler(input_file_path, output_file_path)
            json_reader.read_file()
            json_reader.format_json()
            json_reader.delete_input_file()
        elif flag == '7':
            input_file_path = input('Input file name where to read from: ')
            while os.path.exists(input_file_path) is False:
                input_file_path = input("File doesn't exists - input another file name: ")
            answer = 0
            while (answer == 1 or answer == 2) is False:
                answer = int(input(
                    f'If you want to ingest your file to default directory - '
                    f'C:/Users/Nastasia_Lahoiskaya/PycharmProjects/Python-for-DQE/'
                    f'fix_news_applications/list_of_actions.txt - enter 1,\n '
                    f'if you want to change it - enter 2: '))
            if answer == 1:
                output_file_path = f'{os.getcwd()}/list_of_actions.txt'
            else:
                output_file_path = input('Input file name where to write: ')
            xml_reader = XmlHandler(input_file_path, output_file_path)
            xml_reader.read_file()
            xml_reader.format_xml()
            xml_reader.delete_input_file()
        elif flag == '8':
            print('Stop')
            break
        else:
            print('Try again')


if __name__ == "__main__":
    main()
