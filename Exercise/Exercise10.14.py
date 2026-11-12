from pathlib import Path
import json


def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        return json.loads(contents)
    else:
        return None


def get_new_username(path):
    username = input("Siapa namamu? ")
    path.write_text(json.dumps(username))
    return username


def greet_user():
    path = Path("username.json")
    username = get_stored_username(path)

    if username:
        correct = input(f"Apakah kamu {username}? (y/n) ")
        if correct.lower() == "y":
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu, {username}!")


greet_user()