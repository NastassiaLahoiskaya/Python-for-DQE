import csv
import re


class WordsCount:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.output_list = ''
        self.read_txt = ''
        self.count_dict = ''

    def read_file(self):
        with open(self.input_file, 'r') as read_txt:
            data_to_read = read_txt.read()
            full_lower_text = data_to_read.lower()
            list_with_numbers = re.findall(r'\w+', full_lower_text)
            self.output_list = [x for x in list_with_numbers if not any(i.isdigit() for i in x)]

    def count_words(self):
        self.count_dict = {}
        for i in self.output_list:
            self.count_dict[i] = self.output_list.count(i)

    def write_to_csv(self):
        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            for key, value in self.count_dict.items():
                writer = csv.writer(csvfile, delimiter='-')
                writer.writerow([key, self.output_list.count(key)])
            csvfile.close()

