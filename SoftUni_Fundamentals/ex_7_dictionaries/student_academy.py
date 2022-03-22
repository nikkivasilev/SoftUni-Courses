number_of_lines = int(input())
student_dict = {}

for _ in range(number_of_lines):
    current_student = input()
    current_grade = float(input())

    if current_student not in student_dict:
        student_dict[current_student] = []
    student_dict[current_student].append(current_grade)

for key, value in student_dict.items():
    current_sum = 0
    for num in range(len(value)):
        current_sum += value[num]
    total = current_sum / len(value)
    student_dict[key] = total

for key, value in student_dict.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")
