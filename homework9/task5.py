input = 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'

my_dict = {}

for i in input:
    my_dict[i] = my_dict.get(i, 0) + 1

print(my_dict)