import random


city_name = ['Paris', 'Londom', 'Rome', 'Berlin', 'Madrid']

city_temp = {city:random.randint(20, 30) for city in city_name}
# print(city_temp)

above_23 = {city: temp for city, temp in city_temp.items() if temp > 23}
print(above_23)