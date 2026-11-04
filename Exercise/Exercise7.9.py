sandwich_orders = [
    'pastrami', 'tuna', 'pastrami', 'ayam', 'telur', 'pastrami', 'keju',
]
finished_sandwiches = []

print("Maaf, pastrami sudah habis.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"Saya sudah membuat sandwich {current_order}.")
    finished_sandwiches.append(current_order)

print("\nSandwich yang sudah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")