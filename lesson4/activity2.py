upper=(int(input("Enter a number: ")))
lower=(int(input("Enter a number: ")))

print("The numbers between", lower, "and", upper, "are:")

for j in range(lower, upper+1):
    if j>1:
        for q in range(2,j):
            if j % q == 0:
                break
        else:
            print(j)