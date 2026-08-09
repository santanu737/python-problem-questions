def checkarmstrong(num):
    temp=num
    sum=0

    while temp>0:
        digit=temp%10
        sum=sum+digit*digit*digit
        temp=int(temp/10)
    
    if sum==num:
        return True
    else:
        return False

n=int(input("enter your armstrong number:"))
if(checkarmstrong(n)):
    print("your no is  armstrong no")
else:
    print("this no is not a armstrong no")