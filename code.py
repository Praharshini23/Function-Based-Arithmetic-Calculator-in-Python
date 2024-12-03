def calculator():
    while True:
        print("\n--- Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (^)")
        print("7. Floor Division (//)")
        print("8. Exit")

        # Get user choice
        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4', '5', '6', '7'):
            print("Invalid choice. Please try again.")
            continue

        try:
            # Input numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Perform calculations
            if choice == '1':
                print(f"The result of addition is: {num1 + num2}")
            elif choice == '2':
                print(f"The result of subtraction is: {num1 - num2}")
            elif choice == '3':
                print(f"The result of multiplication is: {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"The result of division is: {num1 / num2}")
                else:
                    print("Error: Division by zero is not allowed.")
            elif choice == '5':
                print(f"The result of modulus is: {num1 % num2}")
            elif choice == '6':
                print(f"The result of exponentiation is: {num1 ** num2}")
            elif choice == '7':
                if num2 != 0:
                    print(f"The result of floor division is: {num1 // num2}")
                else:
                    print("Error: Division by zero is not allowed.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")

# Run the calculator
calculator()
