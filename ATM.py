import time

print("Please insert your CARD:")

time.sleep(5)

password = 12345

pin = int(input("Enter your ATM pin: "))

balance = 5000

if pin == password:
    while True:
        print("""
            1 == balance
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """)
        try:
            option = int(input("Please enter your choise: "))
        except:
            print("Please enter valid option: ")
        
        if option == 1:
            print(f"Your current balance is: {balance}")
            print("=======================================================")
            print("=======================================================")
        if option == 2:
            withdraw_amount = int(input("Please enter withdraw_amount:"))
            print("=======================================================")
            print("=======================================================")
            balance = balance - withdraw_amount
            print(f"{withdraw_amount} is debited from your account.")
            print("=======================================================")
            print("=======================================================")
            print(f"your updated balance is: {balance} ")
            print("=======================================================")
            print("=======================================================")
        if option == 3:
            deposit_amount = int(input("Please enter your deposit_amount:"))
            print("=======================================================")
            print("=======================================================")
            balance = balance + deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            print("=======================================================")
            print("=======================================================")

            print(f"Your updated balance is: {balance}")
            print("=======================================================")
            print("=======================================================")

        if option == 4:
            break

else:
    print("Wrong pin, Please try again! ")
