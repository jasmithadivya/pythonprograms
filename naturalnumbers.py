n=eval(input("enter the ending number to add for natural numbers"))
if(not isinstance(n,int)):
    print("worng input")

if(n>0):
    sum=(n*(n+1))/2
    print("sum of natural numbers is",sum)
else:
    print("error!!!")




