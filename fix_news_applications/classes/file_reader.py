import os
import re
from task_4.task_4_3 import normalization_text as normalize_text
from . import db_handler
from .news import News
from .quizlet import Quiz
from .advertising import Advertising


class FileHandler:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.content_from_file = ''
        self.db_handler = db_handler

    def read_file(self):
        with open(self.input_file_path, "r", encoding='utf-8') as file:
            self.content_from_file = file.read()

    def write_to_file(self):
        with open(self.output_file_path, "a", encoding='utf-8') as file:
            file.write(self.content_from_file)

    def delete_input_file(self):
        os.remove(self.input_file_path)

    def normalize_text(self):
        self.content_from_file = '\n'.join(filter(None, map(str.strip, self.content_from_file.split('\n'))))

    def write_to_database(self):
        lines = self.content_from_file.split('\n\n')
        for line in lines:
            fields = line.split('\n')
            if fields[0] == 'News -------------------------':
                news = News(fields[1], fields[2])
                self.db_handler.insert_news(news)
            elif fields[0] == 'Private Ad ------------------':
                advertising = Advertising(fields[1], fields[2])
                self.db_handler.insert_advertising(advertising)
            elif fields[0] == 'How do you think? ----------':
                quiz = Quiz(fields[1], fields[2], fields[3])
                self.db_handler.insert_quiz(quiz)
