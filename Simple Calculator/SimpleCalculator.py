def calculator():
    print("Welcome to the Simple Calculator!")
    print("Enter 'exit' to quit.")

    while True:
        expression = input("Enter an expression (e.g., 5+4 or 10-3): ")
        if expression.lower() == 'exit':
            break
        
        try:
            result = eval(expression)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print(f"Invalid input. Please enter a valid expression. Error: {e}")

calculator()
