# F = (9/5) * C + 32
# Write a Python program that prints out a table with
# Fahrenheit degrees 0, 10, 20, ..., 100 in the first
# column and the corresponding Celsius degrees in the second column.

print(f"{'Farenheit(*F)':<25} {'Celsius(*C)':<50}")
print("-"*50)
for f in range(0, 101, 10):
    print(f"{f:<25} {(f - 32)*(5/9):<50.2f}")
    # print(f"{n:<25} {((9/5) * n)+32:<50.2f}")