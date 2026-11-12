from pathlib import Path

filenames = ["pg1342.txt"]  # ganti sesuai file milikmu

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
        continue

    lowered = contents.lower()
    count_the = lowered.count("the")
    count_the_space = lowered.count("the ")

    print(f"{filename}:")
    print(f"  'the'  muncul {count_the} kali")
    print(f"  'the ' muncul {count_the_space} kali")