rivers = {
    'nil': 'mesir',
    'amazon': 'brasil',
    'yangtze': 'tiongkok',
}

for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui {country.title()}.")

print("\nSungai-sungai dalam dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nNegara-negara dalam dictionary:")
for country in rivers.values():
    print(country.title())