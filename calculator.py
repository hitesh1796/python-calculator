def sum(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def modulus(a,b):
    return a%b

def power(a,b):
    return a**b
    

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: ."))
op = input("enter the operator(+,-,*,/,**,%):")

if op == '+':
    print(sum(num1,num2))
elif op == '-':
    print(subtract(num1,num2))
elif op =='*':
    print(multiply(num1,num2))    
elif op == '/':
    if num2 !=0 :
        print(divide(num1,num2))
    else :
        print("error: denominator cant be zero")
elif op == '**':
    print(power(num1,num2))
elif op == '%':
    if num2 != 0:
        print(modulus(num1,num2))
    else :
        print("error: denominator cant be zero")
else :
    print("invalid operator")
    