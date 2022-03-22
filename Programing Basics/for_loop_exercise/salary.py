total_open_sites = int(input())
salary = int(input())

for sites in range(total_open_sites):
    name_of_cite = input()
    if name_of_cite == "Facebook":
        salary -= 150
    elif name_of_cite == "Instagram":
        salary -= 100
    elif name_of_cite == "Reddit":
        salary -= 50
    if salary == 0:
        break
if salary == 0:
    print(f"You have lost your salary.")

else:
    print(salary)