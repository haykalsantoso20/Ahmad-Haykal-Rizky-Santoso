class User:
    """Model profil pengguna."""

    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation

    def describe_user(self):
        print(f"Nama lengkap: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Lokasi: {self.location}")
        print(f"Pekerjaan: {self.occupation}")

    def greet_user(self):
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")


user_1 = User("Budi", "Santoso", 25, "Surakarta", "Programmer")
user_2 = User("Siti", "Rahayu", 30, "Yogyakarta", "Desainer")
user_3 = User("Andi", "Wijaya", 22, "Jakarta", "Mahasiswa")

for user in (user_1, user_2, user_3):
    user.describe_user()
    user.greet_user()
    print()