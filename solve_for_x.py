# receive input and split
x, plus, num1, equals, num2 = input("Enter equation: ").split(" ")

# convert strings to int
num1 = int(num1)
num2 = int(num2)

# convert result to string and concatenate to string x = " "
x = str(x)
# print()
print("x = {}".format(num2 - num1))