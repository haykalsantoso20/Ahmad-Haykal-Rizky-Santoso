number = input("Masukkan sebuah angka: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} adalah kelipatan 10.")
else:
    print(f"{number} bukan kelipatan 10.")