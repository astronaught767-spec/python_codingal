n= int(input("Enter any number greater than 1"))
if n<1:
    print("Please enter a number greater than 1")
else:
    for i in range(n,0,-1):
        print(i)