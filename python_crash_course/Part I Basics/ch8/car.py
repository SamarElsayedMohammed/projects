class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    #2)Modifying an Attribute’s Value Through a Method
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
my_new_car = Car('audi', 'a4', 2019)
#my_new_car.year =2010
my_new_car.odometer_reading = 23 #Modifying an Attribute’s Value Directly
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(20)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()