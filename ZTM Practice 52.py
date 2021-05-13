# Custom error class
class CustomizedError(Exception):
    
    def __init__(self, string, error):
        self.warning = f'I don\'t like {string}, so don\'t bring it around here'
        self.string = string
        self.error = error
        self.check_union_error()
    def check_union_error(self):
        if self.string in self.error:
            return print(self.warning)

a = CustomizedError('love', 'I love my pickles sweet and dill')
a
