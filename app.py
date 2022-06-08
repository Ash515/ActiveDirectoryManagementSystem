def Identitymgmt():
    print("****Active Directory Management - Ashwin Group of Business****")
    identity = input("Enter your Identity (a) Admin (b)Employee ")
    if identity == "a":
        admin()
    elif(identity == "b"):
        employee()
    else:
        print("Please enter the valid parameter")


database = {"AshMail": ["E01", "E02", "E03", "E04", "E05"],
            "Ashdesk": ["E02", "E03"], "AshExpense": ["E05"]}


def admin():
    adminChoice = input(
        "Enter your Choice (a) View the Logs (b)Insert new record:")
    if adminChoice == "a":
        databaseCheck()
    elif adminChoice == "b":
        InsertRecord()


def InsertRecord():
    add_empID = input("Enter the employee ID:")
    if add_empID:
        # for s,e in database.items():
        #     if add_empID in e:
        #         print("The Employee id",add_empID,"already in the database...")


        softwareAccess = input("Enter which software he/she has access (a)AshMail (b)Ashdesk (c)AshExpense")
        for software in database:
            if software == softwareAccess:
                database[software].append(add_empID)
                print("Successfully Added the employee ID", add_empID, "!")
                admin()

            else:
                print("Sorry the entered software is not found...")
                admin()
    else:
        print("Please add a employee ID...")
        admin()


def databaseCheck():
    for softwares, empid in database.items():
        print(softwares, empid)
    admin()


def employee():
    pass


Identitymgmt()
