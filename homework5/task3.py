n = 1
lst = []
number = None
while not number:
    try:
        number = int(input("Введіть число: "))

        while n < number:
            if n % 2 != 0:
                lst.append(n)
                n += 2
        print(lst[::-1], end = ' ')

    except:
        print('Треба було вводити число')
        number=None