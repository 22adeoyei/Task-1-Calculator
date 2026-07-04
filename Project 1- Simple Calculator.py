print('Hello! I am your Personal Calculator! Give me any two numbers and what you would like to do with them.')
# ======== Calculator =========
# 1. Add
# 2. Subtract
# 3. Divide
# 4 Multiply
# 5. Exit

while True:
    x = int(input('Your First Number Is :  '))
    y = int(input('Your Second Number Is:  '))
    Command = input('Now pick a Command : Add, Subtract, Divide or Multiply?')
    if Command == '1': 
        print(f'Your Number Is: {x + y}!')  
    if Command == '2':
        print(f'Your Number Is: {x - y}!')
    if Command == '3':
        if y == '0':
            print("You can't Divide by zero Silly!")
        else:
            print(f'Your Number Is: {x / y}!')
    if Command == '4':
        print(f'Your Number Is: {x * y}!')
    if Command =='5':
            print('Thanks for using my calculator!')
            break
    again = input('Would you like another calculation? (yes/no): ').lower()
    if again == 'no':
        print('Thanks for using my calculator!')
        break