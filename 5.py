my_names = ["adi", "ben", "noam", "arthur", "ron"]
for i in range(5):
    print(f"hello world #{i}")
for name in my_names:
    print(f"hello {name}")
    if name == "arthur":
        break
else:
    print("printed all names")
    print(f"hell")
for i in range(len(my_names)):
    print(my_names[i])
a = 0
while a < 5:
    print(a)
    a = a + 1

l = []
current_input = input("enter letter: ")
while current_input != "q":
    l.append(current_input)
    current_input = input("enter letter: ")

print(f"inputs are {l}")

n = [1, 2, 3, 4, 5]
results = [num * 2 for num in n if num > 2]

