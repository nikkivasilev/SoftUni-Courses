jury_quantity = int(input())
total_average_points = 0
total_presentations = 0
current_average = 0
finish = False
presentation_name = input()
while presentation_name != "Finish":
    for n in range(jury_quantity):
        current_score = float(input())
        current_average += current_score / jury_quantity
    total_average_points += current_average
    print(f"{presentation_name} - {current_average:.2f}.")
    total_presentations += 1
    current_average = 0
    presentation_name = input()
average = total_average_points / total_presentations
print(f"Student's final assessment is {average:.2f}.")