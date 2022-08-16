"""
    Title: Bank Account Manager ATM
    Author: Arash Kamyabi

"""

class Account:
    def __init__(self, cust_id):
        self.cust_id = cust_id


class CheckingAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        Account.__init__(self, cust_id)
        self.amount = float("%.2f" % deposit_amount)

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):

        if self.amount > withdraw_amount:
            self.amount -= withdraw_amount

        else:
            print("Error! Insufficient Funds.")


    def display_amount(self):
        print ("Your account balance is: $",self.amount)

    def get_amount(self):
        return self.amount


class SavingsAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        Account.__init__(self, cust_id)
        self.amount = float("%.2f" % deposit_amount)

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):

        if self.amount > withdraw_amount:
            self.amount -= withdraw_amount

        else:
            print("Error! Insufficient Funds.")

    def display_amount(self):
        print ("Your account balance is: $",self.amount)

    def get_amount(self):
        return self.amount


class BusinessAccount(Account):
    def __init__(self, cust_id, deposit_amount):
        Account.__init__(self, cust_id)
        self.amount = float("%.2f" % deposit_amount)

    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):

        if self.amount > withdraw_amount:
            self.amount -= withdraw_amount

        else:
            print("Error! Insufficient Funds.")

    def display_amount(self):
        print ("Your account balance is: $",self.amount)

    def get_amount(self):
        return self.amount


def get_id():
    while 1:
        cust_id = input('Please enter your customer ID number:')
        if cust_id.isdigit():
            return int(cust_id)
        else:
            print("Cannot find your record.")
            print("Please get your card.")
            print("Exiting this session...")

def get_account():
    while 1:
        print("Enter 1 for checking account")
        print("Enter 2 for savings account")
        print("Enter 3 for business account")
        account_id = input('Enter which account to use:')
        if account_id.isdigit() and int(account_id)  in [1,2,3]:
            return int(account_id)
        else:
            print("Invalid response...Please try again")

def get_action():
    while 1:
        print("\nHow may I help you?")
        print("Press 1 for balance view.")
        print("Press 2 for withdrawals.")
        print("Press 3 for deposits.")
        print("Press 4 to exit.")

        action_val = input("Please enter your choice: ")
        if action_val.isdigit() and int(action_val)  in [1,2,3,4]:
            return int(action_val)
        else:
            print("Invalid response...Please try again")

def get_withdrawal():
    while 1:

        withdrawal_amount = input("Enter the amount to withdrawal: ")
        try:
            val= float(withdrawal_amount)
            if val < 0 :
                print("Error. Cannot withdraw negative amount, try again.")
                continue
            return float('%0.2f'%val)
        except ValueError:
            print('Error. Non-numerical input, try again.')

def get_deposit():
    while 1:

        deposit_amount = input("Enter the amount to deposit: ")
        try:
            val= float(deposit_amount)
            if val < 0 :
                print("Error. Cannot deposit negative amount, try again.")
                continue
            return float('%0.2f'%val)
        except ValueError:
            print('Error. Non-numerical input, try again.')

if __name__ == '__main__':
    isSessionOn = True
    isCustomer = False

    def initialise_objects():
        global Arash_checking, Arash_business ,Jane_business, John_savings, database


        Arash_checking = CheckingAccount(1, 10200.24)
        Arash_business = BusinessAccount(1,1000000)
        Jane_savings = SavingsAccount(2, 19230.31)
        John_business = BusinessAccount(3, 51500.40)

        # Checking ID -> 1
        # Savings ID -> 2
        # Business ID -> 3

        database = [[Arash_checking, 1, 1], [Arash_business, 1, 3], [Jane_savings, 2, 2], [John_business, 3, 3]]

        return None

    initialise_objects()

    while isSessionOn is True:
        print ("Welcome to AK National Bank.")

        # Card reading the customer info representation
        customerID = get_id()
        print ("\n")

        cust_accounts = []
        for i in database:
            if i[1] == customerID:
                cust_accounts.append(i[2])
                isCustomer = True
        if isCustomer is True:
            isAccountSelected = False

            while isAccountSelected is False:

                account_type = get_account()

                if account_type in cust_accounts:
                    for x in database:
                        if account_type == x[2] and customerID==x[1]:
                            objectName = x[0]

                    isAccountSelected = True
                    isAccountSessionOn = True

                    while isAccountSessionOn is True:

                        action_value = get_action()

                        if action_value == 1:
                            objectName.display_amount()
                            print ("\n")

                        if action_value == 2:
                            amnt_to_withdraw = get_withdrawal()

                            objectName.withdraw(amnt_to_withdraw)
                            print ("current balance is: $", objectName.get_amount())
                            print ("\n")

                        if action_value == 3:
                            amnt_to_deposit = get_deposit()

                            objectName.deposit(amnt_to_deposit)
                            print ("current balance is: $", objectName.get_amount())
                            print ("\n")

                        if action_value == 4:
                            isAccountSessionOn = False
                            print ("Thank for using the 24-hour ATM service.")
                            print ("Have a pleasant day.")
                            print ("\n\n")
                            print ("##########################################")
                else:
                    print ("Error. You don't have that account.")
                    print ("Please try again.\n")

        else:
            print ("Cannot find your record.")
            print ("Please get your card.")
            print ("Exiting this session...")
