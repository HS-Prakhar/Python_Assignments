database = {
        'eddygrant000':{
            'name': 'Sachin',
            'age': 22,
            'email': 'eddygrant000@gmail.com',
             'pin': 8888,
            'Acc_Balance': 50000
        },
        'sachin123':{
            'name': 'Tanuj',
            'age': 25,
            'email': 'tanuj@gmail.com',
            'pin': 1234,
            'Acc_Balance': 20000
        }
    }
user_pin = 0
def SignIn():
    user_name = input("Enter username: ")
    if user_name in database.keys():
        try: 
            user_pin = int(input("Enter pin: "))
            if user_pin == database[user_name]['pin']:
                print(f"Welcome {database[user_name]['name']}!")
                Accounts(user_name)
            else:
                print("Wrong Pin")
                choices()
        except Exception:
            print("Wrong Pin")
            choices()
    else:
        print("Username is Not Found")
        choices()
def SignUp():
    user_name = input("Create username: ")
    if user_name in database.keys():
        print("User already exist!")
        choices()
    else:
        try:
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            email = input("Enter your email: ")
            pin = int(input("Create your pin: "))
            Acc_Balance = int(input("Enter balance in your account: "))
            print("Username successfully created")
            d1 = {
            user_name:{
                'name': name,
                'age': age,
                'email': email,
                'pin': pin,
                'Acc_Balance': Acc_Balance
            }}
            database.update(d1)
        except Exception:
            print("Something went wrong...")
            choices()
def Accounts(user_name):
    choice2 = int(input("""Enter your choice:
1. Check Balance
2. Deposit
3. Withdrawl
4. Log out
->"""))
    if choice2 == 1:
        print(f"Current balance = INR {database[user_name]['Acc_Balance']}")
        Accounts(user_name)
    elif choice2 == 2:
        try:
            amount = int(input("Enter Amount: "))
            x = database[user_name]['Acc_Balance']
            x += amount
            database[user_name].update({'Acc_Balance': x})
            print(f"""Amount Deposited Successfully!
Current balance = INR {database[user_name]['Acc_Balance']}""")
            Accounts(user_name)
        except Exception:
            print("Please enter amount in digits")
            Accounts(user_name)
    elif choice2 == 3:
        amount = int(input("Enter Amount: "))
        x = database[user_name]['Acc_Balance']
        y = x - amount
        database[user_name].update({'Acc_Balance': y})
        print(f"Collect your cash: {amount}/-")
        print(f"Current balance = INR {database[user_name]['Acc_Balance']}")
        Accounts(user_name)
    elif choice2 == 4:
        print("You have logged out successfully!")
        choices()
    else:
        print("Invalid input")
def choices():
    try:
        choice = int(input("""Enter your choice: 
1. Sign in
2. Sign up
3. Exit
->"""))
        if choice == 1:
            SignIn()
        elif choice == 2:
            SignUp()
        elif choice == 3:
            exit()
        else:
            print("Invalid Input")
            choices()
    except ValueError as e:
        print("Enter integer value")
        choices()
    except Exception as e:
        print("Something went wrong...",e)
        choices()
choices()