def calculator():
    # num1, sign, num2 = input("Calculator: ").split()
    num1 = int(input("value one: "))
    sign = input("input sign: ")
    num2 = int(input("value two: "))
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
    elif sign == "-" and num2 > 0:
        answer = num1 - num2
        print("ans: {}".format(answer))
    else:
        print("Invalid operator. Please use +, -, *, /, or %.")
calculator()