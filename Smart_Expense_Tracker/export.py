from database import create_connection

create_connection()

def export_report(user):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        select 'Income' AS Type, amount, source, payment_mode, income_date from income where username = ?
                   union all
                   select 'Expense' AS Type, amount, category, payment_mode, expense_date from expense where username = ?
    ''', (user[2], user[2]))

    data = cursor.fetchall ()
    file = open("report.txt", "w")
    for i in data:
        
        file.write(str(i)+"\n")

    file.close()

    print("\n=========================================")
    print("   Report Exported Successfully...!!!")
    print("   File Name : report.txt")
    print("=========================================")


    # file.write(data)
    # close(file)

    conn.commit()
    conn.close()