try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a / b)
    r = open("file_not_exists.txt")
except Exception as e:
    print("somting went wrong")
    print(e.args)
print("blablablablaa")
