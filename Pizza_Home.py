IDandPasswordsds = []
stocks = [["Margherita Pizza", 10, 99], ["Farmhouse Pizza", 10, 199], ["Veg Extravaganza Pizza", 10, 399],
          ["Tomato Pasta Pizza", 10, 499], ["Combo(Margherita,Farmhouse)", 10, 521],
          ["Soft Drink(200 ml Coke)", 100, 25]]
AdminID = "Admin"
Adminpassword = "Adpass"
CustomerID = "Cus"
Customerpassword = "Cuspass"
while True:
    print("\n\t\t\t\t\t\t\t\t     WELCOME TO PIZZA HOME")
    print("\n\t\t\t\t\t\t\t\t\tPress 1 sign up \n\n\t\t\t\t\t\t\t\t\tPress 2 to login ")
    a = int(input("\n\nEnter your Valid option  :- "))
    if a == 1:
        a = input("\n\nEnter your name :- ")
        ab = input("\n\t\tEnter your ID :- ")
        abc = input("\n\t\t\tEnter your password :- ")
        IDandPasswordsds.insert(0, ([ab, abc, a]))
        while (True):
            print("\n\nIf you want to login press 1\n\nPress 2 to forget password\n\n press 0 to go back ")
            a = int(input("\n\t\tEnter your valid option"))
            if a == 1:
                loginId = (input("\n\nPlease enter your id"))
                if loginId == IDandPasswordsds[0][0]:
                    logincustomer = input("\n\n\t\tEnter your password")
                    if logincustomer == IDandPasswordsds[0][1]:
                        print("\n\n\t\t\t\t\t\t\tWelcome to Pizza Home")
                        print("\n\n\t\t\t\t\t\t\t\t\tHello Customer\n")
                        while (True):
                            print("\n\n\t\t\t\t Type 1 to see Menu"
                                  "\t\t\t\t Type 2 to keep your order"
                                  "\t\t\t\t Type 0 to logout of the account")
                            cus = int(input("\nPlease Type :- "))
                            if cus == 1:
                                print("\n\t\t\t\tWELCOME TO PIZZA HOME MENU\n\n")
                                print("\t\t\t\t""No.\t\t\t\tPrize\t\t\t\tMenu Name\n")
                                for i in range(0, len(stocks)):
                                    print("\t\t\t\t", i, "\t\t\t\t", stocks[i][2], "\t\t\t\t", stocks[i][0])
                            elif cus == 2:
                                print("\t\t\t\t\tWelcome to Pizza Home order\n\nplease enter your order")
                                price = 0
                                t = 0
                                temp = stocks
                                print("\n\t\t\t\tList serial no. and Quantity one by one ")
                                while t == 0:
                                    a = int(input("\nEnter serial no. of product  :-"))
                                    b = int(input("\tEnter Quantity of product :-"))
                                    if (a <= len(stocks)):
                                        if (stocks[a][1] > b):
                                            stocks[a][1] = stocks[a][1] - b
                                            price = price + b * stocks[a][2]
                                        else:
                                            print("\n\n", stocks[a][0], "is out of Stock . Order Quantity can be",
                                                  stocks[a][1],
                                                  "or less")
                                            break
                                    else:
                                        print("\n\nNo such Item exists ,try again")
                                    t = int(input("\t\t\t\tEnter 0 to add more or 1 to finalize --->"))
                                    print(price)

                                address = input("\n\nPlease enter your Address :-")
                                print("\n\t\tYour bill details")
                                print("\n\t\tOrder Confirmed\n\t\tPrice=", price,
                                      "\n\t\tOrder will be delivered in 30 min at your address", address)
                                print("\n\t\t\t\tThank you for shoping")
                            elif cus == 0:
                                print("You logged out succesfully")
                                break
                    else:
                        print("Invalid password")

                elif loginId != IDandPasswordsds[0][0]:
                    print("Please enter valid ID")
            if a == 2:
                a = input("\nPlease enter your name :- ")
                if a == IDandPasswordsds[0][2]:
                    print("\n\nYour Id is ", IDandPasswordsds[0][0], "\n\nYour password is ", IDandPasswordsds[0][1])
            print("\n\n\t\t\t\t\t\t\t\t\tHello Customer\n")

            if a == 0:
                print("\n\nYou are sucessfully logout")
                break

    elif a == 2:
        print(" \t\t\t\t\tWelcome to pizza Home")
        while (True):
            print("\n\n\t\t\t\tpress 1 If you are admin please\n"
                  "\t\t\t\tpress 2 If you are Customer please\n"
                  "\t\t\t\tpress 3 If you want to quit the app")
            entrychoice = int(input("\nEnter your choice :- "))
            if entrychoice == 1:
                print("\n\t\t\t\t\t\t\t\t\t\t\t\tHello Admin")
                ID = input("\nEnter your id :-").capitalize()
                if ID == AdminID:
                    password = input("\n\t\t\t\tEnter your Passwords :-").capitalize()
                    if password == Adminpassword:
                        print("\n\n\t\t\t\t\t\t\t\t\t\t\tWelcome Admin")
                    while (True):
                        print("\n\n\t\tType 1 to see stocks"
                              "\t\t\t Type 2 to manage the stocks"
                              "\t\t\t Type 3 to manage price"
                              "\t\t\t Type 4 to add items"
                              "\t\t\t Type 0 to logout of the account")
                        View = int(input("\n\nplease type :- "))
                        if View == 1:
                            print("\n\n\t\t\t\tNo.\t\t\t\t\tQuantity\t\t\t\t\tMenu Name\n")
                            for i in range(0, len(stocks)):
                                print("\t\t\t\t", i, "\t\t\t\t\t", stocks[i][1], "\t\t\t\t\t", stocks[i][0])
                        elif View == 2:
                            ab = int(input("\n\nEnter sr no. of item whose stock to change :- "))

                            if (ab < len(stocks)):
                                bc = int(input("Enter the quantity to add :- "))
                                print("\n")
                                stocks[ab][1] += bc
                                print("\n""Stock of ", stocks[ab][0], " updated to ", stocks[ab][1])
                            else:
                                print("\nNo such item found \n")

                        elif View == 3:
                            ab = int(input("\n\nEnter sr no. of item whose stock to change :- "))

                            if (ab < len(stocks)):
                                bc = int(input("Enter the New Price to add :- "))
                                print("\n")
                                stocks[ab][2] = bc
                                print("\n""Stock of ", stocks[ab][0], " updated to ", stocks[ab][2])
                        elif View == 4:
                            ab = input("Enter the Item name")
                            abc = int(input("\tEnter the Item Quantity"))
                            abcd = int(input("\tEnter the Item prize"))
                            stocks.append([ab, abc, abcd])
                        elif View == 0:
                            print("\t\t\t\tYou are succefully logged out")
                            break
                        else:
                            print("\t\t\t\tWrong choice")
                    else:
                        print("\t\t\t\tInvalid passwords")
                elif ID != AdminID:
                    print("\t\t\t\tInvalid ID")

            elif entrychoice == 2:
                print("\n\n\t\t\t\t\t\t\t\t\tHello Customer\n")
                ID = input("Enter your id :-").capitalize()
                if ID == CustomerID:
                    password = input("\n\t\t\tEnter you Passwords :-").capitalize()
                    if password == Customerpassword:
                        while (True):
                            print("\n\n\t\t\t\t Type 1 to see Menu"
                                  "\t\t\t\t Type 2 to keep your order"
                                  "\t\t\t\t Type 0 to logout of the account")
                            cus = int(input("\nPlease Type :- "))
                            if cus == 1:
                                print("\n\t\t\t\tWELCOME TO PIZZA HOME MENU\n\n")
                                print("\t\t\t\t""No.\t\t\t\tPrize\t\t\t\tMenu Name\n")
                                for i in range(0, len(stocks)):
                                    print("\t\t\t\t", i, "\t\t\t\t", stocks[i][2], "\t\t\t\t", stocks[i][0])
                            elif cus == 2:
                                print("\t\t\t\t\tWelcome to Pizza Home order\n\nplease enter your order")
                                price = 0
                                t = 0
                                temp = stocks
                                print("\n\t\t\t\tList serial no. and Quantity one by one ")
                                while t == 0:
                                    a = int(input("\nEnter serial no. of product  :-"))
                                    b = int(input("\tEnter Quantity of product :-"))
                                    if (a <= len(stocks)):
                                        if (stocks[a][1] > b):
                                            stocks[a][1] = stocks[a][1] - b
                                            price = price + b * stocks[a][2]
                                        else:
                                            print("\n\n", stocks[a][0], "is out of Stock . Order Quantity can be",
                                                  stocks[a][1],
                                                  "or less")
                                            break
                                    else:
                                        print("\n\nNo such Item exists ,try again")
                                    t = int(input("\t\t\t\tEnter 0 to add more or 1 to finalize --->"))
                                    print(price)

                                address = input("\n\nPlease enter your Address :-")
                                print("\n\t\tYour bill details")
                                print("\n\t\tOrder Confirmed\n\t\tPrice=", price,
                                      "\n\t\tOrder will be delivered in 30 min at your address", address)
                                print("\n\t\t\t\tThank you for shoping")
                            elif cus == 0:
                                print("You logged out succesfully")
                                break
                    else:
                        print("\t\t\t\tInvalid Password")
                elif ID != CustomerID:
                    print("\t\t\t\tInvalid ID")
            elif entrychoice == 3:
                print("\n\t\t\t\tThank you for using our app")
                break
            else:
                print("Please choose a correct option")