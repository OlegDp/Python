def password_decorator(func):
    def wrapper():
        while True:
            print("Вимоги до паролю: мінімум 8 символів, принаймні 1 буква, 1 цифра, 1 спеціальний символ.")
            password = func()

            if not password or any(x.isspace() for x in password):
                print("Не приймаються пробільні символи і символи табуляції до паролю.")
            else:
            
                if (
                    len(password) >= 8
                    and any(x.isdigit() for x in password)
                    and any(x.isalpha() for x in password)
                    and any(not x.isalnum() for x in password)
                    and any(not x.isspace() for x in password)
                ):
                    print("Пароль відповідає вимогам.")
                    return password
                else:
                    print("Пароль не відповідає вимогам. Спробуйте ще раз.")
    
    return wrapper

@password_decorator
def get_password():
    password = input("Введіть пароль: ")
    return password

if __name__ == "__main__":
    result = get_password()
    print("Ваш пароль:", result)