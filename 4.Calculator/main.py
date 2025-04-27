# Function to display the menu
def show_menu():
    print('Welcome to simple calculator')
    print('The following operations are available')
    print('1. Addition(+)')
    print('2. Substraction(-)')
    print('3. Multiplication(*)')
    print('4. Division(/)')
    print('5. Exponentiation(**)')
   
# Function to get the numbers
def get_numbers():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    return num1,num2

# Function to perform calculation
def calculate(num1,num2,operation):
    if operation == '+':
        return num1+num2
    elif operation == '-':
        return num1-num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        if num2!=0:
            return num1/num2
        else:
             return 'Cannot divide by zero'

    elif operation == '**':
        return num1**num2       
    else:
        return 'Invalid operation'
# Driver function
def main():
    while True:
        show_menu()
        num1,num2 = get_numbers()
        operator = input('Enter operator(+,-,*,/,**)')
        result = calculate(num1,num2,operator)
        print(f'result: {round(result,2)}')
        again = input('Do you want to perform another operation? (Y/N)').upper()
        if again != 'Y':
            print('THanks for using calculator!')
            break
if __name__ == "__main__":
    main()

    