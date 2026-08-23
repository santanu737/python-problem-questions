def dosum(num):
    total=0
    while num>0:
        digit=num% 10 
        total=total+digit
        num=int(num/10)
    return total 

n=int (input("enter a number:"))
print("sum is :" ,dosum(n))


