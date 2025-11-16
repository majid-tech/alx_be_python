# pattern_drawing...

size_of_pattern = int(input("Enter the size of the pattern: "))
i = 0

while i < size_of_pattern:
    j = 1
    for j in range(size_of_pattern):
        print("*", end="")
    print()
    i += 1 