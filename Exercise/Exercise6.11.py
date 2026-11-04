cities = {
    'surakarta': {
        'country': 'Indonesia',
        'population': '520 ribu',
        'fact': 'Dikenal sebagai kota batik dan pusat budaya Jawa.',
    },
    'tokyo': {
        'country': 'Jepang',
        'population': '14 juta',
        'fact': 'Salah satu kota terbesar di dunia.',
    },
    'paris': {
        'country': 'Prancis',
        'population': '2,1 juta',
        'fact': 'Menara Eiffel berdiri di kota ini.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Negara: {info['country']}")
    print(f"  Populasi: {info['population']}")
    print(f"  Fakta: {info['fact']}")