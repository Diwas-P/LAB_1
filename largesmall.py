import random 
l1=[random.randint(1,100) for _ in range(10)]
print(l1)
large=l1[0]
small=l1[0]
for i in l1:
    if(i>large):
        large=i
    if(i<small):
        small=i
print(f"{large} is Largest")
print(f"{small} is smallest")