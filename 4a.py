isTrue = False
str0ne = "One"
strThree = "Three"
a = 2
b = 2
c = [1, 2, 3]
d = [1, 2, 3]
if a == b:
    print("a equals b")
if c == d:
    print("c equals d")
if a is b:
    print("a is b")
if c is d:
    print("c is d")
age = int(input("enter your age: "))
if 0 < age < 120:
    print("ok")
my_names = ["adi", "ben", "noam", "arthur", "ron"]
my_list = []
if my_list:
    print("my_list is not empty")
if my_names:
    print("my_names is not empty")
if len(my_names) > 2:
    print("i remember enough names")
print(len(my_names))

if "zohar" in my_names:
    print("found Zohar")

if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal b")
elif str0ne != strThree:
    print("hello")
else:
    print("a is greater than b")

print(a < b)