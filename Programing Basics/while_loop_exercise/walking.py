target_steps = 10000
total_steps = 0
while total_steps < target_steps:
    command = input()
    if command == "Going home":
        coming_back = int(input())
        total_steps += coming_back
        break
    current_steps = int(command)
    total_steps += current_steps
diff = abs(total_steps - target_steps)
if total_steps >= target_steps:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")