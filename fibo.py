n=int(input("Enter the number of Terms"))
a=0
b=1
c=0
if(n==0):
    print("There is no zero term")
elif(n==1):
    print(f"{a}")
else:
    for i in range(0,n):
        print(f"{a}")
        c=a+b
        a=b
        b=c