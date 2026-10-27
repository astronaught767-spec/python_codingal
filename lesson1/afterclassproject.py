# make a class that lets only age 10-20 users access it


age = int(input("Please enter your age: "))

if age >=10 and age <=20:
    print("Access granted. Welcome!")
    
else:
     print("You are either too young or too old to access this class. Access denied.") 
