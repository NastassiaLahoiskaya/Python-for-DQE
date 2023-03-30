import os
from .news import News
from .advertising import Advertising
from .quizlet import Quiz
import xml.etree.ElementTree as ET


class XmlHandler:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.content_from_file = ''
        self.formatted_text = ''

    def read_file(self):
        tree = ET.parse(self.input_file_path)
        root = tree.getroot()
        self.content_from_file = root.findall("./block")

    def format_xml(self):
        for field in self.content_from_file:
            if field.get("type") == 'News':
                news = News(field.find('text').text, field.find('location').text)
                self.formatted_text += news.news
            elif field.get("type") == 'Private Ad':
                advertising = Advertising(field.find('text').text, field.find('date').text)
                self.formatted_text += advertising.message
            elif field.get("type") == 'Quizlet':
                quizlet = Quiz(field.find('answer').text)
                self.formatted_text += quizlet.question
            else:
                print('Some unknown type of records was found')
                self.content_from_file = 'Empty'
                break
        with open(self.output_file_path, "a") as file_txt:
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
