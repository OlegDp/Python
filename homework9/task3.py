import random

random_dictionary = {str(i) : (i ** 3) for i in range(1, 11)}
print("Значення ключів у словнику є числа ключів, зведені в куб:")
print(random_dictionary)