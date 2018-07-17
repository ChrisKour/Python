import numpy as np
import copy


def nearest(nodes, dimension):                      # Creating the first solution (nearest-neighbor heuristic)
    first_solution = [0]                            # H arxh ths lyshs einai h prwth polh
    first_distances = []                            # Pinakas me tis apostaseis twn polewn ths lyshs
    distances = np.zeros([dimension, dimension])    # Dhmiourgia pinaka me tis apostaseis olwn twn polewn

    for i in range(dimension):                      # Ton gemizoume (apostaseis apo ena simeio se ola ta alla)
        for j in range(dimension):
            distances[i][j] = round(np.linalg.norm(nodes[i] - nodes[j]))

    near = np.empty([dimension, dimension])         # Exoume topiko pinaka panw ston opoio 8a kanoume allages
    np.copyto(near, distances)

    while len(first_solution) < len(nodes):         # oso den exoume balei ola ta nodes sthn arxikh lysh
        # Bres thn elaxisth apostash, gia thn teleytaia polh ths lyshs gia osa stoixeia den einai 0
        minimum_distance = np.min(near[first_solution[-1]][np.nonzero(near[first_solution[-1]])])
        itemindex = np.nonzero(near[int(first_solution[-1])] == minimum_distance)  # index ths elaxisths apostashs
        while itemindex[0][0] in first_solution:    # Kane elegxo oti den einai shmeio pou yparxei hdh sth lysh
            near[int(first_solution[-1])][itemindex[0][0]] = 0  # An einai mhdenise ekeino to simeio
            minimum_distance = np.min(near[int(first_solution[-1])][np.nonzero(near[int(first_solution[-1])])])  # Pare thn epomenh mikroterh apostash
            itemindex = np.nonzero(near[int(first_solution[-1])] == minimum_distance)
        first_solution.append(itemindex[0][0])      # Pros8ese to sth lysh
        first_distances.append(minimum_distance)    # Pros8ese thn apostash tou sth lysh

    first_distances.append(distances[first_solution[-1]][first_solution[0]])  # apostash teleutaiou kai prwtou stoixeiou
    return first_solution, first_distances, distances
