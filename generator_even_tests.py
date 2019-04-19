from random import randint
import os.path

def new_even_test():
    kol_points = randint(7, 10)
    time = []
    time.append(0)
    delt_time = randint(1, 5)
    delt_distance = randint(-7, 7)
    first_koord = randint(1, 100)
    while (first_koord + kol_points * delt_distance < 0):
        delt_diatance = randint(-7, 7)
    for i in range(kol_points):
        time.append(time[-1] + delt_time)
    distance = []
    distance.append(first_koord)
    for i in range(kol_points):
        distance.append(distance[-1] + delt_distance)
    file_id = 1
    file_path = "tests_even/input" + str(file_id) + ".txt"
    while(os.path.exists(file_path)):
        file_id += 1
        file_path = "tests_even/input" + str(file_id) + ".txt"
    f_path = open(file_path, "w")
    for i in range(len(time)):
        f_path.write(str(time[i]) + ',' + str(distance[i]) + '\n')
    f_path.close()
    
    
for i in range(10):
    new_even_test()
