import os
from task_4.task_4_3 import normalization_text as normalize_text


class FileHandler:
    def __init__(self, input_file_path, output_file_path):
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.content_from_file = ''

    def read_file(self):
        with open(self.input_file_path, "r", encoding='utf-8') as file:
            self.content_from_file = file.read()

    def write_to_file(self):
        with open(self.output_file_path, "a", encoding='utf-8') as file:
            file.write(self.content_from_file)

    def delete_input_file(self):
        os.remove(self.input_file_path)

    def normalize_text(self):
        self.content_from_file = normalize_text(self.content_from_file)

