print("welcome to triangle maker would you like to make a triangle which is normal or mirrored?")
choice = input("Enter 'normal' or 'mirrored': ").strip().lower()
rows = int(input("Enter the number of rows: "))

if choice == "normal":
    for i in range(1, rows + 1):
        print("*" * i)
elif choice == "mirrored":
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
else:
    print("Invalid choice. Please enter 'normal' or 'mirrored'.")