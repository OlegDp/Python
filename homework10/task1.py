import random

def ekvivalent(spisok, number):
    '''Функція перевіряє чи є у списку/послідовності 2 числа, сума яких еквівалентна 
    числу переданому 2-гим параметром та повертає булеве значення як результат пошуку фукції.'''
    for i in range(len(spisok)):
        for j in range(i + 1, len(spisok)):
            if spisok[i] + spisok[j] == number:
                return True
    return False

# перевірка через рандомний список і рандомне значення
spisok1 = []
for k in range(7):
    spisok1 += [random.randint(1, 10)]
number1 = random.randint(1, 20)
result1 = ekvivalent(spisok1, number1)
print("Для послідовності", spisok1, "перевірка еквівалентності сум чисел другому параметру - ", number1, ", має результат:", result1)

# перевірка через заданий список
spisok2 = [10, 6, 7, 8]
number2 = 17
result2 = ekvivalent(spisok2, number2)
print("Для послідовності", spisok2, "перевірка еквівалентності сум чисел другому параметру - ", number2, ", має результат:", result2)