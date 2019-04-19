from random import randint
import os.path


def new_uneven_test():
    file_id = 1
    file_path = "tests_uneven/input" + str(file_id) + ".txt"
    while(os.path.isfile(file_path)):
        file_id += 1
        file_path = "tests_uneven/input" + str(file_id) + ".txt"
    f_path = open(file_path, "w")
    kol_points = randint(7, 10)
    time = []
    time.append(0)
    l = 1
    r = 3
    for i in range(kol_points):
        w = randint(l, r)
        time.append(w)
        l = w + 1
        r = l + 2
    distance = []
    l = 0
    r = 100
    distance.append(randint(0, 100))
    for i in range(kol_points):
        w = randint(l, r)
        while abs(w - distance[-1]) > 30:
            w = randint(l, r)
        distance.append(w)
    for i in range(len(time)):
        f_path.write(str(time[i]) + ',' + str(distance[i]) + '\n')
    f_path.close()


for i in range(10):
    new_uneven_test()
