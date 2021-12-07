"""
A small module for illustrating the inheritance

**The module structure is the following:**

- The ``Vehicle`` main class to create vehicle object
- The ``Motorcycle`` child class, inherit from Vehicle, has 2 seats
- The ``Convoy`` class, bunch of vehicles

"""

from typing import Union, Callable, Optional, Tuple, List

class Vehicle:
    """Create a vehicle with a number of seats and list of passengers name
    
    Parameters
    ----------
        n_seats : int
            the number of seats
        passengers : List[str]
            the passengers name

        
    Attributes
    ----------
    seats : int
        the number of seats
    passengers : List[str]
        the passengers name
    """
    def __init__(self, n_seats: int, passengers: List[str] = []):
        self.seats = n_seats
        self.passengers = passengers

    def print_passengers(self):
        """Print the passengers name
        """
        for i in range(len(self.passengers)):
            print(self.passengers[i])

    def add(self, name):
        """Add a passenger

        Parameters
        ----------
        name : str
            passenger's name to add
        """
        self.passengers.append(name)


class Motorcycle(Vehicle):
    """Motorcycle class, child of Vehicle. Only two seat.
    You can declare the passenger and driver name

    Parameters
    ----------
        n_seats : int
            the number of seats
        names_list : list of string
        
        
    Attributes
    ----------
    seats : int
        the number of seats
    passengers : List[str]
        the passengers name
    """
    def __init__(self, brand: str, n_seats: int = 2, passengers: List[str] = []):
        Vehicle.__init__(self, n_seats=n_seats, passengers=passengers)
        self.seats = 2
        self.passengers = passengers
        self.brand = brand

    def add(self, name):
        """Add a passenger, if there is a seat left

        Parameters
        ----------
        name : str
            passenger's name
        """

        if len(self.passengers) < self.seats:
            self.passengers.append(name)
            print('There are', self.seats - len(self.passengers), 'seats left.')
        else:
            print("The vehicle is full.")


class Convoy:
    """Convoy class, contains one or more vehicles
    
    Attributes
    ----------
    vehicle_list : List[Callable]
        list of vehicle instances
    length : int
        the convoy length, number of vehicles
    """
    def __init__(self):
        self.vehicle_list = [Vehicle(n_seats=4)]  # the main vehicle
        self.length = 1  # the main vehicle is the only one at initialization

    def add_vehicle(self, vehicle):
        """Add a vehicle to the convoy

        Parameters
        ----------
        vehicle : Callable
            a vehicle instance
        """
        self.vehicle_list.append(vehicle)
        self.length += 1
