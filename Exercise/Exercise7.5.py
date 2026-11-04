prompt = "\nBerapa umurmu? (ketik 'quit' untuk selesai): "

while True:
    age = input(prompt)

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Tiketmu gratis.")
    elif age <= 12:
        print("Harga tiketmu $10.")
    else:
        print("Harga tiketmu $15.")