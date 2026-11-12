from random import choice

pool = (1, 3, 5, 7, 9, 12, 15, 18, 21, 25, "A", "B", "C", "D", "E")


def draw_ticket():
    ticket = []
    while len(ticket) < 4:
        item = choice(pool)
        if item not in ticket:
            ticket.append(item)
    return ticket


my_ticket = [3, 7, 21, "C"]
winning_ticket = draw_ticket()

attempts = 0
while set(winning_ticket) != set(my_ticket):
    winning_ticket = draw_ticket()
    attempts += 1

print(f"Tiket saya: {my_ticket}")
print(f"Tiket pemenang: {winning_ticket}")
print(f"Butuh {attempts} kali undian sampai tiketku menang.")