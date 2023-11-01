def get_user_info():
    name = input("Как тебя зовут?")
    age = int(input("Сколько тебе полных лет?"))
    print("Твоё имя -" + name + ";" + "Твой возраст -" + str(age) + "года/лет")
    return [name, age]

print("Привет дружище!\nДавай познакомимся.\nРасскажи о себе.")
name, age=get_user_info()
#меняем местами#
name, age=age, name
print(name, age)