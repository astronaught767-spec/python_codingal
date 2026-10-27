# make a class that lets only age 10-20 users access it


age = int(input("Please enter your age: \n"))

if age >=10 and age <=20:
    print("Access granted. Welcome!\n")
    
else:
    print("You are either too young or too old to access this class. Access denied.\n")
