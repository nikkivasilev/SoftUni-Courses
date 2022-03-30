number_of_cars = int(input())
cars_dict = {}
for _ in range(number_of_cars):
    current = input().split("|")
    car = current[0]
    mileage = int(current[1])
    fuel = int(current[2])
    cars_dict[car] = [mileage, fuel]

while True:
    command = input().split(" : ")

    if command[0] == "Stop":
        break

    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        needed_fuel = int(command[3])
        if cars_dict[car][1] < needed_fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car][0] += distance
            cars_dict[car][1] -= needed_fuel
            print(f"{car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        if cars_dict[car][0] >= 100000:
            del cars_dict[car]
            print(f"Time to sell the {car}!")
    elif command[0] == "Refuel":
        car = command[1]
        fueling_fuel = int(command[2])
        if fueling_fuel + cars_dict[car][1] >= 75:
            fueling_fuel = 75 - cars_dict[car][1]
        print(f"{car} refueled with {fueling_fuel} liters")
        cars_dict[car][1] += fueling_fuel

    elif command[0] == "Revert":
        car = command[1]
        kilometers = int(command[2])
        if cars_dict[car][0] - kilometers >= 10000:
            print(f"{car} mileage decreased by {kilometers} kilometers")
            cars_dict[car][0] -= kilometers
        else:
            cars_dict[car][0] = 10000

for car in cars_dict:
    mileage = cars_dict[car][0]
    fuel = cars_dict[car][1]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
