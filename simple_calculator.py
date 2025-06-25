# 🧮 6. Simple Calculator
# Input: 5 + 3 or 12 / 4
# Outputs the result.
# Use eval() with care or custom logic with operator module.

print("Simple Calculator!")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operator"
            
print(f"Result: {result}")