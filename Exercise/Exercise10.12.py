from pathlib import Path
import json

path = Path("favorite_number.json")

if path.exists():
    contents = path.read_text()
    number = json.loads(contents)
    print(f"I know your favorite number! It's {number}.")
else:
    number = input("Apa angka favoritmu? ")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Angkamu sudah disimpan. Jalankan lagi untuk melihat hasilnya.")