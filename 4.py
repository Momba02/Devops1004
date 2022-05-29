def square(number):
    return number*number

def bark():
    print(DogPrefix + "Whoof! Whoof!")

def miao(catsound="Miao! Miao!"):
    return print(catsound)
def makeasound(sound):
    sound()
print(square(7))
miao("Hatoola")
makeasound(bark)
makeasound(miao)
makeasound(partial(miao, "Miaoooooo!"))
myDict = {"name": "aviel",
"age": 28,
"hobbies": ["Skiing", "Cooking"],
"children": None}
print(myDict["name"])
myDict["age"] = 29
print(list(myDict.keys()))
print(list(myDict.values()))
print("Enter your name:", end =" ")
name = input()
print("Have a good day " + name)