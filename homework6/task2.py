import random
matrix = []
number = None

while not number:
    try:
        number = int(input("Введіть число N більше 5: "))
        number2 = int(input("Введіть число M більше 5: "))
        if number > 5 and number2 > 5:
            print()
            for i in range(number):
                line = []
                for j in range(number2):
                    if j < number2:
                        line.append(random.randint(1, 100))
                matrix.append(line)

            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    print(matrix[i][j], end = ' ')
                print()

            print()
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    print(matrix[i][j], end = '\t')
                print()
            
            print()
            for i in range(len(matrix)):
                matrix[i][-2], matrix[i][-1] = matrix[i][-1], matrix[i][-2]
                for j in range(len(matrix[i])):
                    print(matrix[i][j], end = '\t')
                print()
        else:
            print('Треба було вводити числа більше 5')
            number=None
    except:
        print('Треба було вводити число')
        number=None    