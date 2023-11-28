#!/usr/bin/python3
for i in range(10):
    for j in range(1, 10):
        if i == 0:
            print("{:02d}".format(j))
            continue
        if i == j:
            continue
        comb1 = int(str(i) + str(j))
        comb2 = int(str(j) + str(i))
        if comb1 < comb2:
            print("{}".format(comb1), end=", " if i < 10 and j < 10 else '\n')
        else:
            print("{}".format(comb2), end=", " if i < 10 and j < 10 else '\n')
