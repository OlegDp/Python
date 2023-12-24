import random
x = 1
o = [ ]
y = [ ]
counter = 1
string = [ ]
print("Перший список: ")
for j in range(1, 11):
    x = string + [counter]
    counter += 1
    o += x
print(o)

print("Другий список: ")
for i in range(1, 11):
    x = string + [counter]
    counter += 2
    y += x
print(y)

print("Елементи першого списку ключі, а елементи другого значення нашого словника:")
result = dict(zip(o, y))
print(result)