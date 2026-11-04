my_foods = [
    "pizza", "falafel", "carrot cake", "cannoli",
    "ice cream", "nasi goreng", "sate ayam", "bakso",
]
friend_foods = my_foods[:]

my_foods.append("rendang")
friend_foods.append("gado-gado")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)