size = int(input("enter size"))
s = 1
for x in range (size):
    for y in range (x + 1):
        print(s, end= " ")
        s = s + 1
    print()
