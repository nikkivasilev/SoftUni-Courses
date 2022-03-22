def coffee_counter(event):
    event_lower = ['coding', 'dog', 'cat', 'movie']
    event_upper = []
    for item in event_lower:
        event_upper.append(item.upper())
    count_of_coffee = 0
    while event != "END":
        if event in event_lower:
            count_of_coffee += 1
        elif event in event_upper:
            count_of_coffee += 2
        event = input()
    if count_of_coffee > 5:
        print("You need extra sleep")
    else:
        print(count_of_coffee)


first_event = input()
coffee_counter(first_event)
