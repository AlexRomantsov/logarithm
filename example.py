from logarithm import log

number = input("number: ")
base = input("base: ")
result = log(number, base)
print("result = " + str(result))
print(log.__doc__)
input("Please press enter ")