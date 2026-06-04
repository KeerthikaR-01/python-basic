# membership operators

fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("Yes, 'banana' is in the fruits list")

if "grape" not in fruits:
    print("No, 'grape' is not in the fruits list")

# identity operators

x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]

x = y # x and y now refer to the same list object in memory

if x is y:
    print("x and y are the same object")

if x is not y:
    print("x and y are different objects")