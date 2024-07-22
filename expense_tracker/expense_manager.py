expenses = {}


def add_expense():
    expense_id = max(expenses.keys(), default=0) + 1
    date = input("Enter Date (DD-MM-YYYY) :")
    category = input("Enter Category :")
    amount = float(input("Enter Amount :"))
    description = input("Enter Description :")    
    expenses[expense_id] = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("\nNo expenses available.\n")
    else:
        print("\n{:<5} {:<12} {:<10} {:<8} {:<20}".format("ID", "Date", "Category", "Amount", "Description"))
        print("-" * 60)
        for expense_id, details in expenses.items():
            print("{:<5} {:<12} {:<10} {:<8} {:<20}".format(
                expense_id, details['date'], details['category'], details['amount'], details['description']))
        print("")


def update_expense():
    expense_id=int(input("Enter Expense ID to update :"))
    if expense_id in expenses:
        date=input(f"Enter new Date (leave blank to keep '{expenses[expense_id]['date']}') :") or expenses[expense_id]['date']
        category=input(f"Enter new Category (leave blank to keep '{expenses[expense_id]['category']}') :") or expenses[expense_id]['category']
        amount=input(f"Enter new Amount (leave blank to keep '{expenses[expense_id]['amount']}') :")
        amount=float(amount) if amount else expenses[expense_id]['amount']
        description=input(f"Enter new Description (leave blank to keep '{expenses[expense_id]['description']}') :") or expenses[expense_id]['description']
       
        expenses[expense_id] = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        print("Expense updated successfully!\n")
    else:
        print("Expense not found!\n")


def delete_expense():
    expense_id=int(input("Enter Expense ID to delete :"))
    if expense_id in expenses:
        del expenses[expense_id]
        print("Expense deleted successfully!\n")
    else:
        print("Expense not found!\n")
