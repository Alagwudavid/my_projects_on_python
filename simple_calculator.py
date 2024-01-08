def calculator():
    num1, sign, num2 = input("clc: ").split()
    num1 = int(num1)
    num2 = int(num2)
    if sign == "*":
        answer = num1 * num2
        print("ans: {}".format(answer))
    elif sign == "+":
        answer = num1 + num2
        print("ans: {}".format(answer))
    elif sign == "/":
        answer = num1 / num2
        print("ans: {}".format(answer))
    elif sign == "%" and num2 > 0:
        answer = num1 % num2
        print("ans: {}".format(answer))
    else:
        print("Invalid operator. Please use +, -, *, /, or %.")
calculator()