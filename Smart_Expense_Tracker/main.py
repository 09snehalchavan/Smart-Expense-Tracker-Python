from database import check_user_login, create_table,register_user, check_user_exists, update_user_password

from dashboard import dashboard
from expense import create_expense_table
from income import create_income_table
from budget import create_budget_table



create_table()
create_income_table()
create_expense_table()
create_budget_table()

def user_registration():
    # Get user input for registration

    #id = int(input("Enter your ID: "));
    name = input("Enter your name: ");
    username = input("Enter a username: ");
    password = input("Enter a password: ");
    confirm_password = input("Confirm your password: ");
    phone_number = input("Enter your phone number: ");

    if len(password) < 8:
        print("Password must be at least 8 characters long. Please try again.");
        return        
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return

    if check_user_exists(username):
        print("Username already exists. Please choose a different username.");
        return
    
    if not phone_number.isdigit() or len(phone_number) != 10:
        print("Invalid phone number. Please enter a 10-digit phone number.");
        return

        # Here you would add code to save the username and password securely
    register_user(name, username, password, phone_number)
    print("Registration successful!");

def user_login():
    # Get user input for login
    username = input("Enter your username: ");
    password = input("Enter your password: ");

    user = check_user_login(username, password)

    if user:
        # print("Login successful!");
        dashboard(user)
    else:
        print("Invalid username or password. Please try again.");

def password_reset():
        # Get user input for password reset
        username = input("Enter your username: ");

        if not check_user_exists(username):
            print("Username does not exist. Please try again.");
        else:
            new_password = input("Enter your new password: ");
            confirm_password = input("Confirm your new password: ");

            if len(new_password) < 8:
                print("Password must be at least 8 characters long. Please try again.");
                return

            if new_password != confirm_password:
                print("Passwords do not match. Please try again.");
                return

            # Here you would add code to update the user's password in the database
            update_user_password(username, new_password)
            print("Password reset successful!");
    


while True:
    print("\n\n*=*=*=*=*=*=*=*=*=*= Wel-Come To Smart Expense Tracker *=*=*=*=*=*=*=*=*=*=\n")
    print("1. Register");
    print("2. Login");
    print("3. Password Reset");
    print("4. Exit");
    print("\n")

    choice = input("Enter your choice: ");

    if choice == '1':
        print("\n")
        user_registration()
       
    elif choice == '2':
        print("\n")
        user_login()
        # Get user input for login

    elif choice == '3':
        
        # Get user input for password reset
        print("\n")
        password_reset()
    
    elif choice == '4':

        # Exit the program

        print("\nThank You So Much ..... !!!");
        break