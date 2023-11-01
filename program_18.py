num_par3=int(input("Сколько здесь лунок для пар 3\n"))
num_par4=int(input("Сколько здесь лунок для пар 4\n"))
num_par5=int(input("Сколько здесь лунок для пар 5\n"))
difficulty=int(input("Какова корректировка сложности курса?\n"))
total_tries=(num_par3*3+num_par4*4+num_par5*5)+difficulty
print(f"Количество попыток за игру составляет: {total_tries}")
