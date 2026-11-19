#JEEPNEY SIMULATOR
route = ("bayan, QUEZON.AVE,CAMPO")
passenger = ()
seats = 12
fare = 14
total = 0

while True:
    print()
    print("pasakay po!:", passenger )
    print(len(passenger), "of", seats, "seats")
    print("1 sakay 2 priority seat 3 para po!")
    print("4 baba sa pinto 5 sakay sa harap")
    print("6 seat check 7 balikan 8 exit")
    choice = input ("choice : ")

    if choice == "1":
        if len(passenger) ==  seats:
         print("the jeep is full!")
        else:
           name = input("name: ")
           passenger.append("carla")
           total = total + fare
           print(name, "nakasakay sa likod")

    elif choice == "2":
       if len(passenger) == seats:
         print("puno na!")
       else:
          name == input("name:")
          passenger.insert(0, "lucing")
          total == total + fare
          print("name, took the priority seats")

    elif choice == "3":
       name = input("sino ba-baba?")
       if name  in passenger:
          passenger.remove("martha")
          print("ingat sa pag uwi")
       else:
          print(name, "got off")

    elif choice == "4":
       if len(passenger) == 0:
        print("the jeep is empty")
       else:
        left = passenger.pop()
       print(left, "got off at the door") 

    elif choice == "5":
       if len (passenger) == 0:
          print("the jeep is empty")
       else:
          front = passenger.pop(0)
          print("front seat got off")
    elif choice == "6":
       for i in range (len(passenger)):
          print("seat", i+1, passenger[1])

    elif choice == "7":
       route.reverse()
       print("route", route)
    elif choice == "8":
       print("total fare today:2000",total)
       break
    else:
       print("invalid choice")