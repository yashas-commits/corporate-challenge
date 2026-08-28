fruits = ["Apple", "Banana", "Orange", "Mango"]

print("Original list:", fruits)

print("First fruit:", fruits[0])

fruits.append("Grapes")
print("After adding Grapes:", fruits)

fruits.remove("Banana")
print("After removing Banana:", fruits)

print("Fruits in the list:")
for fruit in fruits:
    print(fruit)

print("Number of fruits:", len(fruits))