data = ["Kia", "Kia", "Mazda", "Ford"]

cars = {}

for auto in data:
    if cars.get(auto):
        cars[auto] += 1
    else:
        cars[auto] = 1

for auto in cars:
    print(f"{auto}: {cars[auto]}")