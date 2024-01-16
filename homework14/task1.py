import random
matrix = []
number = None

def bubble_sort_column(matrix, column_index):
    num_rows = len(matrix)
    for i in range(num_rows):
        for j in range(0, num_rows-i-1):
            if matrix[j][column_index] > matrix[j+1][column_index]:
                matrix[j][column_index], matrix[j+1][column_index] = matrix[j+1][column_index], matrix[j][column_index]

def bubble_sort_column2(matrix, column_index):
    num_rows = len(matrix)
    for i in range(num_rows):
        for j in range(0, num_rows-i-1):
            if matrix[j][column_index] < matrix[j+1][column_index]:
                matrix[j][column_index], matrix[j+1][column_index] = matrix[j+1][column_index], matrix[j][column_index]

def bubble_sort_all_columns(matrix):
    num_columns = len(matrix[0]) if len(matrix) > 0 else 0
    for col in range(num_columns):
        if col % 2 != 0:
            bubble_sort_column(matrix, col)
        else:
            bubble_sort_column2(matrix, col)

while not number:
    try:
        number = int(input("Введіть число M більше 5: "))
        if number > 5:
            print()
            for i in range(number):
                line = []
                for j in range(number):
                    if j < number:
                        line.append(random.randint(1, 50))
                matrix.append(line)
           
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    print(matrix[i][j], end = '\t')
                print()
            
            #сортування
            bubble_sort_all_columns(matrix)

            print("\nМатриця після сортування:")
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    print(matrix[i][j], end = '\t')
                print()
            print()

            #підрахунок суми в колонках та виведення з рядком сум
            num_columns = len(matrix[0]) if len(matrix) > 0 else 0
            sums_per_column = [0] * num_columns
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    sums_per_column[j] += matrix[i][j]
            
            line1 = []
            for j in range(num_columns):
                line1.append(sums_per_column[j])
            
            matrix.append(line1)
            
            print("\nМатриця після підрахування:")
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    print(matrix[i][j], end = '\t')
                print()
            print()

        else:
            print('Треба було вводити числа більше 5')
            number=None
    except:
        print('Треба було вводити число')
        number=None    
