import random
matrix = []
number = None
my_x = 0
my_y = 0
while not number:
    try:
        number = int(input("Введіть число більше 0: "))
        
        for i in range(number):
            line = []
            for j in range(number):
                if j < number:
                    line.append(random.randint(10, 99))
            matrix.append(line)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print(matrix[i][j], end = ' ')
            print()

        for i in range(len(matrix)):
            my_x += matrix[i][i]
        print("Cума діагоналі двомірного списку з ліва на право з гори у низ: ", my_x)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (len(matrix) - 1) - i == j:
                    my_y += matrix[i][j]
        print("Cума діагоналі двомірного списку з права на ліво з гори у низ: ", my_y)

        if len(matrix) % 2 != 0:
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if (len(matrix) - 1) / 2 == j and i == j:
                        print("Число, яке знаходиться в центрі перетину діагоналей: ", matrix[i][j])
        else:
            print("Не можна обрахувати в зв'язку з тим, що введене число є парним (двувимірний список є парним N*N)")

    except:
        print('Треба було вводити число')
        number=None