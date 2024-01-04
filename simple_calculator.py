import math
def calculator(num1, num2):
    num1, sign, num2 = input(": ").split(" ")
    num1 = int(num1)
    num2 = int(num2)
    answer = int(answer)

    if sign == "*":
        answer = num1 * num2
        # print("ans: {}".format(answer))

    elif sign == "+":
        answer = num1 + num2
        # print("ans: {}".format(answer))

    elif sign == "/":
        answer = num1 / num2
        # print("ans: {}".format(answer))

    elif sign == "%":
        answer = num1 % num2
        # print("ans: {}".format(answer))

    else:
        print("Enter a valid value...e.g. 2 + 3")

    return num1, num2, answer
print("Value: ", calculator(num1, sign, num2, answer))