class Prey:
    def Flee(self):
        print("This animal is scaping")

class Predator:
    def Hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass

class Wolf(Predator):
    pass

class Fish(Prey,Predator):
    pass



rabbit = Rabbit()
wolf = Wolf()
fish = Fish()


rabbit.Flee()