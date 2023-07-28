'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPT_LIMIT = 10

target_num = randint(LOWER_LIMIT, UPPER_LIMIT)  #число, которое необходимо угадать
print(f"\nЗагадано целое число в диапазоне от {LOWER_LIMIT} до {UPPER_LIMIT}. Угадайте его за {ATTEMPT_LIMIT} попыток.")

for attemt in range(ATTEMPT_LIMIT):
    answer_num = int(input("\nВведите предполагаемое число: "))

    if answer_num > target_num:
        print(f"\nЗагаданное число МЕНЬШЕ указанного. Попыток осталось: {ATTEMPT_LIMIT - (attemt + 1)}")
    elif answer_num < target_num:
        print(f"\nЗагаданное число БОЛЬШЕ указанного. Попыток осталось: {ATTEMPT_LIMIT - (attemt + 1)}")
    else:
        print(f"\nПоздравляем!!! Число угаданно с {attemt + 1} попыток.")
        break


if (attemt + 1) == ATTEMPT_LIMIT and answer_num != target_num:
    print(f"Вы не угадали число... Попытки закончились. Загаданное число было: {target_num}")