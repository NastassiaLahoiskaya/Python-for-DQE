import os
import json
from classes.news import News
from classes.advertising import Advertising
from classes.quizlet import Quiz
from task_4.task_4_3 import normalization_text as normalize_text


class JsonHandler:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.content_from_file = ''
        self.formatted_text = ''

    def read_file(self):
        with open(self.input_file_path) as json_file:
            self.content_from_file = json.load(json_file)

    def format_json(self):
        for field in self.content_from_file:
            if field.get("type") == 'News':
                news = News(field.get("text"), field.get("location"))
                self.formatted_text = normalize_text(news.get_news())
                with open(self.output_file_path + "/news.txt", "w") as f:
                    f.write(self.formatted_text)
            elif field.get("type") == 'Private Ad':
                advertising = Advertising(field.get("text"), field.get("date"))
                self.formatted_text = normalize_text(advertising.get_advertising())
                with open(self.output_file_path + "/advertising.txt", "w") as f:
                    f.write(self.formatted_text)
            elif field.get("type") == 'Quizlet':
                quizlet = Quiz(field.get("question"), field.get("answer"), field.get("conclusion"))
                self.formatted_text = normalize_text(quizlet.get_question())
                with open(self.output_file_path + "/quiz.txt", "w") as f:
                    f.write(self.formatted_text)
            else:
                print('Some unknown type of records was found')
                self.content_from_file = 'Empty'
                break

    def delete_input_file(self):
        if self.content_from_file != 'Empty':
            answer = 0
            while (answer == 1 or answer == 2) is False:
                answer = int(input('The file was processed successfully. Do you want to delete it? 1 - yes, 2 - no: '))
            if answer == 1:
                os.remove(self.input_file_path)
                print('The file was deleted ')
