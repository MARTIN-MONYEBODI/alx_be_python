positive_integer = int(input("Enter the size of the pattern: "))
i = 1
print("Here is your pattern:")
while i <= positive_integer:
    for j in range(1, positive_integer + 1):
        print("*", end="")
    print()
    i += 1