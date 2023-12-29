import random

def rand_matrix(number = 2, number2 = 2):
    """функція приймає 2 параметри і генерує 2-вимірний список заповнений 
    випадковими цілими значенням в диапазлні 0 - 200 """
    matrix = []
    for i in range(number):
        line = []
        for j in range(number2):
            if j < number2:
                line.append(random.randint(0, 200))
        matrix.append(line)
    return matrix

def matrix_simetric(matrix):
    """функція відображає матрицю, створену в першій функції, у форматі таблички (у якої колонки не роз'їжаються) """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = '\t')
        print()

if __name__ == '__main__':
    m = rand_matrix()
    k = rand_matrix(3,)
    l = rand_matrix(4,3)
    print("Результат роботи першої функції: ", m)
    print()
    print("2-вимірний симетричний список, коли перша функція не отримує параметри:")
    matrix_simetric(m)
    print()
    print("2-вимірний симетричний список, коли перша функція отримує 1 параметр :")
    matrix_simetric(k)
    print()
    print("2-вимірний симетричний список, коли перша функція отримує 2 параметри :")
    matrix_simetric(l)