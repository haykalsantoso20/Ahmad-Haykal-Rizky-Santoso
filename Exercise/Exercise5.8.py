usernames = ['admin', 'jaden', 'budi', 'sari', 'dewi']

# 5-8: sapa setiap user
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
