from Prac08.taxi import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random = randint(1, 101)
        if random < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return "Car won't start!"
