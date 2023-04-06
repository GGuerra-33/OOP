
class Car:
    def drive(self):
        print("This animal is eating")


class Volkswagen(Car):
    def drive(self):
        print("I am a shitty driver")

volks = Volkswagen()
volks.drive()