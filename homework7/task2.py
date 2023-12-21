x = None

while not x:
    
    try:
        x = int(input("Введіть число: "))   
        for i in range(0, x):
            print(f"{i:>4}", f"{('1' + ('0' * i)):>{x}}")
        
    except ValueError:
        print("Будь ласка, введіть ціле число.")
