
#####Loop
for i in range (0,5):
    print(i)

i=1
while i<8:
    print("shruti")
    i=i+2

###   If ELSE 
input_num  = float(input("enter number of your choice: "))
print(input_num)
if (input_num>0):
    print("positive")
elif (input_num==0):
    print("zero")
else:
    print("negative")


input_num  = float(input("enter number of your choice: "))
if (input_num%2 ==0):
    print("even")
else:
    print("odd")    

#####  CASE STATEMENT
input_num  = int(input("enter number of your choice: "))
match input_num: 
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")



    #####  CASE STATEMENT
input_num1 = int(input("enter first number of your choice: "))
input_num2 = int(input("enter second number of your choice: "))
operation = input("what do you want - +,-,*,% ")
match operation: 
    case "+":
        print(input_num1 + input_num2)
    case "-":
        print(input_num1-input_num2)
    case "*":
        print(input_num1*input_num2)
    case "%":
        print(float(input_num1/input_num2))
    