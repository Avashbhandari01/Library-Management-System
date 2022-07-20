# Function for the main home display menu.
def homepage():
    # Code to display the welcome message.
    print("     **-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**   ")
    print("        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=    ")
    print("        =                 WELCOME                   =    ")
    print("        =                   TO                      =    ")
    print("        =                 UNIVERSAL                 =    ")
    print("        =                 DIGITAL                   =    ")
    print("        =                 LIBRARY                   =    ")
    print("        =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=    ")
    print("    **-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**-**      ")
    print()
    # Code to display the option table
    while True:
        print("|------------------------------------------------------|")
        print("|        Select an option from the table.              |")
        print("|------------------------------------------------------|")
        print("| Enter 1. To Display the list of books                |")
        print("| Enter 2. To Borrow a book                            |")
        print("| Enter 3. To return a book                            |")
        print("| Enter 4. To exit                                     |")
        print("|------------------------------------------------------|")
        try:
            userinput = int(input("Select a choice from 1 to 4: "))
            print()
            if userinput == 1:
                split()
                print("BookName\t\tAuthorName\t\tQuantity\t\tPrice")
                for i in range(10):
                    print(bookname[i]+"\t\t"+authorname[i]+"\t\t   "+quantity[i]+"\t\t\t"+"$"+cost[i])
            elif userinput == 2:
                split()
                borrowbooks()
            elif userinput == 3:
                split()
                returnBook()
            elif userinput == 4:
                print("Thank you for using Universal Digital Library.")
                break
            else:
                print("Please enter a valid choice from 1 to 4")
        except ValueError:
            print("Please input as suggested.")


# Function to record the current date.
def dates():
    import datetime
    now = datetime.datetime.now
    return str(now().date())


# Function to record the current time.
def times():
    import datetime
    now = datetime.datetime.now
    return str(now().time())


# Function to split the list of books.
def split():
    global bookname
    global authorname
    global quantity
    global cost
    bookname = []
    authorname = []
    quantity = []
    cost = []
    with open("List of Books.txt", "r") as f:

        lines = f.readlines()
        lines = [x.strip('\n') for x in lines]
        for i in range(len(lines)):
            index = 0
            for a in lines[i].split(','):
                if index == 0:
                    bookname.append(a)
                elif index == 1:
                    authorname.append(a)
                elif index == 2:
                    quantity.append(a)
                elif index == 3:
                    cost.append(a.strip("$"))
                index += 1


