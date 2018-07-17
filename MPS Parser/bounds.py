# Krataw eksi times gia thn ka8e metablhth
# low,up,fixed,free,katw orio-oo,dyadikh
# Oti den xreishmopoieitai einai 0

def readBounds(lines_list, indexBOUNDS, indexENDATA, x):
    bounds = [["e" for col in range(6)] for row in range(len(x))]         # Dhmiourgia pinaka bounds
    for i in range(indexBOUNDS + 1, indexENDATA):
        varIndex = x.index(lines_list[i].split()[2])                    # Pairnw th 8esh ths metablhths ston pinaka x
        if lines_list[i].split()[0] == "UP":                            # Analoga me ton typo apo8hkeuw ta dedomena
            bounds[varIndex][0] = float(lines_list[i].split()[3])
        elif lines_list[i].split()[0] == "LO":
            bounds[varIndex][1] = float(lines_list[i].split()[3])
        elif lines_list[i].split()[0] == "FX":
            bounds[varIndex][2] = float(lines_list[i].split()[3])
        elif lines_list[i].split()[0] == "FR":
            bounds[varIndex][3] = 1
        elif lines_list[i].split()[0] == "MI":
            bounds[varIndex][4] = 1
        elif lines_list[i].split()[0] == "BV":
            bounds[varIndex][5] = 1
        if len(lines_list[i].split()) > 4:                              # Edw h idia diadikasia se periptwsh pou exw
            varIndex = x.index(lines_list[i].split()[4])                # parapanw sthles
            if lines_list[i].split()[0] == "UP":
                bounds[varIndex][0] = float(lines_list[i].split()[5])
            elif lines_list[i].split()[0] == "LO":
                bounds[varIndex][1] = float(lines_list[i].split()[5])
            elif lines_list[i].split()[0] == "FX":
                bounds[varIndex][2] = float(lines_list[i].split()[5])
            elif lines_list[i].split()[0] == "FR":
                bounds[varIndex][3] = 1
            elif lines_list[i].split()[0] == "MI":
                bounds[varIndex][4] = 1
            elif lines_list[i].split()[0] == "BV":
                bounds[varIndex][5] = 1

    print("\nBOUNDS:")

    for i in range(len(x)):                                     # Analoga me ton typo ektypwnw ta dedomena
        if bounds[i][0] != "e" and bounds[i][1] != "e":         # An exw upper kai lower bound ta ektypwnw
            print(bounds[i][0], ">=", x[i], ">=", bounds[i][1])
        elif bounds[i][0] != "e" and bounds[i][1] == "e":       # An exw mono upper to ektypwnw kai meta ektypwnw to default 0
            print(bounds[i][0], ">=", x[i], ">=", 0)
        elif bounds[i][0] == "e" and bounds[i][1] != "e":       # An exw mono lower to ektypwnw
            print(x[i], ">=", bounds[i][1])
        if bounds[i][2] != "e":
            print(x[i], "=", bounds[i][2])
        if bounds[i][3] != "e":
            print(x[i], "is free.")
        if bounds[i][4] != "e":
            print(x[i], "> -\u221E")
        if bounds[i][5] != "e":
            print(x[i], "= 0 or ", x[i], "= 1")

    return bounds
