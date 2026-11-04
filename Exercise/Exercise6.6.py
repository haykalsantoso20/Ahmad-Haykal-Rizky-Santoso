favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

people = ['jen', 'budi', 'sarah', 'andi', 'phil', 'dewi']

for person in people:
    if person in favorite_languages:
        print(f"Terima kasih {person.title()}, sudah mengisi polling!")
    else:
        print(f"{person.title()}, kamu diundang untuk mengisi polling bahasa favorit.")