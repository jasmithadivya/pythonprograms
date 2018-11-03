n=eval(input("enter the number"))
if(not isinstance(n,int)):
  print("worng input")


else:
    if(n>10):
       if(n%10==0):
           print("n of multiple numbers of 10")
       else:
           print("not divisible")