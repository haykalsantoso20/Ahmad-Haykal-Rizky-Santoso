guests = input("Berapa orang dalam rombongan makan malam kamu? ")
guests = int(guests)

if guests > 8:
    print("Maaf, kamu harus menunggu meja.")
else:
    print("Mejamu sudah siap.")