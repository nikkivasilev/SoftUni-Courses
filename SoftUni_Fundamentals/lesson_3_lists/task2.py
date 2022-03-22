def courses(number_of_courses):
    courses_list = []
    for current_course in range(number_of_courses):
        courses_list.append(input())
    return courses_list


number = int(input())
print(courses(number))