# Function to borrow the books from the library.
def borrowbooks():
    success = False
    # Code to get the name of the borrower.
    while True:
        firstName = input("Enter the first name of the borrower: ")
        if firstName.isalpha():
            break
        print("please input alphabet from A-Z")
    while True:
        lastName = input("Enter the last name of the borrower: ")
        if lastName.isalpha():
            break
        print("please input alphabet from A-Z")
    # Code to create a text file when the book is borrowed and record the borrowers details.
    t = "Borrow-" + firstName + ".txt"
    with open(t, "w+") as f:
        f.write("               Universal Digital Library  \n")
        f.write("               Borrowed By: " + firstName + " " + lastName + "\n")
        f.write("       Date: " + dates() + "       Time:" + times() + "\n\n")
        f.write("S.N. \t\tBookname \t      Authorname\t\t  Cost \n")
    repeat = False
    count = 1
    total = 0.0
    while success == False:
        print("Please select a option below:")
        for i in range(len(bookname)):
            print("Enter", i, "to borrow book", bookname[i])

        try:
            a = int(input())
            if a < 0:
                print("Please input according to the options above.")
            else:
                try:
                    if (int(quantity[a]) > 0):
                        print("Book is available")
                        with open(t, "a") as f:
                            f.write(
                                str(count) + " \t\t  " + bookname[a] + "\t\t  " + authorname[a] + "\t\t  " + "$" + cost[a] + "\n")
                                    
                            total += float(cost[a])

                        quantity[a] = str(int(quantity[a]) - 1)
                        with open("List of Books.txt", "w+") as f:
                            for i in range(10):
                                f.write(bookname[i] + "," + authorname[i] + "," + str(quantity[i]) + "," + "$" + cost[i] + "\n")
                                    

                        with open(t, "r") as f:
                            data = f.read()
                            print(data)
                        print("\t\t\t\t\t\t\t\t\t\t   Total:-" + "$" + str(total))

                        # Code to borrow multiple books from the library.
                        loop = True
                        while loop == True:
                            choice = str(input("Do you want to borrow more books? Press y for yes and n for no."))
                            if (choice.upper() == "N"):
                                with open(t, "a") as f:
                                    f.write("\t\t\t\t\t\t\t\t\t\t   Total: $" + str(total))
                                print("Thank you for borrowing books from us. ")
                                print("")
                                loop = False
                                success = True

                            elif (choice.upper() == "Y"):
                                count = count + 1
                                print("Please select an option below:")
                                for i in range(len(bookname)):
                                    print("Enter", i, "to borrow book", bookname[i])
                                a = int(input())

                                with open(t, "r") as f:
                                    booklines = f.read().split("\n")
                                    for i in range(5, 5+count-1):
                                        booklines2 = booklines[i].split("\t")
                                        if (booklines2[2].strip()) == bookname[a]:
                                            repeat = True
                                    if repeat == True:
                                        print("Cannot borrow same book twice.")
                                        break
                                    else:
                                        if (int(quantity[a]) > 0):
                                            print("Book is available")
                                            with open(t, "a") as f:
                                                f.write(
                                                    str(count) + ". \t\t  " + bookname[a] + "\t\t  " + authorname[a] + "\t\t  " + "$" + cost[a] + "\n")
                                                        
                                                total += float(cost[a])

                                            quantity[a] = str(int(quantity[a]) - 1)

                                            with open("List of Books.txt", "w+") as f:
                                                for i in range(10):
                                                    f.write(bookname[i] + "," + authorname[i] + "," + str(quantity[i]) + "," + "$" + cost[i] + "\n")
                                                        
                                                    success = False

                                            with open(t, "r") as f:
                                                data = f.read()
                                                print(data)
                                            print("\t\t\t\t\t\t\t\t\t\t   Total:-" + "$" + str(total))

                                        else:
                                            loop = False
                                            break
                            else:
                                print("Please choose as instructed")

                    else:
                        print("Book is not available")
                        success = False
                except IndexError:
                    print("")
                    print("Please choose book according to their number.")

        except ValueError:
            print("")
            print("Please choose as suggested.")


# Function to return the books borrowed from the library
def returnBook():
    name = input("Enter name of borrower: ")
    a = "Borrow-" + name + ".txt"
    try:
        with open(a, "r") as f:
            lines = f.readlines()
            lines = [a.strip("$") for a in lines]

        with open(a, "r") as f:
            data = f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b = "Return-" + name + ".txt"
    with open(b, "w+") as f:
        f.write("                Library Management System \n")
        f.write("                   Returned By: " + name + "\n")
        f.write("    Date: " + dates() + "    Time:" + times() + "\n\n")
        f.write("S.N.\t\tBookname\t\tAuthorname\t\tCost\n")

    total = 0.0
    for i in range(10):
        if bookname[i] in data:
            with open(b, "a") as f:
                f.write(str(i + 1) + "\t\t" + bookname[i] + "\t\t" + authorname[i] + "\t\t    $" + cost[i] + "\n")
                quantity[i] = str(int(quantity[i]) + 1)
            total += float(cost[i])

    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    choose = input()
    if (choose.upper() == "Y"):
        print("By how many days was the book returned late?")
        day = int(input())
        fine = 2 * day
        with open(b, "a") as f:
            f.write("\t\t\t\t\t\t\tFine: $" + str(fine) + "\n")
        total = total + fine

    print("Final Total: " + "$" + str(total))
    with open(b, "a") as f:
        f.write("\t\t\t\t\t\t\tTotal: $" + str(total))

    with open("List of Books.txt", "w+") as f:
        for i in range(10):
            f.write(
                bookname[i] + "," + authorname[i] + "," + str(quantity[i]) + "," + "$" + cost[i] + "\n")
                


homepage()



