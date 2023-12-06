N = input("Введіть будь-яке число: ")
my_lst = list(N)
for i in range(0, len(N)):
    if (my_lst.count(my_lst[i]) >= 2):
        print("Yes")
        break
    elif i == (len(N) -1):
        print("No")