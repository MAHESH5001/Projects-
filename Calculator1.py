def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation =input(''' 
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ''')

    if operation == '+':
        print('{} + {} = '.format(num1, num2))
        print(num1 + num2)

    elif operation == '-':
        print('{} - {} = '.format(num1, num2))
        print(num1 - num2)

    elif operation == '*':
        print('{} * {} = '.format(num1, num2))
        print(num1 * num2)

    elif operation == '/':
        if num2 != 0:
            print('{} / {} = '.format(num1, num2))
            print(num1 / num2)
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print('You have not typed a valid operator, please run the program again.')

def again():
    calc_again = input(''' 
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''')

    if calc_again.upper() == 'Y':
        calculator()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculator()