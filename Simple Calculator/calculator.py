number1 = int(input("Enter the first number: "))
sign = input("Enter the operator: ")
number2 = int(input("Enter the second number: "))

if sign == '+':
    print('Addition of these number is: ' +  str(number1 + number2))
elif sign == '-':
    print('Subtraction of these number is: ' +  str(number1 - number2))
elif sign == '*':
    print('Multiplication of these number is: ' +  str(number1 * number2))
elif sign == '/':
    if number2 != 0:
        print('Division of these number is: ' +  str(number1 / number2))
    else:
        print('Error')
elif sign == '%':
    print('Modulas of these number is: ' +  str(number1 % number2))
else:
    print('Invalid Operator')