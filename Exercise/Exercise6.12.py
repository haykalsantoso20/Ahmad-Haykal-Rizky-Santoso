cities = {
    'surakarta': {
        'country': 'Indonesia',
        'population': '520 ribu',
        'language': 'Jawa dan Indonesia',
        'landmarks': ['Keraton Surakarta', 'Pasar Gede', 'Galabo'],
        'fact': 'Dikenal sebagai kota batik dan pusat budaya Jawa.',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': '14 juta',
        'language': 'Jepang',
        'landmarks': ['Tokyo Tower', 'Shibuya Crossing'],
        'fact': 'Salah satu kota terbesar di dunia.',
    },
    'paris': {
        'country': 'Prancis',
        'population': '2,1 juta',
        'language': 'Prancis',
        'landmarks': ['Menara Eiffel', 'Louvre', 'Notre-Dame'],
        'fact': 'Menara Eiffel berdiri di kota ini.',
    },
}

for city, info in cities.items():
    print(f"\n=== {city.title()} ===")
    print(f"Negara   : {info['country']}")
    print(f"Populasi : {info['population']}")
    print(f"Bahasa   : {info['language']}")
    print(f"Fakta    : {info['fact']}")
    print("Landmark :")
    for landmark in info['landmarks']:
        print(f"  - {landmark}")