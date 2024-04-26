from random import randint as rnd


def guess_number():
    number = rnd(1, 100)
    user_number = 0
    while user_number != number:
        user_number = int(input('Введите целое число от 1 до 100: '))
        if user_number == number:
            print('Отличная интуиция! Вы угадали число :)')
        elif user_number > number:
            print('Ваше число больше того, что загадано')
        else:
            print('Ваше число меньше того, что загадано')


guess_number()
