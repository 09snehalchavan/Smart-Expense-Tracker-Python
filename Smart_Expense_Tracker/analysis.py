from database import create_connection

create_connection()

def category_analysis(user):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
            select category, sum(amount)  from expense
                where username = ? group by category    
    ''', (user[2],))

    records = cursor.fetchall()

    if not records:
        print("No expense records found.")
        conn.close()
        return
    

    print("\n========== Category Analysis ==========")
    # print("-" * 45)
    print(f"{'Category':<20} {'Total Expense'}")
    print("-" * 45)

    for category, total in records:
        print(f"{category:<20} ₹{total:.2f}")

    print("-" * 45)

    conn.close()