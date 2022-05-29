from functools import partial
DogPrefix = "Dog bark sounds like: "

isTrue = False
a = 2
b = 2.5
strOne = "One"
strThree = "Tree"
if a < b:
    print("%d is lower than %f" % (a, b))
if strOne != strThree:
    print("Strings are different")
else:
    print("Strings are the same")
if a < b and strOne != strThree:
    print("a is lower than b and the strings are not equal")
if isTrue:
    print("Never going to happen")
elif not isTrue:
    print("Always going to happen")