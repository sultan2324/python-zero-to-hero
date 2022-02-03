
def fact(n):
    factorial = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        while 1 < n:
            factorial *= n
            n -= 1
        return factorial


num = int(input("Enter a number to find factorial : "))
print("Factorial of ", num, " is : ", fact(num))
