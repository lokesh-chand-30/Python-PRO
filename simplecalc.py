x = int(input("Enter a decimal no: "))
y = int(input("Enter another decimal no: "))
opn = input("SELECT AN OPERATION +,-,*,%: ")
print("Your selected operation is:",opn)
if(opn == '+'):
     print("The result is",x+y)
elif(opn == '-'):
    print("The result is",x-y)
elif(opn == '*'):
    print("The result is",x*y)
elif(opn == '%'):
    print("The result is",x%y)
else:
    print("Invalid operation")