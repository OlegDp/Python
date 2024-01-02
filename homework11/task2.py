def formula(num):
    """Формула для підрахунку простих чисел"""
    return num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def generator(n, z):
    """Генератор послідовності простих чисел з заданого діапазону"""
    for num in range(n, z + 1):
        if formula(num):
            yield num

# Випадкові значення для n та z
import random
n = random.randint(1, 50)
z = random.randint(51, 100)

print("Прості числа у діапазоні від", n, "до", z, ": ", list(generator(n, z)))