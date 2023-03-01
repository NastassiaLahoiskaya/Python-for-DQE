from Choice import Choice


def main():
    make_your_choice = Choice(input('Please enter your choice:\n1 for News message\n2 for Advertisement\n3 for Question of a day\n'))
    make_your_choice.choose_message_type()


if __name__ == "__main__":
    main()
