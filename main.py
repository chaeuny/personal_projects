import random

#cosntant value
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2, 
    "B": 4, 
    "C": 6, 
    "D": 8
}

#the more rare the symbol, the higher the value
symbol_value = {
    "A": 5, 
    "B": 4, 
    "C": 3, 
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else: 
                winnings += values[symbol] * bet
                winnings_lines.append(line + 1)
        
    return winnings, winnings_lines


#we need to randomize the symbols in each row and add it to the list
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #the nested list represents the values in the column
    columns = []
    for _ in range(cols): #generate a col for every col we have
        column = []
        current_symbols = all_symbols[:] #copy of the current symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value) #add the value to the column

        columns.append(column)

    return columns

def print_slot_machine(columns):
    #we need to change the column into a row: 'transposing'
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print() #brings a new line down 

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

def spin(balance):
    lines = get_number_of_lines()
    while True: 
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet >= balance:
            print(f"You do not have enough to bet that amount, your current balance is: R{balance}.")
        else:
            break


    print(f"You are betting R{bet} on {lines} lines. Total bet is equal to: R{total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won R{winnings}.")
    print(f"You won on lines:", *winning_lines) #splat opperator: pass every single line from the winning_lines list 
    return winnings - total_bet


#rerunning the main function (if they want to play again)
def main():
    balance = deposit()
    while True:
        print(f"Current balance is R{balance}")
        answer = input("Press enter to play. (q to quit)")
        if answer == "q":
            break
        else:
            balance == spin(balance)

    print(f"You are left with R{balance}")


main()