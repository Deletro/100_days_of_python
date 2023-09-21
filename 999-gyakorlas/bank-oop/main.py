from bank import Bank


bank = Bank()
bank.open_new_bank_account("Akos")
bank.open_new_bank_account("Balazs")

while True:
    print("Welcome to the OPT Bank")
    print("Choose an option:")
    choice = input("'G' - log in\n'R' - Exit\n : ").lower()
    if choice == "r":
        print("Have a nice day!")
        break
    elif choice == "g":
        user, security = bank.account_log_in()
        if not user:
            continue
        account_status = True
        while account_status:
            user_choice = input(
                "Select:\nModify your password - 'M'\nDeposit money - 'D'\nWithdraw money - 'W'\nTransfer money - 'T'\nBalance inquiry - 'I'\nExit - 'R'\n : "
            ).lower()
            if user_choice == "r":
                print("We are transfering you to the log-in menu.")
                break
            elif user_choice == "m":
                print(user.account_password)
                old_password = int(input("Old password: "))
                new_password = int(input("New password: "))
                new_again = int(input("New password again: "))
                if new_password == new_again:
                    user.change_password(old_password, new_password)
                else:
                    print("The two 'new password' are not the same.")
            elif user_choice == "d":
                money_you_want_to_deposit = int(
                    input("The amount you want to deposit: ")
                )
                user.deposit_money(money_you_want_to_deposit)
            elif user_choice == "w":
                money_you_want_to_withdraw = int(
                    input("The amount you want to withdraw: ")
                )
                user.withdraw_money(money_you_want_to_withdraw)
            elif user_choice == "t":
                for_who = input("For who?: ")
                from_whom = user.owner
                amount_money = int(input("How much $ ?: "))
                bank.money_transfer(
                    for_who=for_who, from_whom=from_whom, amount_money=amount_money
                )
            elif user_choice == "i":
                user.balance_inquiry()
            else:
                print(f"There is no '{user_choice}' option.")
    else:
        print(f"There is no '{choice}' option.")
