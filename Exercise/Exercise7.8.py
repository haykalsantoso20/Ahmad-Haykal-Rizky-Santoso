sandwich_orders = ['tuna', 'ayam', 'telur', 'keju']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"Saya sudah membuat sandwich {current_order}.")
    finished_sandwiches.append(current_order)

print("\nSandwich yang sudah selesai dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")