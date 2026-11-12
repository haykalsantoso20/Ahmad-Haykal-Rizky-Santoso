from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


print("Dadu 6 sisi:")
die_6 = Die()
for _ in range(10):
    die_6.roll_die()

print("\nDadu 10 sisi:")
die_10 = Die(10)
for _ in range(10):
    die_10.roll_die()

print("\nDadu 20 sisi:")
die_20 = Die(20)
for _ in range(10):
    die_20.roll_die()