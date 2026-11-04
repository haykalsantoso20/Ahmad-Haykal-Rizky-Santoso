# 1. import module_name
import city_functions
print(city_functions.city_country('santiago', 'chile'))

# 2. from module_name import function_name
from city_functions import city_country
print(city_country('surakarta', 'indonesia'))

# 3. from module_name import function_name as fn
from city_functions import city_country as cc
print(cc('tokyo', 'jepang'))

# 4. import module_name as mn
import city_functions as cf
print(cf.city_country('paris', 'prancis'))

# 5. from module_name import *
from city_functions import *
print(city_country('bandung', 'indonesia'))