X = "\nMasukkan topping pizza (ketik 'quit' untuk selesai): "

while True:
    topping = input(X)

    if topping == 'quit':
        break
    else:
        print(f"Saya akan menambahkan {topping} ke pizzamu.")