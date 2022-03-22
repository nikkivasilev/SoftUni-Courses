courses_dict = {}


while True:
    command = input()

    if command == 'End':
        break
    command = command.split(" -> ")
    course = command[0]
    student = command[1]

    if course not in courses_dict:
        courses_dict[course] = []
    if student not in courses_dict[course]:
        courses_dict[course].append(student)

for key, value in courses_dict.items():
    print(f"{key}")
    for i in value:
        print(f"-- {i}")
