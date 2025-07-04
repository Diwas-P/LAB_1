a=[]
for num in range(1,51):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    if count==2:
        a.append(num)
print(a)  
b=int(input("Enter a number:"))
if b in a:
    print(f"{b} is Prime number less than 50")
else:
    print(f"{b} is not a prime number less than 50")