if __name__ == '__main__':
    result_gipotenuza = lambda x, y = 4: ((x ** 2) + (y ** 2)) ** 0.5

    k = result_gipotenuza(3, )
    print("Значення гіпотенузи при x = 3: ", k)

    n = map(lambda x, y = 4: ((x ** 2) + (y ** 2)) ** 0.5, [1,2,3])
    print("Один список/послідовність чисел для обробки у map: ", list(n))

    j = map(lambda x, y = 4: ((x ** 2) + (y ** 2)) ** 0.5, [1,4,7], [4,3,8])
    print("2 списки/послідовності чисел для обробки у map: ", list(j))