import math
area=int(input("Введите площадь в кв. м \n"))
pot_area=int(input("Введите площадь в кв. м, на которую хватит 1-й банки\n"))
num_pot=math.ceil(area/pot_area)
print(f"Вам понадобится {num_pot} баночек c краской.")
end_area=num_pot*pot_area-area
print(f"Оставшейся краской можно покрасить {end_area} м2.")