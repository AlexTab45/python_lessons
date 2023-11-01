white_score=int(input("Введите свой счет белых\n"))
black_score=int(input("Введите свой счет черных\n"))
white_score_end=white_score+6.5
black_score_end=black_score
print("После добавления 6.5 балл равен:")
print(f"Белый - {white_score_end}\nЧepный - {black_score_end}")
if white_score_end>black_score_end:
    print("Белые - победили!!!")
elif white_score_end<black_score_end:
    print("Черные - победили!!!")
else:
    print("Ничья.")