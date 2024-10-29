# Can a newborn baby in Nigeria expect to live for one billion (109 ) seconds?
# Write a Python program for doing arithmetics to answer the question.

life_expectancy = 55

# seconds = input("Enter years in seconds: ")
# seconds = int(seconds)

seconds = 10**9

seconds_2_year = 31536000

result_in_years = seconds / seconds_2_year

if result_in_years > life_expectancy:
    print(f"A newborn cannot live upto {result_in_years:.0f} years. based on current life_expectancy: {life_expectancy}years")
elif result_in_years < life_expectancy:
    print(f"A newborn can live upto {result_in_years:.0f} years. based on current life expectancy: {life_expectancy}years")
else:
    print("Please input a valid value: ")