from car import Car
class Battery:
    def __init__(self,battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        if self.battery_size ==40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"Car's range is {range} miles on full charge.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()