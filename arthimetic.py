print("Select an Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
choice=int(input("1-4:"))
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if(choice==1):
    result=num1+num2
elif(choice==2):
    result=num1-num2
elif(choice==3):
    result=num1/num2
else:
    result=num1*num2
print(result)