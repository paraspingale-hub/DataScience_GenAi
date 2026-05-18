import Arithmetic

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Calling functions from the Arithmetic module
        addition = Arithmetic.Add(num1, num2)
        subtraction = Arithmetic.Sub(num1, num2)
        multiplication = Arithmetic.Mult(num1, num2)
        division = Arithmetic.Div(num1, num2)
        
        print("\n--- Results ---")
        print(f"Addition: {addition}")
        print(f"Subtraction: {subtraction}")
        print(f"Multiplication: {multiplication}")
        print(f"Division: {division}")
        
    except ValueError:
        print("Please enter valid numbers.")