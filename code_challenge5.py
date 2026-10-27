n = int(input("size of range"))
for x in range (n):
    for y in range (n):
        if x == y or x + y == 4:
           print("*", end= "")
        else:
            print(" ", end= "")
    print()