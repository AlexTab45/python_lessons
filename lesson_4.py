num_glases=int(input("Сколько стаканов было продано\n"))
price=int(input("Стоимость 1 стакана\n"))
total_sales=num_glases*price
if total_sales>25:
    print("Стоимость доставки 1.5 $")
else:
    print("Стоимость доставки 4 $")