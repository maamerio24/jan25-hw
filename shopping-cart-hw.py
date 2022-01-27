# # 1) Build a Shopping Cart
# #     Should have the following capabilities:

# #     1) Takes in input
# #     2) Stores user input into a list
# #     3) User can add or delete items
# #     4) User can see current shopping list
# #     5) Loops until user 'quits'
# #     6) Upon quiting the program, print out all items in the user's list

cart =[]

def shopping_cart():
    while True:
        items = input("What item will you be shopping for today? ")
        cart.append(items)
        print("Your current shopping cart is: ")
        for item in cart:
            print("-  " + item)

        done = False
        while not done:
            adjust = input("Would you like to add or delete items?(a/d/no) ").lower()
            if adjust == "a":
                done = True
            elif adjust == "d":
                remove = input("Which item would you like remove? ")
                cart.remove(remove)
                print("Your current shopping cart is: ")
                for item in cart:
                    print("-  " + item)
            elif adjust == "no":
                print("Your final shopping cart is :")
                for item in cart:
                    print("-  " + item)
                return
            else:
                input("That was an invalid command. Press any key to continue. ")

shopping_cart()





        





