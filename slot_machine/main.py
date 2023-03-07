#cosntant value
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 100

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

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break 
            else:
                print("Enter a valid numebr of lines.")
        else: 
            print("Please enter an number.")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet? R")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break 
            else:
                print(f"Amount must be between R{MIN_BET} - R{MAX_BET}.")
        else: 
            print("Please enter an amount.")

    return amount


#rerunning the main function (if they want to play again)
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet >= balance:
            print(f"You do not have enough to bet that amount, your current balance is: R{balance}.")
        else:
            break


    print(f"You are betting R{bet} on {lines} lines. Total bet is equal to: R{total_bet}")



main()