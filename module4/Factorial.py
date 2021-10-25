def factorial(num):
    are = 1
    for i in range(1, num+1):
        are *= i
    return are

num = int(input("Input a number: "))
print(factorial(num))
