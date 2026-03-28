"""
while True:
   print("1.Create a Account")
   print("2.withdraw or Deposite")
   print("3.Check Balance")
   print("4.Exit")
   a=input("Hello what have to do --> ")
   print(a)
   if(a=="1"):
    b=(input("Enetr your name in Capital only \n"))
    print(b)
    c=(input("Enter What is Youe Age \n"))
    print(c)
   elif(a=="4"):
    print("Thankyou For Your Respond 😊")
    break 
   else:
    print("Please Recheck 😊")
    
"""

balance = 0
name = ""
age = ""
pin = 0

while True:
    print("\n===== BANK MENU =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice --> ")

    if choice == "1":
        name = input("Enter your name (CAPITAL letters): ")
        age = input("Enter your age: ")
        pin = 0
        balance = 0
        print("\nAccount created successfully 😊")

    elif choice == "2":
        if name == "":
            print("Please create an account first!")
        else:
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                balance = balance + amount
                print("Deposited successfully!")
            else:
                print("Invalid amount")

    elif choice == "3":
        if name == "":
            print("Please create an account first!")
        else:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Invalid amount")
            else:
                balance = balance - amount
                print("Withdrawal successful!")

    elif choice == "4":
        if name == "":
            print("Please create an account first!")
        else:
            print("\n===== ACCOUNT DETAILS =====")
            print("Name:", name)
            print("Age:", age)
            print("Balance:", balance)

    elif choice == "5":
        print("Thank you for using the bank 😊")
        break

    else:
        print("Please choose a valid option!")
