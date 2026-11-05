x = True
while x == True:
     x = bool(int(input("are you okay? true/false: ")))
     if x == True:
            print("continuing loop")
            continue
else:
        print("end of loop")