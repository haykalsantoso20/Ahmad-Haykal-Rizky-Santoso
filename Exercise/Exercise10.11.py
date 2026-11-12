from pathlib import Path
import json

number = input("Apa angka favoritmu? ")

path = Path("favorite_number.json")
contents = json.dumps(number)
path.write_text(contents)

print("Angkamu sudah disimpan.")