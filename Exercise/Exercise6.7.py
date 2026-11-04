person_1 = {
    'first_name': 'Haykal',
    'last_name': 'Santoso',
    'age': 20,
    'city': 'Surakarta',
}
person_2 = {
    'first_name': 'Ahmad',
    'last_name': 'Dhani',
    'age': 22,
    'city': 'Yogyakarta',
}
person_3 = {
    'first_name': 'Andi',
    'last_name': 'Pratama',
    'age': 19,
    'city': 'Semarang',
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name}, umur {person['age']}, tinggal di {person['city']}.")