customer_list = []
while True:
    question = input("New Customer? (y/n): ")
    if question == "y":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        Age = int(input("Age: "))
        Phone_number = int(input("Contact No: "))
        customer_list.append({'fName': first_name, 'lName': last_name, 'Age': Age, 'Mobile': Phone_number})
    elif question == "n":
        for names in customer_list:
            print("=" * 18)
            print("Customer list::")
            print("=" * 18)
            print("Full Name --- Age --- Contact number")
            print("-" * 18)
            print(names['fName'], names['lName'], "-", names['Age'], "-", names['Mobile'])
        break
    else:
        print("insert either 'y' or 'n'")