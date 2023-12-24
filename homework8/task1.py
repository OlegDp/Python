import random

line = []
for i in range(1, 16):
    i = random.randint(1,100)
    line += [i]
print(line)

x = 0
y = 0
for k in line:
    if k % 2 == 0:
        x += k
    else:
        y += k
# print("Сума парних: ", x) 
# print("Сума не парних: ", y)
if y > x:
    print("Yes")
else:
    print("No")