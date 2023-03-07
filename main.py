
#gets the input from the user
def deposit():
    while True:
        amount = input("How much would you like to deposit? R")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break 
            else:
                print("Amount must be greater than R0.")
        else: 
            print("Please enter an amount.")

    return amount

deposit()