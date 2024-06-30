size = int(input("Enter the size of the pattern:"))

tmp = size
while tmp > 0:
    for i in range(size):
        print("*", end="")
    print("")
    tmp -= 1
