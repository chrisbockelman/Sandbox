name = input("Enter your name: ")
while name == "":
    print("Invalid input")
    name = input("Enter your name: ")
for char in name:
    print(char)