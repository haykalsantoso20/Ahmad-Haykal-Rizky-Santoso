class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka. Silakan masuk!")


class IceCreamStand(Restaurant):
    """Kedai es krim, turunan dari Restaurant."""

    def __init__(self, restaurant_name, cuisine_type="Es Krim"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print(f"Rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


stand = IceCreamStand("Es Krim Manis")
stand.flavors = ["Vanila", "Cokelat", "Stroberi", "Matcha"]

stand.describe_restaurant()
stand.display_flavors()