from pathlib import Path

path = Path("learning_python.txt")

contents = path.read_text()
print("Cara 1: membaca seluruh file")
print(contents)

lines = contents.splitlines()
print("Cara 2: loop per baris")
for line in lines:
    print(line)