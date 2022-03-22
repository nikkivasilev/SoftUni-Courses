numbers = list(map(int, input().split(", ")))
max_group = 10


while bool(numbers):
    current_group = [num for num in numbers if num <= max_group]
    for num in current_group:
        if num in numbers:
            numbers.remove(num)
    print(f"Group of {max_group}'s: {current_group}")
    max_group += 10
    current_group = []
