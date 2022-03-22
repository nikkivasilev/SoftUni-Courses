class Person:
    species = 'mammal'

    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


ivan = Person("Ivan", "Ivanov", 33)
maria = Person("Maria", "Ivanova", 22)

print(ivan.first_name)
print(ivan.last_name)
print(ivan.age)
