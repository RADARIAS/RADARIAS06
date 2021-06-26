a = int(input("введите несколько цифр без пробела:\n"))
a_max = a % 10
a = a // 10
while a > 0:
    if a % 10 > a_max:
        a_max = a % 10
    a = a // 10
print(a_max)