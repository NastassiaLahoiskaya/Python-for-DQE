import csv
import re


class WordsCount:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def write_to_csv(self):
        with open(self.input_file, 'r') as read_txt:
            data_to_read = read_txt.read()
            row = data_to_read.lower()
            list_with_numbers = re.findall(r'\w+', row)
            output_list = [x for x in list_with_numbers if not any(i.isdigit() for i in x)]
            read_txt.close()

        count_dict = {}
        for i in output_list:
            count_dict[i] = output_list.count(i)
            read_txt.close()

        with open(self.output_file, 'w', encoding='UTF8', newline='') as csvfile:
            for key, value in count_dict.items():
                writer = csv.writer(csvfile, delimiter='-')
                writer.writerow([key, output_list.count(key)])
            csvfile.close()
