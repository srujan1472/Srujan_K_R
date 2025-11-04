class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower() 

    def compute(self):
        if self.operation in ("add", "+"):
            return self.a + self.b
        elif self.operation in ("subtract", "-"):
            return self.a - self.b
        elif self.operation in ("multiply", "*"):
            return self.a * self.b
        elif self.operation in ("divide", "/"):
            if self.b == 0:
                return "Error: Division by zero!"
            return self.a / self.b
        else:
            return "Invalid operation type!"

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    calc = Calculator(a, b, operation)
    result = calc.compute()

    print("Result:", result)
