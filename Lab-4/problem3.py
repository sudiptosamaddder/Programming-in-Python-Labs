base = float(input("Enter the base: "))
exp = int(input("Enter the exponent (non-negative integer): "))

result = 1
for i in range(exp):
    result *= base

print(base, "raised to the power", exp, "=", result)