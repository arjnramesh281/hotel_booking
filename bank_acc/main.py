import random
import os

def save_account(account_details):
    file_name = f"weekly-tasks/bank_acc/{account_details['account_number']}.txt"
    with open(file_name, 'w') as file:
        for key, value in account_details.items():
            file.write(f"{key}: {value}\n")

def load_account(account_number):
    file_name = f"weekly-tasks/bank_acc/{account_number}.txt"
    if not os.path.exists(file_name):
        return None
    
    account_details = {}
    with open(file_name, 'r') as file:
        for line in file:
            key, value = line.strip().split(': ')
            account_details[key] = value
    
    return account_details

def update_balance(account_number, new_balance):
    account_details = load_account(account_number)
    if account_details:
        account_details['balance'] = str(new_balance)
        save_account(account_details)

acc = []

while True:
    print('\n1. Create account\n2. Login')
    ch = int(input('Enter your choice: '))

    if ch == 1:
        name = input('Enter your name: ')
        ph = int(input('Enter your phone number: '))
        password = int(input('Enter your pin: '))
        balance = int(input('Deposit: '))
        
        account_number = random.randint(10000, 99999)
        
        account_details = {
            'name': name,
            'phone': ph,
            'password': str(password),  
            'balance': str(balance),
            'account_number': str(account_number)
        }
        
        acc.append(account_details)
        
        save_account(account_details)
        
        print(f"Account has been created successfully! Your account number is: {account_number}")
    
    elif ch == 2:
        acc_num = input('Enter your account number: ')
        password = input('Enter your pin: ')
        
        account_details = load_account(acc_num)
        
        if account_details:
            if account_details['password'] == password:
                print(f"Login successful! Welcome, {account_details['name']}.")
                
                while True:
                    print('\n1. Deposit\n2. Withdraw\n3. Display Balance\n4. Logout')
                    option = int(input('Enter your choice: '))
                    
                    if option == 1:  
                        amount = int(input('Enter amount to deposit: '))
                        new_balance = int(account_details['balance']) + amount
                        update_balance(acc_num, new_balance)
                        account_details['balance'] = str(new_balance) 
                        print(f"Amount deposited successfully! New balance is: {new_balance}")
                    
                    elif option == 2:  
                        amount = int(input('Enter amount to withdraw: '))
                        current_balance = int(account_details['balance'])
                        if amount <= current_balance:
                            new_balance = current_balance - amount
                            update_balance(acc_num, new_balance)
                            account_details['balance'] = str(new_balance) 
                            print(f"Amount withdrawn successfully! New balance is: {new_balance}")
                        else:
                            print("Insufficient balance.")
                    
                    elif option == 3: 
                        print(f"Your current balance is: {account_details['balance']}")
                    
                    elif option == 4:  
                        print("Logging out...")
                        break                  
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Invalid pin. Please try again.")
        else:
            print("Account not found. Please check the account number and try again.")