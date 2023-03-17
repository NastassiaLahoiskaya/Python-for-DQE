import re
import csv


class LettersCount:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.string_united = ''
        self.count_dict = ''

    def read_file(self):
        with open(self.input_file, 'r') as read_txt:
            data_to_read = read_txt.read()
            full_text = data_to_read.lower()
            list_with_numbers = re.findall(r'\w+', full_text)
            output_list = [x for x in list_with_numbers if not any(i.isdigit() for i in x)]
            self.string_united = ''.join(output_list)
            self.string_united = list(self.string_united)

    def count_letters(self):
        self.count_dict = {}
        for i in self.string_united:
            self.count_dict[i] = self.string_united.count(i)

    def write_to_csv(self):
        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            count_letters = len(self.string_united)
            for key, value in self.count_dict.items():
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow([key, self.string_united.count(key), '', round(self.string_united.count(key)/count_letters*100, 2)])
            csvfile.close()
