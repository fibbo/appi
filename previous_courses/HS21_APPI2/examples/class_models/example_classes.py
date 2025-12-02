
class Kurse:               
    def language(self):
        print("Shape is an abstract class. Does not have a language.")
    
    def mode(self):
        print("Shape is an abstract class. Does not have a mode.")
    
    def duration(self):
        print("Shape is an abstract class. Does not have a duration.")


class Programming(Kurse):
    def __init__(self, language, mode, duration):
        self.language = language
        self.mode = mode
        self.duration = duration

    def get_language(self):
        return self.language
    
    def get_mode(self):
        return self.mode

    def get_duration(self):
        return self.duration

veranstaltung = Programming("eng","premises", 120)
print(veranstaltung.get_language())
print(veranstaltung.get_mode())
print(veranstaltung.get_duration())