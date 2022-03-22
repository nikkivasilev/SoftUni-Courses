list_of_phones = input().split(", ")

command = input()
while command != "End":
    command_list = command.split(" - ")
    current_command = command_list[0]
    phone = command_list[1]
    if current_command == "Add":
        if phone not in list_of_phones:
            list_of_phones.append(phone)
    elif current_command == "Remove":
        if phone in list_of_phones:
            list_of_phones.remove(phone)
    elif current_command == "Bonus phone":
        phones = phone.split(":")
        old_phone = phones[0]
        new_phone = phones[1]
        if old_phone in list_of_phones:
            list_of_phones.insert(list_of_phones.index(old_phone) + 1, new_phone)
    elif current_command == "Last":
        if phone in list_of_phones:
            list_of_phones.remove(phone)
            list_of_phones.append(phone)
    command = input()
print(", ".join(list_of_phones))
