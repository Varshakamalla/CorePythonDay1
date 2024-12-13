class Bank:
    acc_balance = 10000

    def deposit(self):
        deposit_amount = int(input("Enter the deposit amount: "))
        if deposit_amount >= 100 and deposit_amount % 100 == 0 and deposit_amount <= 50000:
            self.acc_balance += deposit_amount
            print(f'Amount Deposited successfully. The account balance is {self.acc_balance}')
        else:
            print("Enter correct amount of money (multiple of 100, between 100 and 50000).")

    def withdraw(self):
        withdraw_amount = int(input("Enter the withdraw amount: "))
        if 100 <= withdraw_amount <= 20000 and withdraw_amount % 100 == 0 and withdraw_amount <= self.acc_balance and self.acc_balance >= 500:
            self.acc_balance -= withdraw_amount
            print(f'The account balance is {self.acc_balance}')
            return True
        else:
            print("Invalid withdrawal amount or insufficient balance.")
            return False

    def balance_enquiry(self):
        print(f'Your current balance is {self.acc_balance}')

    def viewOptions(self):
        withdrawal_attempts = 0
        while True:
            print("\nSelect an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Balance Enquiry")
            print("0. Exit")
            option = int(input("Enter the option: "))

            if option == 1:
                self.deposit()
            elif option == 2:
                if withdrawal_attempts < 3:
                    if self.withdraw():
                        withdrawal_attempts += 1
                else:
                    print("Maximum withdrawal attempts reached.")
            elif option == 3:
                self.balance_enquiry()
            elif option == 0:
                print("Exiting... Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def validate(self):
        count = 0
        while count < 3:
            pin = int(input("Enter the pin: "))
            if pin == 1234:
                self.viewOptions()
                break
            else:
                count += 1
                print(f"Invalid PIN. Attempt {count}")
        else:
            print("Maximum attempts completed. Exiting.")

obj = Bank()
obj.validate()
