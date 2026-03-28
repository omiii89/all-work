print("Welcome ! To Our Genral Store ")
amount = 0 + 200

print("===LIST===")
print("1.Kitchen Products")
print("2.Dairy Products")
print("3.Snacks")
print("4.Total Amount")
print("5.Exits")

select = input("Enter Your Choice --> ")
if select =="1" :
    kitchen_product = { "masoor" : 30  , "soyabean" : 40 , "chanadal" : 80 , "khobra" : 56  }
    print(kitchen_product)
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
elif select == "2" :
    dairy_product = "HEllo"
              
else:
            print("Thank You ") 
                   