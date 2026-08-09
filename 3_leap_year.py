y=int(input("enter a year: "))

if(y %4 == 0 and y %100 !=0)or(y%400==0):
    print("this year is  a leap year")
else:
    print("thisis not a leap year")