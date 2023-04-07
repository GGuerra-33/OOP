class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_people()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_people(cls):
        cls.number_of_people += 1


p1 = Person("Cristiano")
p2 = Person("Lionel")
print(Person.number_of_people_())
