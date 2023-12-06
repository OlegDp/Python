N = int(
    input("Введіть число N: ")
)

n = 1
while n < N:
    y = n ** 2

    if y > N:
        break

    print(y, end = " ")
    n += 1