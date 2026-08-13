# Python Calculators
n1 = float(input("Enter the 1st number: "))
n2 = float(input("Enter the 2nd number: "))
op =input(" Enter the arithmetic operator:")
if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '/':
    if n2 == 0 :
        result = "MATH ERROR: You cannot use zero here"
    else:
        result = n1 / n2
elif op == '*':
    result = n1 * n2
elif op == '%':
    if n2 == 0 :
        result = "MATH ERROR: You cannot use zero here"
    else:
        result = n1 % n2
elif op == '**':
    if n1 == 0 and n2 <= 0:
        result = "MATH ERROR: Invalid power"
    else:
        result = n1 ** n2
else:
    result = "MATH ERROR"
print(f"Result = {result}")
