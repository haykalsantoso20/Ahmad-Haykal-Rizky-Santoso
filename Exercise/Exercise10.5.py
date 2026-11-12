from pathlib import Path

names = []

print("Ketik 'q' untuk berhenti.")
while True:
    name = input("Siapa namamu? ")
    if name == "q":
        break
    names.append(name)
    print(f"Terima kasih, {name}!")

contents = "\n".join(names)
path = Path("guest_book.txt")
path.write_text(contents)

print(f"{len(names)} nama sudah ditulis ke guest_book.txt")