favorite_numbers = {
    'budi': [7, 21],
    'Haykal': [12, 3, 9],
    'andi': [3],
    'Dimas': [21, 5],
    'Rusdi': [9, 14, 1],
}

for name, numbers in favorite_numbers.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(number)