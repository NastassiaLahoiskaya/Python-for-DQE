import os
import json
from .news import News
from .advertising import Advertising
from .quizlet import Quiz


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
        with open(self.output_file_path, "w") as file_txt:
            for field in self.content_from_file:
                if field.get("type") == 'News':
                    news = News(field.get("text"), field.get("location"))
                    self.formatted_text = news.news
                elif field.get("type") == 'Private Ad':
                    advertising = Advertising(field.get("text"), field.get("date"))
                    self.formatted_text = advertising.message
                elif field.get("type") == 'Quizlet':
                    quizlet = Quiz(field.get("answer"))
                    self.formatted_text = quizlet.question
                else:
                    print('Some unknown type of records was found')
                    self.content_from_file = 'Empty'
                    break
                file_txt.write(self.formatted_text)

    def delete_input_file(self):
        input('The file was processed successfully. Do you want to delete it? 1 - yes, 2 - no: ')
        answer = 0
        while (answer == 1 or answer == 2) is False:
            answer = int(input('The file was saved '))
        if answer == 1:
            os.remove(self.input_file_path)
            print('The file was deleted ')
