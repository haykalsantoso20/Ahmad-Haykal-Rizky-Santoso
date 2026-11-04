car = 'subaru'
name = 'Budi'
number = 10
age_0 = 22
age_1 = 18
cars = ['audi', 'bmw', 'subaru', 'toyota']

# 1. Kesetaraan dan ketidaksetaraan string
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'bmw'? I predict False.")
print(car == 'bmw')
print("\nIs car != 'bmw'? I predict True.")
print(car != 'bmw')
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

# 2. Menggunakan lower()
print("\nIs name.lower() == 'budi'? I predict True.")
print(name.lower() == 'budi')
print("\nIs name.lower() == 'Budi'? I predict False.")
print(name.lower() == 'Budi')

# 3. Tes numerik
print("\nIs number == 10? I predict True.")
print(number == 10)
print("\nIs number == 5? I predict False.")
print(number == 5)

print("\nIs number != 5? I predict True.")
print(number != 5)
print("\nIs number != 10? I predict False.")
print(number != 10)

print("\nIs number > 5? I predict True.")
print(number > 5)
print("\nIs number > 10? I predict False.")
print(number > 10)

print("\nIs number < 15? I predict True.")
print(number < 15)
print("\nIs number < 10? I predict False.")
print(number < 10)

print("\nIs number >= 10? I predict True.")
print(number >= 10)
print("\nIs number >= 11? I predict False.")
print(number >= 11)

print("\nIs number <= 10? I predict True.")
print(number <= 10)
print("\nIs number <= 9? I predict False.")
print(number <= 9)

# 4. Kata kunci and dan or
print("\nIs age_0 >= 21 and age_1 >= 18? I predict True.")
print(age_0 >= 21 and age_1 >= 18)
print("\nIs age_0 >= 21 and age_1 >= 21? I predict False.")
print(age_0 >= 21 and age_1 >= 21)

print("\nIs age_0 >= 21 or age_1 >= 21? I predict True.")
print(age_0 >= 21 or age_1 >= 21)
print("\nIs age_0 < 18 or age_1 >= 21? I predict False.")
print(age_0 < 18 or age_1 >= 21)

# 5. Item ada di dalam list
print("\nIs 'toyota' in cars? I predict True.")
print('toyota' in cars)
print("\nIs 'honda' in cars? I predict False.")
print('honda' in cars)

# 6. Item tidak ada di dalam list
print("\nIs 'honda' not in cars? I predict True.")
print('honda' not in cars)
print("\nIs 'audi' not in cars? I predict False.")
print('audi' not in cars)