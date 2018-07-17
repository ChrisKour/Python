import random


def eksomalynsh(list, iterations):
    # Ta pososta na deixnei h kamera sto swsto shmeio
    elr = 0.1    # Enw h kamera deixnei R na eimaste L
    ecr = 0.3    # Enw h kamera deixnei R na eimaste C
    err = 0.7    # Enw h kamera deixnei R na eimaste R

    plele = prwrw = 0.7     # Oles oi pia8anothtes metakinhshs
    plelw = prwre = 0.3
    plwle = plwce = pcelw = pcecw = pcwce = pcwre = precw = prerw = 0.15
    plwlw = plwcw = pcele = pcece = pcwcw = pcwrw = prece = prere = 0.35

    p1 = list[0] * (plele * elr + plelw * elr)  # Ypologismos olwn twn barwn
    p2 = list[1] * (plwle * elr + plwlw * elr + plwce * ecr + plwcw * ecr)
    p3 = list[2] * (pcele * elr + pcelw * elr + pcece * ecr + pcecw * ecr)
    p4 = list[3] * (pcwce * ecr + pcwcw * ecr + pcwre * err + pcwrw * err)
    p5 = list[4] * (prece * ecr + precw * ecr + prere * err + prerw * err)
    p6 = list[5] * (prwre * err + prwrw * err)

    weight = p1 + p2 + p3 + p4 + p5 + p6
    eksomalynsh = [0, 0, 0, 0, 0, 0]

    for i in range(iterations):     # Kanonikopoihsh
        temp = random.random()*weight
        if temp < p1:
            eksomalynsh[0] += 1
        elif temp < p1 + p2:
            eksomalynsh[1] += 1
        elif temp < p1 + p2 + p3:
            eksomalynsh[2] += 1
        elif temp < p1 + p2 + p3 + p4:
            eksomalynsh[3] += 1
        elif temp < p1 + p2 + p3 + p4 + p5:
            eksomalynsh[4] += 1
        else:
            eksomalynsh[5] += 1

    print("P(X2|e1:3) = <", eksomalynsh[0]+eksomalynsh[1], "", eksomalynsh[2]+eksomalynsh[3], "", eksomalynsh[4]+eksomalynsh[5], ">")
    print("P(A2|e1:3) = <", eksomalynsh[0]+eksomalynsh[2]+eksomalynsh[4], "", eksomalynsh[1]+eksomalynsh[3]+eksomalynsh[5], ">")