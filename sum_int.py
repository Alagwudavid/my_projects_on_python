# Write a program that computes the sum of the integers from 1 up to and including n.
# Compare the result with the famous formula n(n + 1)/=2.
print(f"{'Integer':<25} {'Sum':<25} {'Comparison':<25}")
print("-"*70)
for n in range(1, 101):
    print(f"{n:<25} {sum(range(1, n + 1)):<25} {((n * (n + 1)) // 2):<25}")