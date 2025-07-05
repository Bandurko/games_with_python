# This is game "guess the number"

import random


guessesTaken = 0

myName = input('Привет! Как вас зовут?\n')

number = random.randint(0, 100)

print(myName + ', угадай число лт 1 до 100 за 6 попыток')

for guessesTaken in range(6):
    # print('Попытка №' + (guessesTaken + 1))
    guess = int(input('Попытка №' + str(guessesTaken + 1) + '\n'))

    if guess < number:
        print('Твое число меньше загаданного')

    if guess > number:
        print('Твое число больше загаданного')

    if guess == number:
        break

if guess == number:
    # guessesTaken = str(guessesTaken + 1)
    print('Отлично, ' + myName + '! Ты угадал с ' + str(guessesTaken + 1) + ' попытки!')

if guess != number:
    # number = str(number)
    print('Увы. Загаданное число ' + str(number) + '.')