n=eval(input("enter the number"))
if(not isinstance(n,int)):
  print("worng input")


else:
    if(n>10):
       if(n%10==0):
           print("n of multiple numbers of 10")
       else:
           print("not divisible")
    else:
        if(n>50):
            print("n is gater then 50")
        else:
            if(n%multiplier ==0):
                print("the num",n,"is a multipel of number",multiplier)
            else:
                print("the num",n"is a multipel of number",multiplier)



