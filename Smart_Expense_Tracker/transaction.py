from database import create_connection

create_connection()

def view_all_transactions(user):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        select 'Income' AS Type, amount, source, payment_mode, income_date from income where username = ?
                   union all
                   select 'Expense' AS Type, amount, category, payment_mode, expense_date from expense where username = ?
    ''', (user[2], user[2]))

    transactions = cursor.fetchall()


    if not transactions:
        print("No transactions found for the user.")
        return

    # print("\nType\t\tAmount\t\tCategory\t\tPayment\t\tDate")
    print("-" * 95)
    print(f"{'Type':<10} {'Amount':>10} {'Category':<20} {'Payment':<15} {'Date'}")
    print("-" * 95)

    for row in transactions:
        transaction_type, amount, category, payment, date = row

        # print(f"{transaction_type}\t\t{amount}\t\t{category}\t\t{payment}\t\t{date}")
        print(f"{transaction_type:<10} {amount:>10.2f} {category:<20} {payment:<15} {date}")
    
    print("-" * 95)
    # conn.commit()
    conn.close()


#Search Transaction

def search_transactions(user):

    while True:
        print("\n========== Search Transaction ==========")
        print("1. Search by Payment Mode")
        print("2. Search by Category")
        print("3. Back")

        choice = input("Enter your choice : ")

        if choice == '1':
            conn = create_connection()
            cursor = conn.cursor()

            search_payment_mode = input("Enter the Payment Mode to search transactions: ")

            cursor.execute('''
                SELECT 'Income' AS Type, amount, source, payment_mode, income_date FROM income WHERE username = ? and lower(payment_mode) = lower(?)
                UNION ALL
                SELECT 'Expense' AS Type, amount, category, payment_mode, expense_date FROM expense WHERE username = ? and lower(payment_mode) = lower(?)
                ''', (user[2],search_payment_mode, user[2],search_payment_mode))

            transactions = cursor.fetchall()

            if not transactions:
                print("No transactions found for the given payment mode.")
        
            print(f"{'Type':<10} {'Amount':>10}\t\t {'Category':<20} {'Payment':<15} {'Date'}")
            print("-" * 95)
            for row in transactions:
                transaction_type, amount, category, payment, date = row
                print(f"{transaction_type:<10} {amount:>10.2f} \t\t{category:<20} {payment:<15} {date}")
        
        elif choice == '2':
            conn = create_connection()
            cursor = conn.cursor()

            search_category = input("Enter the Category to search transactions: ")

            cursor.execute('''
                SELECT 'Income' AS Type, amount, source, payment_mode, income_date FROM income WHERE username = ? and lower(source) = lower(?)
                UNION ALL
                SELECT 'Expense' AS Type, amount, category, payment_mode, expense_date FROM expense WHERE username = ? and lower(category) = lower(?)
                ''', (user[2],search_category, user[2],search_category))

            transactions = cursor.fetchall()

            if not transactions:
                print("No transactions found for the given category.")
        
            print(f"{'Type':<10} {'Amount':>10}\t\t {'Category':<20} {'Payment':<15} {'Date'}")
            print("-" * 95)
            for row in transactions:
                transaction_type, amount, category, payment, date = row
                print(f"{transaction_type:<10} {amount:>10.2f} \t\t{category:<20} {payment:<15} {date}")        

        elif choice == '3':
            break

        else:
            print("Invalid Choice")


   