# Class Inheritance
class Person:
    def __init__(self):
        self.gender = 'N/A'
    def get_gender(self):
        print(self.gender)
        print('I am a person too')

class Male(Person):
    def __init__(self):
        self.gender = 'Male'
    
class Female(Person):
    def __init__(self):
        self.gender = 'Female'
    
a = Male()
a.get_gender()
