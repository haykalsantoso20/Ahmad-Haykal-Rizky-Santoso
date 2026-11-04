pizzas = ["pepperoni", "margherita", "BBQ chicken"]
friend_pizzas = pizzas[:]

pizzas.append("four cheese")
friend_pizzas.append("hawaiian")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
