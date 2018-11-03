num = int(input("enter a number of factorial :"))
factorial = 1
if num < 0:
    print("please enter a positive integer")
else:

    print("the factorial of 0 is")
    for i in range(1,num+1):
        factorial=factorial*i


print(factorial)

