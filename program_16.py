#ввести длину кирпича, см и добавить 1 см к длине каждого кирпича; длину стены, м
import math
brick_len=int(input("Введите длину кирпича в см \n"))+1
wall_len=float(input("Введите длину стены в м \n"))
#рассчитываем количество кирпичей
num_bricks=wall_len/(brick_len/100)
print(f"{math.floor(num_bricks)} кирпичей строится один ряд стены")
#вывести на печать остаток стены, незаполненный кирпичами
left_over=(wall_len*100)-(math.floor(num_bricks)*brick_len)
print(f"Это на {left_over} см меньше требуемой длины стены")