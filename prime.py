number=eval(input("enter the prime number"))
if(not isinstance(n,int)):
 print("wrong input")
num=3
if num >1:
         for i in range(2,num):
             if(num%i)==0:
                 print(num,"is not a prime num")
                 print(i,"itemes",num/i,"is",num)

             else:
                 print(num,"num isnot a prime num")


