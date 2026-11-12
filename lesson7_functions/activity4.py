choice = input("What shape would you like to calculate the perimeter of? (square/rectangle): ")
if choice == "square":
    side = float(input("Enter the side length: "))
    print("Perimeter is", 4 * side)
elif choice == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    print("Perimeter is", 2 * (length + width))
else:
    print("Invalid input")