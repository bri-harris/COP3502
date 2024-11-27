class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"{self.odometer} miles driven")

    def update_odometer(self,mileage):
        if mileage<self.odometer:
            print('Invalid')
        else:
            self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles

