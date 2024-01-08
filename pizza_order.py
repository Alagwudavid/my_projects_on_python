print("#"*20)
print("Pizza Order Program")
print("#"*20)
one = 100
two = 200
three = 300
a = 30
b = 50
c = 20
t1 = "Small pizza"
t2 = "Medium pizza"
t3 = "Large pizza"
a1 = "pepperoni for small fries"
b1 = "pepperoni for medium or large pizza"
c1 = "extra cheese for any size pizza"
print("""main-dish
    1. Small pizza = $100
    2. Medium pizza = $200
    3. Large pizza = $300""")
mainDish = input("Select from main dish e.g one: ")
if mainDish == "one":
    sideMenu = input("Want to add some side-menu [y/n]: ").lower()
    if sideMenu == "y":
        print("""side-menu
    a. pepperoni for small fries = $30
    b. pepperoni for medium or large pizza = $50
    c. extra cheese for any size pizza = $20""")
        sideChoice = input("Choose from a-c in the menu above: ").lower()
        if sideChoice == "a":
            print(f'Your bill for "{t1}" and "{a1}" is ${one + a}')
        elif sideChoice == "b":
            print(f'Your bill for "{t1}" and "{b1}" is ${one + b}')
        elif sideChoice == "c":
            print(f'Your bill for "{t1}" and "{c1}" is ${one + c}')
    elif sideMenu == "n":
        print(f'Your bill for "{t1}" only is ${one}')
elif mainDish == "two":
    sideMenu = input("Want to add some side-menu [y/n]: ").lower()
    if sideMenu == "y":
        print("""side-menu
    a. pepperoni for small fries = $30
    b. pepperoni for medium or large pizza = $50
    c. extra cheese for any size pizza = $20""")
        sideChoice = input("Choose from a-c in the menu above: ").lower()
        if sideChoice == "a":
            print(f'Your bill for "{t2}" and "{a1}" is ${two + a}')
        elif sideChoice == "b":
            print(f'Your bill for "{t2}" and "{b1}" is ${two + b}')
        elif sideChoice == "c":
            print(f'Your bill for "{t2}" and "{c1}" is ${two + c}')
    elif sideMenu == "n":
        print(f'Your bill for "{t2}" only is ${two}')
elif mainDish == "three":
    sideMenu = input("Want to add some side-menu [y/n]: ").lower()
    if sideMenu == "y":
        print("""side-menu
    a. pepperoni for small fries = $30
    b. pepperoni for medium or large pizza = $50
    c. extra cheese for any size pizza = $20""")
        sideChoice = input("Choose from a-c in the menu above: ").lower()
        if sideChoice == "a":
            print(f'Your bill for "{t3}" and "{a1}" is ${three + a}')
        elif sideChoice == "b":
            print(f'Your bill for "{t3}" and "{b1}" is ${three + b}')
        elif sideChoice == "c":
            print(f'Your bill for "{t3}" and "{c1}" is ${three + c}')
    elif sideMenu == "n":
        print(f'Your bill for "{t3}" only is ${three}')
else:
    print("Try again!")
print("Thanks for patronising us.")