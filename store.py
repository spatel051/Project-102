print("Welcome to Veggie Store!")

class store:
    def __init__(self, card_num, name):
        self.card_num = card_num
        self.name = name
    
    def buy(self):
         print("Please choose what you would like to purchase:")
         print("1) Vegetables 2) Fruits 3) Other")

         activity = int(input("Enter activity number: "))
         if(activity == 1):
            print("Here is what we currently have in stock:")
            print("1) Tomatoes 2) Potatoes 3) Spinach")
            answer = (input("Please enter your choices here (with the amount): "))
            print("You have purchased " + answer)
            print("That will be $110.")
            amount = int(input("Pay: "))
            if amount < 110:
                print("Insufficient funds")
                amount = int(input("Please pay again: "))
                if amount < 110:
                    print("Insufficient funds")
                    amount = int(input("Please pay again: "))
                elif amount > 110:
                    new_amount = amount - 110
                    print("Thank you. Your change is $" + str(new_amount))
                else:
                    print("Thank you! You may expect your delivery within 2-3 days.")

            elif amount > 110:
                new_amount = amount - 110
                print( "Thank you. Your change is $" + str(new_amount))
            else:
                print("Thank you! You may expect your delivery within 2-3 days.")

         elif(activity == 2): 
            print("Here is what we currently have in stock:")
            print("1) Oranges 2) Apples 3) Bananas 4) Grapes")

            answer = (input("Please enter your choices here (with the amount): "))
            
            print("You have purchased " + answer)
            print("That will be $90.")
            amount = int(input("Pay: "))
            if amount < 90:
                print("Insufficient funds!")
                amount = int(input("Please pay again: "))

                if amount < 90:
                    print("Insufficient funds!")
                    amount = int(input("Please pay again: "))
                    
                elif amount > 90:
                    new_amount = amount - 90
                    print( "Thank you. Your change is $" + str(new_amount))
                else:
                    print("Thank you! You may expect your delivery within 2-3 days.")

            elif amount > 90:
                new_amount = amount - 90
                print( "Thank you. Your change is $" + str(new_amount))
            else:
                print("Thank you! You may expect your delivery within 2-3 days.")

         elif(activity == 3):
            answer = (input("Please enter your choices here (with the amount): "))
            print("You have purchased " + answer)
            print("That will be $246.")
            amount = int(input("Pay: "))
            if amount < 250:
                print("Insufficient funds!")
                amount = int(input("Please pay again: "))
                if amount < 250:
                    print("Insufficient funds!")
                    amount = int(input("Please pay again: "))
                    
                elif amount > 250:
                    new_amount = amount - 250
                    print("Thank you. Your change is $" + str(new_amount))
                else:
                    print("Thank you! You may expect your delivery within 2-3 days.")

            elif amount > 250:
                new_amount = amount - 250
                print( "Thank you. Your change is $" + str(new_amount))
            else:
                print("Thank you! You may expect your delivery within 2-3 days.")
    
def main():
    name = input("Enter name: ")
    card_number = input("Enter card number: ")
    print("Welcome " + name + "!")
    new_user = store(card_number, name)

    if card_number.strip().isdigit():
        new_user.buy()
        
    else:
        print("Please only enter numbers!")
        card_number = input("Insert card number: ")
        if card_number.strip().isdigit():
            new_user.buy()

    
if __name__=="__main__":
    main()