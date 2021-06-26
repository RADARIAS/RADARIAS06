user_seconds = int(input('Введите время в секундах:\n'))

if user_seconds >= 3600:
    hour = user_seconds // 3600
    minutes = (user_seconds % 3600) // 60
    user_seconds %= 60
else:
    hour = 0
    minutes = user_seconds // 60
    user_seconds %= 60
print(f'Расчетное время: {hour:02d}:{minutes:02d}:{user_seconds:02d}')