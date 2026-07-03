from database import create_connection

create_connection()


def create_budget_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        create table if not exists budget(
            budget_id integer primary key autoincrement,
            username text unique,
            budget_amount real not null
        )
    """)

    conn.commit()
    conn.close()


def set_budget(user):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        select * from budget
        where username = ?
    """, (user[2],))

    record = cursor.fetchone()

    if record:
        print("\nBudget already exists.")
        print("Please choose Update Budget.\n")
        conn.close()
        return

    budget = float(input("Enter Budget Amount : "))

    cursor.execute("""
        insert into budget(username, budget_amount)
        values(?, ?)
    """, (user[2], budget))

    conn.commit()
    conn.close()

    print("\nBudget Set Successfully.\n")


def update_budget(user):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        select budget_amount
        from budget
        where username = ?
    """, (user[2],))

    old_budget = cursor.fetchone()

    if old_budget is None:
        print("\nNo Budget Found.")
        print("Please Set Budget First.\n")
        conn.close()
        return

    add_budget = float(input("Enter Amount to Add : "))

    new_budget = old_budget[0] + add_budget

    cursor.execute("""
        update budget
        set budget_amount = ?
        where username = ?
    """, (new_budget, user[2]))

    conn.commit()
    conn.close()

    print("\nBudget Updated Successfully.")
    print(f"Old Budget : ₹{old_budget[0]:.2f}")
    print(f"Added      : ₹{add_budget:.2f}")
    print(f"New Budget : ₹{new_budget:.2f}\n")


def view_budget(user):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        select budget_amount
        from budget
        where username = ?
    """, (user[2],))

    budget = cursor.fetchone()

    if budget is None:
        print("\nNo Budget Found.")
        print("Please Set Budget First.\n")
        conn.close()
        return

    budget_amount = budget[0]

    cursor.execute("""
        select ifnull(sum(amount),0)
        from expense
        where username = ?
    """, (user[2],))

    total_expense = cursor.fetchone()[0]

    remaining = budget_amount - total_expense

    print("\n========== Budget Status ==========")
    print(f"Budget Amount : ₹{budget_amount:.2f}")
    print(f"Total Expense : ₹{total_expense:.2f}")

    if remaining >= 0:
        print(f"Remaining Budget : ₹{remaining:.2f}")
    else:
        print(f"Budget Exceeded By : ₹{-remaining:.2f}")

    print("=" * 35)

    conn.close()


def budget_mnmg(user):

    while True:

        print("\n========== Budget Management ==========")
        print("1. Set Budget")
        print("2. Update Budget")
        print("3. View Budget Status")
        print("4. Back")

        choice = input("Enter Your Choice : ")

        if choice == "1":
            set_budget(user)

        elif choice == "2":
            update_budget(user)

        elif choice == "3":
            view_budget(user)

        elif choice == "4":
            break

        else:
            print("Invalid Choice.")