n= int(input("Enter a number: "))

count = 0
digits = abs(n)

if digits == 0:
	count = 1
else:
	while digits > 0:
		count += 1
		digits //= 10

print("Number of digits:", count)
