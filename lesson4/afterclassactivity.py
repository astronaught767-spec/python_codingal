decimal_number = int(input("Enter a decimal number: "))

if decimal_number == 0:
	binary_number = "0"
else:
	binary_number = ""
	number = abs(decimal_number)

	while number > 0:
		remainder = number % 2
		binary_number = str(remainder) + binary_number
		number //= 2

	if decimal_number < 0:
		binary_number = "-" + binary_number

print("Binary number:", binary_number)
