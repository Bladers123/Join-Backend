class view():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def show(self):
        print(self.name, self.age, self.gender)