# a = int(input("Enter your age: "))
# if 0 < a < 120:
#     print("Ok")
# else:
#     print("Not Ok")
# b = int(input("Enter amount of pets: "))
# if 0 < b < 4:
#     print("Ok")
# else:
#     print("Not Ok")
#
#
def validate(prompt, low, high, ok, not_ok):
    input_from_user = int(input(prompt))
    if low < input_from_user < high:
        return ok
    else:
        return not_ok


print(validate("Enter your age: ", 0, 120, "age is good", "age is not good"))
print(validate("Enter amount of pets: ", 0, 4, "You are a good person", "you are a better person"))

