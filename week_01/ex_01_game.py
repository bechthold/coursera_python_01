import random

number = random.randint(0, 101)

while True:
    answer = input('Введите число: ')
    if not answer or answer == 'exit':
        break
    
    if not answer.isdigit():
        print('Введите правильное число!')
        continue
    
    user_answer = int(answer)
    
    if number > user_answer:
        print('Загаданное число больше')
    elif number < user_answer:
        print('Загаденное число меньше')
    else:
        print('Вы угадали верно!')
        break
        
    