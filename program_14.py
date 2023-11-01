import math
volume=float(input("Пожалуйста, введите объем банки (cм3):\n"))
candy_volume=float(input("Пожалуйста, введите объем одной конфеты (см3):\n"))
num_candy=volume/candy_volume
print(f"В банке {math.floor(num_candy)} конфет.")