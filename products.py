kitchen_product = { "masoor" : 30  , "soyabean" : 40 , "chanadal" : 80 , "khobra" : 56  }
print(kitchen_product)
amount = 0 + 20
while True:
    b = input("ENTER WHAT PRODUCT U WANT ").lower()

    if b in kitchen_product:
            print(f"the kitechen product PRICE IS ${kitchen_product[b]} ")
            amount = amount + kitchen_product[b]
    else:
            print("Sorry that is not in our store still now !!")
            a = input("! Want anything less (Y/N) --> ").upper()

            if a != "Y":
                print(f"Total Bill is ${amount }")
                print("Thanks For shopping 😊")
                break
