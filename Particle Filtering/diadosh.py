import random


def diadosh(t0):
    diadosh_list = [0, 0, 0, 0, 0, 0]

    for i in range(t0[0]):  # le
        temp = random.random()
        if temp < 0.7:  # Apo LE -> LE einai 0.7%
            diadosh_list[0] += 1
        else:  # Apo LE -> LW einai 0.3%
            diadosh_list[1] += 1

    for i in range(t0[1]):  # lw
        temp = random.random()
        if temp < 0.15:  # Apo lw -> le einai 0.15%
            diadosh_list[0] += 1
        elif temp < 0.5:  # Apo lw -> lw einai 0.35%
            diadosh_list[1] += 1
        elif temp < 0.65:  # Apo lw -> ce einai 0.15%
            diadosh_list[2] += 1
        else:  # Apo lw -> cw einai 0.35%
            diadosh_list[3] += 1

    for i in range(t0[2]):  # ce
        temp = random.random()
        if temp < 0.35:  # Apo ce -> le einai 0.35%
            diadosh_list[0] += 1
        elif temp < 0.5:  # Apo ce -> lw einai 0.15%
            diadosh_list[1] += 1
        elif temp < 0.85:  # Apo ce -> ce einai 0.35%
            diadosh_list[2] += 1
        else:  # Apo ce -> cw einai 0.15%
            diadosh_list[3] += 1

    for i in range(t0[3]):  # cw
        temp = random.random()
        if temp < 0.15:  # Apo cw -> ce einai 0.15%
            diadosh_list[2] += 1
        elif temp < 0.5:  # Apo cw -> cw einai 0.35%
            diadosh_list[3] += 1
        elif temp < 0.65:  # Apo cw -> re einai 0.15%
            diadosh_list[4] += 1
        else:  # Apo cw -> rw einai 0.35%
            diadosh_list[5] += 1

    for i in range(t0[4]):  # re
        temp = random.random()
        if temp < 0.35:  # Apo re -> ce einai 0.35%
            diadosh_list[2] += 1
        elif temp < 0.5:  # Apo re -> cw einai 0.15%
            diadosh_list[3] += 1
        elif temp < 0.85:  # Apo re -> re einai 0.35%
            diadosh_list[4] += 1
        else:  # Apo re -> rw einai 0.15%
            diadosh_list[5] += 1

    for i in range(t0[5]):  # rw
        temp = random.random()
        if temp < 0.3:  # Apo rw -> re einai 0.3%
            diadosh_list[4] += 1
        else:  # Apo rw -> rw einai 0.7%
            diadosh_list[5] += 1

    return diadosh_list
