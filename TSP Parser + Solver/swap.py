import math
import time
import numpy as np


def swap(dimension, first_solution, first_distances, distances, start_time):  # Tabu search me swap
    memory = np.zeros([dimension, dimension])           # Etoimase ton pinaka mnhmhs

    memory_num = round(math.sqrt(dimension))     # o ari8mos gyrwn pou den 8a ksanasymmetasxei ena swap

    # Swap
    best_solution = first_solution[:]       # Edw kratame thn synolika kalyterh lysh
    current_solution = first_solution[:]    # H lysh sthn opoia ginontai ta dokimastika swap
    solution = first_solution[:]            # H lysh sthn opoia 8a kanei reset gia ka8e synolikh epanalipsh to swap
    least_worse_solution = []               # H ligotero kakh lysh se ka8e epanalhpsh toy swap

    best_distances = first_distances[:]     # Oi kalyteres apostaseis
    current_distances = first_distances[:]
    solution_distances = first_distances[:]
    least_worse_distances = []
    best_total_distance = np.sum(np.array(first_distances))

    better = False                          # Elegxos an gia mia epanalhpsh eixame kalyterh timh
    least_worse = 1000000

    while time.time() - start_time < 60:    # Orio xronou 1 lepto
        for i in range(dimension):
            for j in range(dimension):
                if j > i:        # Den kanoume swap thn idia 8esh kai den kanoume diploelegxous
                    current_solution[i], current_solution[j] = current_solution[j], current_solution[i]     # swap
                    # Enhmerwsh pinaka apostasewn
                    current_distances[i] = distances[current_solution[i]][current_solution[i+1]]
                    if i != 0:
                        current_distances[i-1] = distances[current_solution[i-1]][current_solution[i]]
                    else:
                        current_distances[-1] = distances[current_solution[-1]][current_solution[0]]
                    current_distances[j-1] = distances[current_solution[j - 1]][current_solution[j]]
                    if j == dimension - 1:
                        current_distances[j] = distances[current_solution[j]][current_solution[0]]
                    else:
                        current_distances[j] = distances[current_solution[j]][current_solution[j+1]]
                    temp = np.sum(np.array(current_distances))
                    if temp < best_total_distance:    # An exoume kalyterh apostash (mikroterh)
                        best_total_distance = temp
                        best_solution = current_solution[:]         # Kai thn antistoixh diadromh
                        best_distances = current_distances[:]
                        better = True                               # Breikame sthn epanalhpsh kalyterh lysh
                        mem_i = i
                        mem_j = j
                    else:                                           # An exoume xeiroterh diadromh
                        if temp < least_worse and memory[i][j] == 0:  # Bres ayth poy den einai toso kakh kai den exei xrhsimopoih8ei teleutaia
                            least_worse = temp  # Apo8hkeuse thn apostash gia sygkrinontai oi epomenes
                            least_worse_solution = current_solution[:]   # Pare th lysh
                            least_worse_distances = current_distances[:]
                            mem_i = i
                            mem_j = j
                current_solution = solution[:]      # arxikopoihsh ths current solution
                current_distances = solution_distances[:]
        least_worse = 1000000
        if better:                                  # An exoume kalyterh lysh sthn epanalhpsh
            current_solution = best_solution[:]     # Thn bazoume san default sthn epomenh
            solution = best_solution[:]
            current_distances = best_distances[:]
            solution_distances = best_distances[:]
        else:                                       # An den brhkame kalyterh lysh
            current_solution = least_worse_solution[:]  # Bazoume thn kainourgia lysh san default sthn epomenh
            solution = least_worse_solution[:]
            current_distances = least_worse_distances[:]
            solution_distances = least_worse_distances[:]
        better = False
        for a in range(dimension):                  # Meiwnoyme tous ari8mous sta swap pou xrhsimopoih8hkan
            for b in range(dimension):
                if memory[a][b] > 0:
                    memory[a][b] -= 1
        memory[mem_i][mem_j] = memory_num            # To telutaio swap mpainei sthn tabulist
    return best_solution, best_distances
