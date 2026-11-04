mountains = ["Merapi", "Semeru", "Rinjani", "Bromo"]
print(f"List awal: {mountains}")

# Mengakses elemen
print(f"Elemen pertama: {mountains[0]}")
print(f"Elemen terakhir: {mountains[-1]}")

# Mengubah elemen
mountains[0] = "Merbabu"
print(f"Setelah diubah: {mountains}")

# Menambah elemen
mountains.append("Kerinci")
mountains.insert(1, "Sindoro")
print(f"Setelah append dan insert: {mountains}")

# Menghapus elemen
removed = mountains.pop()
print(f"pop() mengeluarkan: {removed}")

removed = mountains.pop(0)
print(f"pop(0) mengeluarkan: {removed}")

del mountains[0]
print(f"Setelah del mountains[0]: {mountains}")

mountains.remove("Bromo")
print(f"Setelah remove('Bromo'): {mountains}")

mountains.extend([]) if False else None
mountains.append("Slamet")
mountains.append("Lawu")
print(f"List untuk diurutkan: {mountains}")

# Mengurutkan
print(f"sorted(): {sorted(mountains)}")
print(f"List asli: {mountains}")

mountains.sort()
print(f"sort(): {mountains}")

mountains.sort(reverse=True)
print(f"sort(reverse=True): {mountains}")

mountains.reverse()
print(f"reverse(): {mountains}")

# Panjang list
print(f"Jumlah gunung: {len(mountains)}")