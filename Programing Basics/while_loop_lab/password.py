username = input()
password = input()
current_password = ''

while current_password != password:
    current_password = input()

print(f"Welcome {username}!")