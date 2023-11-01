'''temperature=float(input("Enter temperature outside :"))
total=5
total+=temperature # +,/,-,* заменяет название переменной
temperature=float(input("Enter temperature outside :"))
total+=temperature
temperature=float(input("Enter temperature outside :"))
total+=temperature
temperature=float(input("Enter temperature outside :"))
total+=temperature
temperature=float(input("Enter temperature outside :"))
total+=temperature
print(total)'''

'''total=0
for t in range(5):
    temperature=float(input("Enter temperature outside :"))
    total+=temperature
print(total)'''

counter=0
total=0
while counter<5:
    temperature=float(input("Enter temperature outside :"))
    total+=temperature
    counter+=1
print(total)
