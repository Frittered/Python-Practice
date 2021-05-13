class TextEdit:
    def __init__(self):
        user_input = input('Enter your input for editing: ')
        self.user_input = user_input
        self.get_string()
        self.print_upper()
    def get_string(self):
        return print(str(self.user_input))
    def print_upper(self):
        output_upper = self.user_input.upper()
        return print(output_upper)
x = TextEdit()
x
