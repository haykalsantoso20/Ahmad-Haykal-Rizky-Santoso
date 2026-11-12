from random import sample

pool = (1, 3, 5, 7, 9, 12, 15, 18, 21, 25, "A", "B", "C", "D", "E")
winning_ticket = sample(pool, 4) 
print(winning_ticket)