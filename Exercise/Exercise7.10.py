responses = {}

polling_active = True

while polling_active:
    name = input("\nSiapa namamu? ")
    place = input("Kalau kamu bisa mengunjungi satu tempat di dunia, "
                  "kamu ingin pergi ke mana? ")

    responses[name] = place

    repeat = input("Apakah ada orang lain yang mau mengisi? (ya/tidak) ")
    if repeat == 'tidak':
        polling_active = False

print("\n--- Hasil Polling ---")
for name, place in responses.items():
    print(f"{name.title()} ingin pergi ke {place.title()}.")