guest_list = ["Haykal", "Kelvin", "Dimas", "Budi",
              "Teddy", "Afif", "B.J. Habibie"]

print("Maaf, meja baru tidak tiba tepat waktu. Saya hanya bisa mengundang dua orang.\n")

# Keluarkan tamu satu per satu sampai tersisa dua
removed = guest_list.pop()
print(f"{removed}, maaf, saya tidak bisa mengundang Anda makan malam.")

removed = guest_list.pop()
print(f"{removed}, maaf, saya tidak bisa mengundang Anda makan malam.")

removed = guest_list.pop()
print(f"{removed}, maaf, saya tidak bisa mengundang Anda makan malam.")

removed = guest_list.pop()
print(f"{removed}, maaf, saya tidak bisa mengundang Anda makan malam.")

print()

# Dua tamu yang masih diundang
print(f"{guest_list[0]}, Anda masih diundang makan malam.")
print(f"{guest_list[1]}, Anda masih diundang makan malam.")

# Kosongkan list dengan del
del guest_list[0]
del guest_list[0]

print(f"\nIsi list sekarang: {guest_list}")