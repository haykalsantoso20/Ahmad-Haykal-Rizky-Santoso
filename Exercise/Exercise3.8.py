locations = ["Jepang", "Islandia", "Peru", "Maroko", "Selandia Baru"]

print("Urutan asli:")
print(locations)

print("\nsorted() urutan abjad:")
print(sorted(locations))

print("\nList setelah sorted() (masih urutan asli):")
print(locations)

print("\nsorted() urutan abjad terbalik:")
print(sorted(locations, reverse=True))

print("\nList setelah sorted() terbalik (masih urutan asli):")
print(locations)

locations.reverse()
print("\nSetelah reverse() pertama:")
print(locations)

locations.reverse()
print("\nSetelah reverse() kedua (kembali ke urutan asli):")
print(locations)

locations.sort()
print("\nSetelah sort() (abjad):")
print(locations)

locations.sort(reverse=True)
print("\nSetelah sort(reverse=True) (abjad terbalik):")
print(locations)