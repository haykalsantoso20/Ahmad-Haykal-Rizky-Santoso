print("Kalkulator penjumlahan. Ketik 'q' untuk berhenti.")

while True:
    first = input("\nMasukkan angka pertama: ")
    if first == "q":
        break

    second = input("Masukkan angka kedua: ")
    if second == "q":
        break

    try:
        result = int(first) + int(second)
    except ValueError:
        print("Maaf, kamu harus memasukkan angka, bukan teks.")
    else:
        print(f"Hasil penjumlahan: {result}")