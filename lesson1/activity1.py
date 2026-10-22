medical_cause= input("Did/do u have a medical cause?")


atten=0

if  medical_cause.upper()=="Y":
    print("You are allowed to attend the exam.\n")
else:
    atten=int(input("what is your attendace percentage\n"))
    if atten>=75:
        print("You are allowed to attend the exam.\n")
    else:
        print("You are not allowed to attend the exam.\n")