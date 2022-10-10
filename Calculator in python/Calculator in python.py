num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

#add 2 numbers
def Add (num1, num2):
    return num1 + num2

#subtract 2 numbers
def Sub (num1, num2):
    return num1 - num2  

#multiply 2 numbers
def Multiply (num1, num2):
    return num1 * num2  

#divide 2 numbers
def Divide (num1, num2):
    if(num2 == 0):
        print("error.. enter another value")
    else:
        return num1 / num2    

print("Select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

process = int(input("Select operations form 1, 2, 3, 4 :"))

if (process==1):
    print(num1, "+", num2, "=", Add(num1,num2))
elif (process==2):
    print(num1, "-", num2, "=", Sub(num1,num2))
elif (process==3):
    print(num1, "*", num2, "=", Multiply(num1,num2))  
elif (process==4):
    print(num1, "/", num2, "=", Divide(num1,num2))  
else:
    print("Not valid..")   