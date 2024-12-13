def validate(pin):
    if len(pin) == 4 and pin.isdigit():
        return True
    else:
        return False
def bank_operations():
    balance = 0
    while True:
        print("\nChoose your option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Enquiry")
        print("4. Exit")

        option = input("Enter option (1/2/3/4): ")

        if option == '1':
            deposit_amount = float(input("Enter deposit amount: "))
            balance += deposit_amount
            print(f"Deposited {deposit_amount}. New balance: {balance}")

        elif option == '2':
            withdraw_amount = float(input("Enter withdrawal amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance.")
            else:
                balance -= withdraw_amount
                print(f"Withdrew {withdraw_amount}. New balance: {balance}")

        elif option == '3':
            print(f"Your current balance is: {balance}")

        elif option == '4':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid option.")
def main():
    pin = input("Enter your PIN: ")
    if validate(pin):
        print("Pin validated successfully.")
        bank_operations()
    else:
        print("Invalid PIN.")
main()
