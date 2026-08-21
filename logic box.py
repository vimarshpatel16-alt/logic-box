

print("Welcome to the Pattern Generator and Number Analyzer!")
print()

while True:
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        rows = int(input("Enter the number of rows for the pattern: "))
        print("\nPattern:")

        for i in range(1, rows + 1):
            print("*" * i)

        print()

    elif choice == 2:
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        total = 0

        for num in range(start, end + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")

            total += num

        print(f"Sum of all numbers from {start} to {end} is: {total}")
        print()

    elif choice == 3:
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        print()

presentation linkk-https://drive.google.com/drive/folders/1b8TnZBpXxMHKusFRD9UTlRkXkaESiTQ_
