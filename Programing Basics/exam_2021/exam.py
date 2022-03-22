total_students = int(input())
less_than_three = 0
less_than_four = 0
less_than_five = 0
five_and_up = 0
total_score = 0
for n in range(total_students):
    current_grade = float(input())
    total_score += current_grade
    if current_grade < 3:
        less_than_three += 1
    elif current_grade < 4:
        less_than_four += 1
    elif current_grade < 5:
        less_than_five += 1
    elif current_grade >= 5:
        five_and_up += 1
average_fail = less_than_three / total_students * 100
average_less_than_four = less_than_four / total_students * 100
average_less_than_five = less_than_five / total_students * 100
top_students = five_and_up / total_students * 100
average_score = total_score / total_students
print(f"Top students: {top_students:.2f}%")
print(f"Between 4.00 and 4.99: {average_less_than_five:.2f}%")
print(f"Between 3.00 and 3.99: {average_less_than_four:.2f}%")
print(f"Fail: {average_fail:.2f}%")
print(f"Average: {average_score:.2f}")
