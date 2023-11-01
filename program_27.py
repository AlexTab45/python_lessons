frend_1=int(input("Какую сумму собрал первый друг - \n"))
frend_2=int(input("Какую сумму собрал второй друг - \n"))
frend_3=int(input("Какую сумму собрал третий друг - \n"))
total=frend_1+frend_2+frend_3
if total<1000:
    print(f"Вы набрали менее 1000$ {total+100}")
if (total>=1000) and (total<=2000):
    print(f"Вы набрали от 1000 до 2000$ {total*2}")
if total>2000:
    print(f"Вы набрали более 2000$ {total+2000}")