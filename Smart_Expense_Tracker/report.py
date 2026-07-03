from database import create_connection

create_connection()

def all_report(user):
    
    while True:
        print("\n========== Report Menu ============\n")
        print("1. Financial Summary")
        print("2. Income Report")
        print("3. Expense Report")
        print("4. Back")
        print("\n===================================\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            # print("Financial Summary Report")
            financial_report(user)

        elif choice == '2':
            income_report(user)

        elif choice == '3':
            expense_report(user)

        elif choice == '4':
            break

        else:
            print("Invalid choice.....")
    

def financial_report(user):

    conn = create_connection()
    cursor = conn.cursor()

    print("="*10, "Financial Summary Report", "="*10)

    cursor.execute('''
            select ifnull (sum(amount),0) from income where username = ?
        ''', (user[2],))
    
    total_income = cursor.fetchone()[0]

    cursor.execute('''
            select ifnull (sum(amount),0) from expense where username = ?
        ''', (user[2],))
    
    total_expense = cursor.fetchone()[0]

    
    balance = total_income - total_expense

    print(f"Total Income = {total_income}")
    print(f"Total Expense = {total_expense}")
    print(f"Balance = {balance}")
    print("="*90,"\n")

    conn.commit()
    conn.close()

def income_report(user):
    conn = create_connection()
    cursor = conn.cursor()

    print("="*10, "Income Report", "="*10,"\n")
    cursor.execute('''
        select ifnull (sum(amount),0) from income where username = ?
    ''',(user[2],))

    total_income = cursor.fetchone()[0]

    cursor.execute('''
        select ifnull(max(amount),0) from income where username = ?
    ''',(user[2],))
    max_income = cursor.fetchone()[0]

    cursor.execute('''
        select ifnull(min(amount),0) from income where username = ?
    ''',(user[2],))
    min_income = cursor.fetchone()[0]

    print(f"Total Income = {total_income}")
    print(f"Highest Income = {max_income}")
    print(f"Lowest Income = {min_income}")
    print("="*90)


def expense_report(user):
    conn = create_connection()
    cursor = conn.cursor()

    print("="*10, "Expense Report", "="*10,"\n")
    cursor.execute('''
        select ifnull (sum(amount),0) from expense where username = ?
    ''',(user[2],))

    total_expense = cursor.fetchone()[0]

    cursor.execute('''
        select ifnull(max(amount),0) from expense where username = ?
    ''',(user[2],))
    max_expense = cursor.fetchone()[0]

    cursor.execute('''
        select ifnull(min(amount),0) from expense where username = ?
    ''',(user[2],))
    min_expense = cursor.fetchone()[0]

    print(f"Total Expense = {total_expense}")
    print(f"Highest Expense = {max_expense}")
    print(f"Lowest Expense = {min_expense}")
    print("="*90)