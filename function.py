def check_password(password):
    if password == "python123":
        print("Access Granted !!")
    else:
        print("Access Denied !!")


password = input("Enter your password: ")
check_password(password)