from random import randint
number=randint(1,100)
print('Угадайте число от 1 до 100')
while True:
    x=int(input('Введите число: '))
    if x<number:
         print('Ваше число меньше того, что загадано.')
    elif x>number:
         print('Ваше число больше того, что загадано.')
    elif x==number:
         break
print('Отличная интуиция! Вы угадали число :)')