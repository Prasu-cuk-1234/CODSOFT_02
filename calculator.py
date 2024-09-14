# Function to display the menu
def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Function to perform the operation
def perform_operation(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    else:
        return None

# Main program loop
def calculator():
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter choice (1-5): "))
            if choice == 5:
                print("Exiting calculator. Goodbye!")
                break

            if choice < 1 or choice > 5:
                print("Invalid choice. Please choose a valid option.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            result = perform_operation(choice, num1, num2)
            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Running the calculator
calculator()