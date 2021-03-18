bilet = int(input('введите количество билетов:\n'))
age_lists = []
prise_bilet = []
for prise in range(1, bilet + 1):
     while True:
          age = int(input("Введите возраст посетителя:\n"))
          if 0 <= age <= 100:
               break
          else:
               print(f'Вами были введены неккорректные данные.\n Возраст посетителя - {age} Пожалуйста будьте внимательны!!!')
     if 18 <= age <= 25:
          prise = 990
     elif 0 <= age <= 18:
          prise = 0
     elif 25 <= age <= 100:
          prise = 1390
     age_lists.append(age)
     prise_bilet.append(prise)
     print(age_lists, prise_bilet)
for a, b in zip(age_lists, prise_bilet):
     print('Возраст посетителя:', a, 'Стоимость билета:', b)
if bilet < 3:
     print('СУММА ВАШЕГО ЗАКАЗА СОСТАВИТ:', sum(prise_bilet))
if bilet >= 3:
     print('СУММА ВАШЕГО ЗАКАЗА СО СКИДКОЙ 10% СОСТАВИТ:', sum(prise_bilet) * 0.9)
