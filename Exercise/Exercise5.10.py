current_users = ['admin', 'John', 'budi', 'Sari', 'dewi']
new_users = ['JOHN', 'andi', 'SARI', 'rina', 'Eko']

# Salinan huruf kecil dari current_users untuk perbandingan
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: the username is already used. Please enter a new username.")
    else:
        print(f"{new_user}: the username is available.")