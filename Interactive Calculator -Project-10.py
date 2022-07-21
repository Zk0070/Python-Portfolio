print('Welcome to the interactive calculator program developed by Zabi Khan!!')
print('*************************************************')
print('''
/ ,-----------------. \
| |    1.05459 e -34| |
| `-----------------' |
| [@ ] On/Off  ###### |
|              ###### |
| [7] [8] [9] [C] [AC]|
|                     |
| [4] [5] [6] [X] [%] |
|                     |
| [1] [2] [3] [+] [-] |
|                     |
| [0] [.]  [EXP]  [=] |
\_____________________/''')
print('*************************************************')

def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def mul(num1,num2):
    return num1 * num2
def div(num1,num2):
    return num1 / num2
def mod(num1,num2):
    return num1%num2
operations={
    '+':add,
    '-':sub,
    '*':mul,
    '/':div,
    '%':mod,
}

def calculator():
    end_calc=False
    num1=float(input('Enter a number for operation to be performed: '))
    for symbol in operations:
        print(symbol)
    while not end_calc:
        operation=input('Enter the operation to be performed: ')
        num2=int(input('Enter the second number for operation to be performed: '))
        calculator_func=(operations[operation])
        answer=calculator_func(num1,num2)
        print(f'{num1}{operation}{num2} is {answer}')
        print('Thank you for using the calculator!!')
        furthercal=input(f'Do you want to continue with the operation with {answer} yes or no: ')
        num1=answer
        if furthercal=='no':
            end_calc=False
            calculator()

calculator()

