from random import choice

pool = (1, 3, 5, 7, 9, 12, 15, 18, 21, 25, "A", "B", "C", "D", "E")

winning_ticket = []
while len(winning_ticket) < 4:
    item = choice(pool)
    if item not in winning_ticket:
        winning_ticket.append(item)

print("Tiket apa pun yang cocok dengan 4 angka/huruf berikut menang hadiah!")
print(winning_ticket)