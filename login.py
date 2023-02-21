username = input("Enter username:")
password = input("Enter password:")

print(username)
print(password)

# เขียนเงื่อนไขตรวจสอบ username/password
if (username == "admin" and password == "1234"):
    print("Login success")
else:
    print("Login fail")
