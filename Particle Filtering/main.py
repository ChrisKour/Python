import random
from diadosh import diadosh
from anadeigmatolhpsia import anadeigmatolhpsia
from eksomalynsh import eksomalynsh

iterations = 1000000

# le = 0, lw = 1, ce = 2, cw = 3, re = 4, rw = 5
t0 = [0, 0, 0, 0, 0, 0]

# t = 0
for i in range(iterations):     # Arxikh katanomh 33% stis 8eseis me anemo E
    temp = random.random()
    if temp < 1/3:      # le
        t0[0] += 1
    elif temp < 2/3:    # ce
        t0[2] += 1
    else:               # re
        t0[4] += 1

for j in range(3):
    list = diadosh(t0)
    list2 = anadeigmatolhpsia(list, iterations, j)
    if j == 1:
        eksomalynsh(list2, iterations)
    if j == 2:
        print("P(X3|e1:3) = <", list2[0]+list2[1], "", list2[2]+list2[3], "", list2[4]+list2[5], ">")
        print("P(A3|e1:3) = <", list2[0]+list2[2]+list2[4], "", list2[1]+list2[3]+list2[5], ">")
    t0 = list2[:]

list = diadosh(t0)
print("P(X4|e1:3) = <", list[0]+list[1], "", list[2]+list[3], "", list[4]+list[5], ">")
print("P(A4|e1:3) = <", list[0]+list[2]+list[4], "", list[1]+list[3]+list[5], ">")
