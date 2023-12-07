sum_numbers = 0
count_numbers = 0
max_number = 0
min_number = None
even_count = 0
odd_count = 0

number = input("Введіть ціле число (введіть 0 для завершення): ")

while number != "0":
    try:
        number = int(number)

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if number == 0:
            break

        sum_numbers += number
        count_numbers += 1

        if number > max_number:
            max_number = number
        
        if min_number is None or number < min_number:
            min_number = number
           

    except :
        print("Будь ласка, введіть коректне ціле число.")

    number = input("Введіть ціле число (введіть 0 для завершення): ")

if count_numbers > 0:
    average = sum_numbers / count_numbers
    print("Сума чисел:", sum_numbers)
    print("Середнє арифметичне:", average)
    print("Максимальне значення:", max_number)
    print("Мінімальне значення:", min_number)
    print("Кількість парних чисел:", even_count)
    print("Кількість непарних чисел:", odd_count)
else:
    print("Не введено жодного числа.")