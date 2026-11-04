prompt = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "
active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Saya akan menambahkan {topping} ke pizzamu.")