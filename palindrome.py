n=int(input("Enter a number"))
a=str(n)
if(a==a[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")