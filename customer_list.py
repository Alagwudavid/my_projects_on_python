customer_list = []
while True:
    question = input("New Customer? (y/n): ")
    if question == "y":
        first_name, last_name = input("Enter full name: ").split()
        customer_list.append({'fName': first_name, 'lName': last_name})
    elif question == "n":
        for names in customer_list:
            print("=" * 6)
            print("Customer list::")
            print("=" * 6)
            print(names['fName'], names['lName'])
        break
    else:
        print("insert either 'y' or 'n'")