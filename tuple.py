cities = ("Delhi", "Pune", "Kolkata", "Jaipur", "Goa")
print("Cities:", cities)

def first_last(city):
    return city[0], city[-1]

a, b = first_last(cities)
print("First City:", a)
print("Last City:", b)

students = (("John", 85), ("Alice", 92), ("Bob", 78), ("David", 88))
print("Students:", students)

sorted_students = tuple(sorted(students))
print("Sorted Students:", sorted_students)

def show_fruits(items):
    x, y, z = items
    print("Fruit 1:", x)
    print("Fruit 2:", y)
    print("Fruit 3:", z)

fruits = ("Mango", "Orange", "Grapes")
show_fruits(fruits)