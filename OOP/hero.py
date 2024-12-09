# Activity 1: Design your own class
class Superhero:
    def __init__(self, name, superpower, city):
        self.name = name
        self.superpower = superpower
        self.city = city

    def display_info(self):
        print(f"Superhero Name: {self.name}")
        print(f"Superpower: {self.superpower}")
        print(f"City: {self.city}")

    def use_superpower(self):
        print(f"{self.name} uses their superpower: {self.superpower}!")

hero1 = Superhero("Ivory", "Invisibility", "Adelaide")
hero1.display_info()
hero1.use_superpower()

#Inheritance layer
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, city, flight_speed):
        super().__init__(name, superpower, city)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} mph!")

flying_hero = FlyingSuperhero("Skylar", "Flight", "Geneva", 300)
flying_hero.display_info()
flying_hero.use_superpower()
flying_hero.fly()


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass # This will be overriden in subclasses

class Car(Vehicle):
    def move(self):
        print("Driving.")

class Plane(Vehicle):
    def move(self):
        print("Flying.")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling.")

# List of vehicles
vehicles = [Car(), Plane(), Bicycle()]

for v in vehicles:
    v.move()