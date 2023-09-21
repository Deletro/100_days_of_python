import random


class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 100000
        self.account_number = []
        self.account_number_generator()
        self.account_password = 1234
        self.password_code_wrong_try = 3

    def change_password(self, old_password, new_password):
        if self.account_password == old_password:
            self.account_password = new_password
            print("Your password has changed!")
        else:
            print("Wrong old password")

    def account_security(self):
        while True:
            password = int(input("Enter here your password: "))
            if password == self.account_password:
                self.show_account_properties()
                break
            elif self.password_code_wrong_try == 1:
                print("Wrong Password. Your Account is Locked")
                break
            else:
                self.password_code_wrong_try -= 1
                print(
                    f"Wrong Password. Remaining tryes: {self.password_code_wrong_try}"
                )

    def account_number_generator(self):
        for num in range(12):
            num = random.randint(1, 9)
            self.account_number.append(num)

    def show_account_properties(self):
        print("----------------------------------------------")
        print(f"Account Owner Name: {self.owner}")
        print(f"Your Balance: {self.balance}")
        print("Your Account number:")
        print("".join(str(num) for num in self.account_number))
        print("----------------------------------------------")

    def balance_inquiry(self):
        print("--------------------------------")
        print(f"Your Balance: {self.balance} $")
        print("--------------------------------")

    def deposit_money(self, the_amount_you_want_to_pay):
        self.balance += the_amount_you_want_to_pay
        print(f"Your balance is: {self.balance} $")

    def withdraw_money(self, the_amount_you_want_to_withdraw):
        if the_amount_you_want_to_withdraw > self.balance:
            return print("You dont have enough of money to withdraw that much")
        self.balance -= the_amount_you_want_to_withdraw
        print(f"Your balance is: {self.balance} $")


class Bank:
    def __init__(self):
        self.bankaccounts = []

    def open_new_bank_account(self, owner):
        self.bankaccounts.append(BankAccount(owner))

    def account_log_in(self):
        balance_owner = input("Type your name here: ")
        for owner in self.bankaccounts:
            if owner.owner == balance_owner:
                return owner, owner.account_security()
        print(f"We dont have an account with that name: '{balance_owner}'")

    def account_existance_checker(self, balance_owner_name):
        for owner in self.bankaccounts:
            if owner.owner == balance_owner_name:
                return owner
            continue

    def money_transfer(self, for_who, from_whom, amount_money):
        account1 = self.account_existance_checker(from_whom)
        # print(account1.balance)
        account1.balance -= amount_money
        # print(account1.balance)
        account2 = self.account_existance_checker(for_who)
        # print(account2.balance)
        account2.balance += amount_money
        # print(account2.balance)
