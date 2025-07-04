print("Enter 10 intgers")
p=0
n=0
z=0
for i in range(1,11):
    a=int(input("Enter a numb:"))
    if(a>0):
        p+=1
    elif(a<0):
        n+=1
    else:
        z+=1
print(f"Positive:{p}")
print(f"Negative:{n}")
print(f"Zero:{z}")