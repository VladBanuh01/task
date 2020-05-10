print('Hello Rabotnik!!')

n_one = ""
n_two = ""

while n_one == "" or n_two == "":
    try:
        n_one = int(input("Введите первое положительное число: "))
        if n_one < 0:
            raise ValueError("ValueError exception thrown")

        n_two = int(input("Введите второе положительное число: "))
        if n_two < 0:
            raise ValueError("ValueError exception thrown")

        # Addition and subtraction
        print(f"Результат сложения = {n_one+n_two}")
        print(f"Результат вычитания = {n_one-n_two}") 


