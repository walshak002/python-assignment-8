"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""
class calculator:
    def add(self, o, x):
        return o + x
    def subtract(self, o, x):
        return o - x
    def multiply(self, o, x):
        return o * x
    def divide(self, o, x):
        if x == 0:
             return "Error: Division by zero is not allowed."
        return o / x
    
cal = calculator()

print(cal.add(5, 5))
print(cal.subtract(5, 2))
print(cal.multiply(5,4))
print(cal.divide(10, 0))

    