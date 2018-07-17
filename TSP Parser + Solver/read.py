import numpy as np


def read(lines_list):
    index_coords = lines_list.index("NODE_COORD_SECTION")    # Pou ksekinane oi syntetagmenes
    index_eof = lines_list.index("EOF")                      # Pou teleiwnei to arxeio
    dimension = 0
    weight = ""

    for i in range(index_coords):                            # Pairnoume times gia dimension kai weight
        if lines_list[i].split(":")[0] == 'DIMENSION' or lines_list[i].split(":")[0] == 'DIMENSION ':
            dimension = int(lines_list[i].split(": ")[1])
        elif lines_list[i].split(":")[0] == 'EDGE_WEIGHT_TYPE' or lines_list[i].split(":")[0] == 'EDGE_WEIGHT_TYPE ':
            weight = lines_list[i].split(": ")[1]

    print("Number of nodes:", dimension)                    # Tis ektypwnoyme
    print("Type of edge weight:", weight)

    nodes = np.empty([dimension, 2])                  # Dhmiourgia pinaka me syntetagmenes
    k = 0                                                   # Eswterikh metablhth

    for i in range(index_coords+1, index_eof):                # Se ka8e node bazoume tis syntetagmenes toy
        nodes[k][0] = int(lines_list[i].split()[1])
        nodes[k][1] = int(lines_list[i].split()[2])
        k += 1
    return nodes, dimension
