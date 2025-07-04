a = int(input("Enter a number: "))
if a > 1:
    p = True
    for i in range(2, a):
        if a % i == 0:
            p = False
            break
    if p:
        print("Prime")
    else:
        print("Not Prime")
else:
    print(" Wrong Value")