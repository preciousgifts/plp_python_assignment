# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def show_identity(self):
        print(f"I am {self.name} from the {self.universe} universe. My power is {self.power}!")

    def use_power(self):
        print(f"{self.name} uses their power: {self.power}!")

# Subclass
class FlyingHero(Superhero):
    def __init__(self, name, power, universe, wingspan):
        super().__init__(name, power, universe)
        self.wingspan = wingspan

    def use_power(self):
        print(f"{self.name} soars through the sky with a wingspan of {self.wingspan} meters!")

# Another Subclass
class SpeedHero(Superhero):
    def __init__(self, name, power, universe, speed):
        super().__init__(name, power, universe)
        self.speed = speed

    def use_power(self):
        print(f"{self.name} runs at the speed of {self.speed} km/h!")

# Create instances
hero1 = FlyingHero("Falcon", "Flight", "Marvel", 3.5)
hero2 = SpeedHero("Flash", "Super Speed", "DC", 3000)

# Call methods
hero1.show_identity()
hero1.use_power()

hero2.show_identity()
hero2.use_power()

