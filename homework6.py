result_first = int(input('Ввведите результат первого дня:\n'))
result_max = int(input('Ввведите желаемый результат:\n'))
day = 1
if result_first > result_max:
    print(f'Вы ввели неверные данные, результат первой тренировки {result_first} '
          f'больше целевого результата {result_max}!!! ')
else:
    while result_first < result_max:
        day += 1
        result_first += result_first / 100 * 10
        print(f'{result_first:.2f}км:', day, 'день')
    print(f'Результат {result_max}км будет достигнут на {day} день!')