speed=int(input("Please enter the test speed (mph)\n"))
distance=round(float(input("Please enter the tested braking distance (m)\n")))
if (speed <= 30) and (distance <=14):
    print("Your car has passed the braking distance check.")
elif (speed <= 50) and (distance <=38):
    print("Your car has passed the braking distance check.")
else:
    print("Your car has not passed the braking distance check.")