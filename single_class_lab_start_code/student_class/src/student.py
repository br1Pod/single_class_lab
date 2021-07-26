
class Student:
    def __init__(self, name, cohort):

        # initialise instance variables
        self.name = name
        self.cohort = cohort

    def talk(self):
        return "I can talk!"


    def say_favourite_language(self, fave_lang):
        return ("I love " + fave_lang)
    