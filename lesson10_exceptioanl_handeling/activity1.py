try:
    num1,num2=eval(input("type 2 #'s seperated by comma:"))
    result=num1/num2
    print("resultis", result)

except ZeroDivisionError:
    print("Division by 0 is error")

except SyntaxError:
    print("The format should be x,y")

except:
    print("Wrong input")

else:
    print("No exceptions")

finally:
    print("this will execute no matter what")