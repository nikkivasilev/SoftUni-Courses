from math import floor
number_of_tournaments = int(input())
starting_points = int(input())
w = 2000
f = 1200
sf = 720
average_points = 0
total_points = starting_points
tournaments_won = 0
for _ in range(number_of_tournaments):
    current_tournament = input()
    if current_tournament == "W":
        total_points += w
        tournaments_won += 1
    elif current_tournament == "F":
        total_points += f
    elif current_tournament == "SF":
        total_points += sf

average_points = floor((total_points - starting_points) / number_of_tournaments)
winnage_percent = (tournaments_won / number_of_tournaments) * 100
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{winnage_percent:.2f}%")
