from math import floor

first_time = int(input())
second_time = int(input())
third_time = int(input())

time_sum_in_seconds = first_time + second_time + third_time

minutes = time_sum_in_seconds // 60
seconds = time_sum_in_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f'{minutes}:{seconds}')