x = None

while not x:
    
    try:
        x = int(input("Введіть число: "))
        if 3 <= x <= 9:
            counter = 1
            string = ' '
            for i in range(1, x + 1):
                print(string + str(counter) + string[::-1])
                string = string + str(counter)
                counter += 1
        else:
            print("Треба було вводити число від 3 до 9 ")
            x = None
    except ValueError:
        print("Будь ласка, введіть ціле число.")