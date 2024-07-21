names = ['Hanna', 'Jenny', 'Alex', 'Sam']
ages = [23, 25, 22, 24]
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']


for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")  # Hanna is 23 years old and lives in New York ....

zip_list = list(zip(names, ages, cities))
print(zip_list)  # [('Hanna', 23, 'New York'), ('Jenny', 25, 'Los Angeles'), ('Alex', 22, 'Chicago'), ('Sam', 24, 'Houston')]

for name, age, city in zip_list:
    print(f"{name} is {age} years old and lives in {city}")


brands = ['Apple', 'Samsung', 'Sony', 'Nokia']
products = ['iPhone', 'Galaxy', 'Xperia', 'Lumia']

zip_list = list(zip(brands, products))