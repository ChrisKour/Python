import random


def anadeigmatolhpsia(diadosh, iterations, j):
    if j == 0:      # Thn prwth stigmh h kamera deixnei aristera (L)
        w1 = 0.7
        w2 = 0.3
        w3 = 0.1
    else:           # Tis epomenes deixnei deksia (R)
        w1 = 0.1
        w2 = 0.3
        w3 = 0.7

    p1 = diadosh[0] * w1
    p2 = diadosh[1] * w1
    p3 = diadosh[2] * w2
    p4 = diadosh[3] * w2
    p5 = diadosh[4] * w3
    p6 = diadosh[5] * w3

    weight = p1 + p2 + p3 + p4 + p5 + p6    # Briskoume to synoliko baros
    anadeigmatolhpsia = [0, 0, 0, 0, 0, 0]

    for i in range(iterations):             # Dhmiourgoyme ksana to deigma symfwna me ta barh
        temp = random.random()*weight
        if temp < p1:
            anadeigmatolhpsia[0] += 1
        elif temp < p1 + p2:
            anadeigmatolhpsia[1] += 1
        elif temp < p1 + p2 + p3:
            anadeigmatolhpsia[2] += 1
        elif temp < p1 + p2 + p3 + p4:
            anadeigmatolhpsia[3] += 1
        elif temp < p1 + p2 + p3 + p4 + p5:
            anadeigmatolhpsia[4] += 1
        else:
            anadeigmatolhpsia[5] += 1

    return anadeigmatolhpsia
