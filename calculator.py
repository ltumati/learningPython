def add(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def divide(x,y):
    return x / y

print("select operation")
print("1.add")
print("2.subtraction")
print("3.multiplication")
print("4.divide")
choice =input("enter the choice (1/2/3/4):")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

if choice  == 1:
    print(num1,"+", num2 ,"= ", add(num1,num2))

elif choice  == 2:
    print(num1 , "-" ,num2 , "=", subtraction(num1,num2))
    print("asdfsfadsfasdfsfsdfasf")

elif choice  == 3:
    print(num1 ,"*", num2 ,"=" ,multiplication(num1,num2))

elif choice  == '4':
    print(num1 ,"/", mum2, "=" ,divide(num1, num2))

else:
    print("invalid number")
   

