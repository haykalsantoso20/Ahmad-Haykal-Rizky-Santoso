favorite_places = {
    'budi': ['Candi Prambanan', 'Pantai Parangtritis'],
    'Haykal': ['Malioboro', 'Kebun Teh Kemuning', 'Bromo'],
    'andi': ['Lawang Sewu'],
}

for name, places in favorite_places.items():
    print(f"\nTempat favorit {name.title()}:")
    for place in places:
        print(f"- {place}")