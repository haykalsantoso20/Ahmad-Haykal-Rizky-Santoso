try:
    first = int(input("Masukkan angka pertama: "))
    second = int(input("Masukkan angka kedua: "))
except ValueError:
    print("Maaf, kamu harus memasukkan angka, bukan teks.")
else:
    print(f"Hasil penjumlahan: {first + second}")