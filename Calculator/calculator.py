# Function to display the calculator menu
def display_menu():
    print("Welcome to the Python Calculator!")
    print("Please select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

# Function to get and validate user's choice
def get_user_choice():
    choice = input("Enter your choice (1-5): ")
    while choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (1-5): ")
    return int(choice)

# Function to perform the selected operation
def perform_operation(choice, num1, num2):
    if choice == 1:
        result = num1 + num2
        operation = "+"
    elif choice == 2:
        result = num1 - num2
        operation = "-"
    elif choice == 3:
        result = num1 * num2
        operation = "*"
    else:
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return
        operation = "/"
    print(f"Result: {num1} {operation} {num2} = {result:.2f}\n")

# Main calculator function
def calculator():
    display_menu()

    # Get user's choice
    choice = get_user_choice()

    # If user doesn't choose to exit
    if choice != 5:
        try:
            # Get user input for two numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
            calculator()  # Restart the calculator if there is an error

        # Perform the selected operation and display the result
        perform_operation(choice, num1, num2)

        # Recursive call to continue the calculator
        calculator()
    else:
        print("Exiting the program...")

# Start the calculator
calculator()
