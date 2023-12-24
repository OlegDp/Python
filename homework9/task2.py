import random

random_dictionary = {str(i) : random.randint(1, 5) for i in range(1, 21)}

print("Згенерований словник:")
print(random_dictionary)

result = 1
for value in random_dictionary.values():
    result *= value

print("Результат множення значень ключів: ", result)