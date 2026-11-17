def cube(num):
    return num ** 3

def execute(num):
    if num%3==0:
        return cube(num)
    else:
        return False

print(execute(9))
print(execute(10))