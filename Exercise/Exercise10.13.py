from pathlib import Path
import json

path = Path("user_info.json")

if path.exists():
    user = json.loads(path.read_text())
    print("Saya ingat tentang kamu:")
else:
    user = {
        "username": input("Siapa namamu? "),
        "age": input("Berapa umurmu? "),
        "city": input("Di kota mana kamu tinggal? "),
    }
    path.write_text(json.dumps(user))
    print("Informasimu sudah disimpan. Ini yang saya ingat:")

print(f"- Nama: {user['username']}")
print(f"- Umur: {user['age']}")
print(f"- Kota: {user['city']}")