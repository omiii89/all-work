# ---------- INITIAL DATA ----------
pin = ""
balance = 0
history = []

# ---------- ACCOUNT SETUP ----------
print("===== WELCOME TO MOBILE RECHARGE SYSTEM =====")
pin = input("Create a 4-digit PIN: ")
balance = int(input("Add initial balance: "))
print("Account created successfully ✅")

# ---------- MAIN SYSTEM ----------
while True:
    print("\n========== MENU ==========")
    print("1. Mobile Recharge")
    print("2. Mobile Data Recharge")
    print("3. Recharge History")
    print("4. Check Balance")
    print("5. Exit")
    print("==========================")

    choice = input("Select an option (1-5): ")

    # -------- MOBILE RECHARGE --------
    if choice == "1":
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            phone_number = input("Enter 10-digit mobile number: ")
            amount = int(input("Enter recharge amount: "))

            if amount <= balance and amount > 0:
                balance -= amount
                history.append(f"Mobile Recharge | {phone_number} | Rs.{amount}")
                print("Recharge successful ✅")
            else:
                print("Insufficient balance ❌")
        else:
            print("Wrong PIN ❌")

    # -------- DATA RECHARGE --------
    elif choice == "2":
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            phone_number = input("Enter 10-digit mobile number: ")
            amount = int(input("Enter data recharge amount: "))

            if amount <= balance and amount > 0:
                balance -= amount
                history.append(f"Data Recharge | {phone_number} | Rs.{amount}")
                print("Data recharge successful ✅")
            else:
                print("Insufficient balance ❌")
        else:
            print("Wrong PIN ❌")

    # -------- RECHARGE HISTORY --------
    elif choice == "3":
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            if len(history) == 0:
                print("No recharge history found.")
            else:
                print("\n----- Recharge History -----")
                for item in history:
                    print(item)
        else:
            print("Wrong PIN ❌")

    # -------- CHECK BALANCE --------
    elif choice == "4":
        entered_pin = input("Enter your PIN: ")

        if entered_pin == pin:
            print(f"Current Balance: Rs.{balance}")
        else:
            print("Wrong PIN ❌")

    # -------- EXIT --------
    elif choice == "5":
        print("Thank you for using Mobile Recharge System 😊")
        break

    else:
        print("Invalid option. Please try again ❌")
