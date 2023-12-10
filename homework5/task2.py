matrix = []

for i in range(5):
    line = [0, 0, 0, 0, 0]
    matrix.append(line)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            matrix[i][j] = 10 + i

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (len(matrix) - 1) - i == j:
            matrix[i][j] = 14 - j
        print(matrix[i][j], end = ' ')
    print()
 

            
