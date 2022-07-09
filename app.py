def Identitymgmt():
    print("****Active Directory Management - Ashwin Group of Business****")
    identity = input("Enter your Identity (a) Admin (b)Employee ")
    if identity == "a":
        admin()
    elif(identity == "b"):
        employee()
    else:
        print("Please enter the valid parameter")


database = {"Ashdesk": ["E02", "E03"], "AshMail": ["E01", "E02", "E03", "E04", "E05"],
            "AshExpense": ["E05"]}


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
        #  for s,e in database.items():
        #      if add_empID in e:
        #         print("The Employee id",add_empID,"already in the database...")
        #      else:
        #          pass()

        softwareAccess = input(
            "Enter which software he/she has access (a)AshMail (b)Ashdesk (c)AshExpense")
        for software,eid in database:
            if software == softwareAccess:
                for i in eid:
                    if eid==add_empID:
                        print("Id already having access to this software")
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
