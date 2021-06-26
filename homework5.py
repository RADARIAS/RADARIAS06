revenue = float(input('Ввведите сумму выручки:\n'))
costs = float(input('Ввведите сумму издержек:\n'))
profit = revenue - costs
if profit > 0:
    number_people = int(input('Отлично!!! В этот раз мы в плюсе!!!\n'
                              'Ввведите численнось сотрудников фирмы:\n'))
    profitability = profit / revenue
    profit_pers = profit / number_people
    print(f'Фирма работает эффективно!!! Прибыль составила {profit:.2f} руб;\n'
          f'Коэффициент рентабельности: {profitability:.2f};\n'
          f'Персональная прибыль на сотрудника: {profit_pers:.2f} руб')
elif not profit:
    print('В этот раз ваша фирма не заработала ни копейки!!!')
else:
    print(f'В этот раз фирма потерпела убыток в размере {profit * (-1)} руб. ')