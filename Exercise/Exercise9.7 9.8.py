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
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Hak akses admin:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):

    def __init__(self, first_name, last_name, age, location, occupation):
        super().__init__(first_name, last_name, age, location, occupation)
        self.privileges = Privileges()  # instance sebagai atribut


admin = Admin("Dewi", "Lestari", 31, "Semarang", "Administrator")
admin.privileges.show_privileges()