from Prac08.taxi import Car
from Prac08.taxi import Taxi
from Prac08.unreliableCar import UnreliableCar

def main():
    trip = Taxi("Prius1", 100)
    trip.drive(40)
    print(trip)
    print("Current Fare: ${:.2f}".format(trip.get_fare()))
    trip.start_fare()
    trip.drive(100)
    print(trip)
    print("Current Fare: ${:.2f}".format(trip.get_fare()))
    # trip = UnreliableCar("Vroom", 100, 75)
    # trip.drive(40)
    # print(trip)
main()