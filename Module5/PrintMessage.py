class PrintMessage:
    def __init__(self, message):
        self.message = message

    def print_message(self):
        ptf = open("List_of_actions.txt", "a")
        print(self.message, file=ptf)
        ptf.close()
