correct_password = "s3cr3t!P@ssw0rd"
guess = str(input())

if guess == correct_password:
    print("Welcome")
else:
    print("Wrong password!")