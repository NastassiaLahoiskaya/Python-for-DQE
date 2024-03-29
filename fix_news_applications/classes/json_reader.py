import os
import json
from . import db_handler
from .news import News
from .advertising import Advertising
from .quizlet import Quiz


class JsonHandler:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.content_from_file = ''
        self.formatted_text = ''
        self.db_handler = db_handler.DatabaseHandler()

    def read_file(self):
        with open(self.input_file_path) as json_file:
            self.content_from_file = json.load(json_file)

    def format_json(self):
        with open(self.output_file_path, "a") as file_txt:
            for field in self.content_from_file:
                if field.get("type") == 'News':
                    news = News(field.get("text"), field.get("location"))
                    self.formatted_text = news.news
                    self.db_handler.insert_news(news)
                elif field.get("type") == 'Private Ad':
                    advertising = Advertising(field.get("text"), field.get("date"))
                    self.formatted_text = advertising.message
                    self.db_handler.insert_advertising(advertising)
                elif field.get("type") == 'Quizlet':
                    quizlet = Quiz(field.get("answer"))
                    self.formatted_text = quizlet.question
                    self.db_handler.insert_quiz(quizlet)
                else:
                    print('Some unknown type of records was found')
                    self.content_from_file = 'Empty'
                    break
                file_txt.write(self.formatted_text)

    def delete_input_file(self):
        answer = int(input('The file was processed successfully. Do you want to delete it? 1 - yes, 2 - no: '))
        while answer not in (1, 2):
            answer = int(input('Invalid input. '
                               'The file was processed successfully. Do you want to delete it? 1 - yes, 2 - no: '))
        if answer == 1:
            os.remove(self.input_file_path)
            print('The file was deleted')
        else:
            print('The file was saved')

    def close_db_connection(self):
        self.db_handler.close()
