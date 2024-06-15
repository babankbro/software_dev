user_db = "Sarayut"
password_db = "1234"
user = input("Enter your username:")
password = input("Enter your password:")

if user == user_db and password == password_db:
    print("Login success!")
elif password == password_db:
    print("Username is incorrect.")
else:
    print("Password is incorrect.")

