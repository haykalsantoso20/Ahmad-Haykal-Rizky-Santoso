class User:

    def __init__(self, first_name, last_name, age, location, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.occupation = occupation
        self.login_attempts = 0  

    def describe_user(self):
        print(f"Nama lengkap: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Lokasi: {self.location}")
        print(f"Pekerjaan: {self.occupation}")

    def greet_user(self):
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")

    def increment_login_attempts(self):
        """Menambah login_attempts sebanyak 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Mengembalikan login_attempts ke 0."""
        self.login_attempts = 0


user = User("Budi", "Santoso", 25, "Surakarta", "Programmer")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Percobaan login: {user.login_attempts}")

user.reset_login_attempts()
print(f"Percobaan login: {user.login_attempts}")