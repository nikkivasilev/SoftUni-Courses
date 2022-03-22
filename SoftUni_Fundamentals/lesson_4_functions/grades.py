def grade_text(grade_num):
    if grade_num < 3:
        print("Fail")
    elif grade_num < 3.50:
        print(f"Poor")
    elif grade_num < 4.50:
        print("Good")
    elif grade_num < 5.50:
        print("Very Good")
    else:
        print("Excellent")


current_grade = float(input())

grade_text(current_grade)
