inpu = 'Любіть Україну, як сонце, любіть, як вітер, і трави, і води… В годину щасливу і в радості мить, любіть у годину негоди. Любіть Україну у сні й наяву, вишневу свою Україну, красу її, вічно живу і нову, і мову її солов’їну. Між братніх народів, мов садом рясним, сіяє вона над віками… Любіть Україну всім серцем своїм і всіми своїми ділами. Для нас вона в світі єдина, одна в просторів солодкому чарі… Вона у зірках, і у вербах вона, і в кожному серця ударі, у квітці, в пташині, в електровогнях, у пісні у кожній, у думі, в дитячий усмішці, в дівочих очах і в стягів багряному шумі…'

# змінюємо регістр та прибираємо розділові знаки
new_inpu = inpu.lower().replace(",", "").replace(".", "").replace("…", "")
print(inpu)

# розбиваємо рядок на об'єкт список
x = new_inpu.split()
my_dict = {}

# рахуємо кількість повторень в словнику
for i in x:
    my_dict[i] = my_dict.get(i, 0) + 1
print(my_dict)
print()
y = 0
l = 1
maximum = None
minimum = None
for j in my_dict:
    if my_dict[j] > y:
        y = my_dict[j]
        maximum = y
for i in my_dict:
    if my_dict[i] == maximum:
        print(i, "зустрічається в тексті", maximum, "разів")
print()
my_s = ' '
for k in my_dict:
    if my_dict[k] <= l:
        l = my_dict[k]
        minimum = l
for s in my_dict:
    if my_dict[s] == minimum:
        my_s = str(my_s) + str(s) + ', ' 
        
print(my_s, "зустрічається в тексті", minimum, "раз")