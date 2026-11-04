def describe_city(city, country='Indonesia'):
    """Menampilkan kalimat sederhana tentang sebuah kota."""
    print(f"{city.title()} ada di {country.title()}.")


describe_city('surakarta')
describe_city('yogyakarta')
describe_city('tokyo', 'jepang')