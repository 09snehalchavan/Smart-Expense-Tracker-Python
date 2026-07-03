from income import create_income_table, add_income_data
from expense import create_expense_table, add_expense_data
from transaction import view_all_transactions, search_transactions
from report import all_report
from analysis import category_analysis
from budget import budget_mnmg
from export import export_report
# create_income_table()

def add_income(user):
    amount = int(input("Enter the amount: "))
    source = input("Enter the source of income: ")
    print("Payment Modes \n\t1. Cash \t2. Card \t3. Online")
    payment_mode = input("Enter the choice in 1, 2, 3 : ")  

    if payment_mode == '1':
        payment_mode = 'Cash'
    elif payment_mode == '2':
        payment_mode = 'Card'
    elif payment_mode == '3':
        payment_mode = 'Online'
    else:
        print("Invalid choice. Please select a valid payment mode.")
        return

    income_date = input("Enter the date of income (YYYY-MM-DD): ")  

    add_income_data(user[2], amount, source, payment_mode, income_date)
    print("Income data added successfully..!!!")



def add_expense(user):
    amount = int(input("Enter the amount: "))
    category = input("Enter the category of expense: ")
    print("Payment Modes \n\t1. Cash \t2. Card \t3. Online")
    payment_mode = input("Enter the choice in 1, 2, 3 : ")  

    if payment_mode == '1':
        payment_mode = 'Cash'
    elif payment_mode == '2':
        payment_mode = 'Card'
    elif payment_mode == '3':
        payment_mode = 'Online'
    else:
        print("Invalid choice. Please select a valid payment mode.")
        return

    # expense_date = input("Enter the date of expense (YYYY-MM-DD): ")  
    description = input("Enter a description for the expense: ")

    add_expense_data(user[2], amount, category, payment_mode, description)
    print("Expense data added successfully..!!!")


def user_profile(user):
    print("\n================= User Profile =================")
    print(f"ID : {user[0]}")
    print(f"Name : {user[1]}")
    print(f"Username : {user[2]}")
    print(f"Password : ********")
    print(f"Phone No. : {user[4]}")
    print("===================================================\n")



def dashboard(user):

    print(f"\n================= Welcome {user[1]} to the Dashboard....!!! =================")

    while True:

        print("==================================================================")
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. View All Transaction")
        print("4. Search Transaction")
        print("5. Monthly Report")
        print("6. Category Analysis")
        print("7. Budget Management")
        print("8. Export Report")
        print("9. View Profile")
        print("10. Logout")

        choice = input("\nEnter your choice = ")

        if choice == '1':
            print("\n")
            add_income(user)
            # print("Add Income")

        elif choice == '2':
            # print("Add Expense")
            print("\n")
            add_expense(user)

        elif choice == '3':
            # print("View All Transaction")
            print("\n")
            view_all_transactions(user)

        elif choice == '4':
            # print("Search Transaction")
            print("\n")
            search_transactions(user)

        elif choice == '5':
            # print("Monthly Report")
            print("\n")
            all_report(user)

        elif choice == '6':
            # print("Category Analysis")
            category_analysis(user)

        elif choice == '7':
            # print("Budget Management")
            budget_mnmg(user)

        elif choice == '8':
            # print("Export Report")
            export_report(user)

        elif choice =='9':
            # print("Profile")
            user_profile(user)

        elif choice == '10':
            print("Logging out....")
            break

        else:
            print("Invalid Choice")