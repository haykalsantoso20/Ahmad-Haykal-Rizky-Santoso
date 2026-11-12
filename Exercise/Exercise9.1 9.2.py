class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka. Silakan masuk!")


restaurant = Restaurant("Warung Solo", "Masakan Jawa")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


restaurant_1 = Restaurant("Warung Solo", "Masakan Jawa")
restaurant_2 = Restaurant("Sushi Tei", "Jepang")
restaurant_3 = Restaurant("Padang Sederhana", "Masakan Padang")

restaurant_1.describe_restaurant()
print()
restaurant_2.describe_restaurant()
print()
restaurant_3.describe_restaurant()