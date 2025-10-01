def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def main():
    print("Welcome to 021 Calculator")
    while True:
        print("\nOptions: add, subtract, multiply, divide, exit")
        choice = input("Choose operation: ").lower()

        if choice == "exit":
            print("Exiting 021 Calculator. Bye!")
            break

        if choice in ["add", "subtract", "multiply", "divide"]:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if choice == "add":
                print("Result:", add(x, y))
            elif choice == "subtract": 
                print("Result:", subtract(x, y))
            elif choice == "multiply": 
                print("Result:", multiply(x, y))
            elif choice == "divide":
                print("Result:", divide(x, y))
        else: 
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
