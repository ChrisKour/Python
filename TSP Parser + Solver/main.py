import time
import numpy as np
import os.path
import sys
from swap import swap
from nearest import nearest
from read import read

filename = input("Enter a file name: ")  # o xrhsths dinei to onoma tou arxeiou(prepei na einai sto idio directory)
if not (os.path.isfile("./"+filename+".tsp")):          # An den yparxei stamataei to programma
    print("There is no such file.")
    sys.exit(1)
lines_list = open(filename+".tsp").read().splitlines()  # Diabasma arxeiou

start_time = time.time()                                # Wra ekkinhshs

nodes, dimension = read(lines_list)               # Diabasma dedomenwn
first_solution, first_distances, distances = nearest(nodes, dimension)  # Euresh prwths lyshs nearest neighbor

fs = np.array(first_solution) + 1                    # Pros8esh 1 gia na paroume ton ari8mo kombou opws sto arxeio
print("Nearest Neighbor:")
print("First Solution:", fs.tolist())    # Ektypwsh apotelesmatwn
print("First Distance:", np.sum(np.array(first_distances)))

# Tabu search me swap
best_solution, best_distances = swap(dimension, first_solution, first_distances, distances, start_time)

bs = np.array(best_solution) + 1                     # Pros8esh 1 gia na paroume ton ari8mo kombou opws sto arxeio
print("Tabu search (swap):")
print("Best Solution:", bs.tolist())                    # Ektypwsh apotelesmatwn
print("Best Distance:", np.sum(np.array(best_distances)))

