class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Mobil ini sudah menempuh {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Kamu tidak boleh memundurkan odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini punya baterai {self.battery_size} kWh.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"Mobil ini bisa menempuh sekitar {range} mil dengan daya penuh.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai di-upgrade ke 65 kWh.")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.get_range()      # sebelum upgrade
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()      # sesudah upgrade