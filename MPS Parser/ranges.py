def readRanges(lines_list, rows, indexRANGES, b, A, x, indexBOUNDS, indexENDATA):
    if indexBOUNDS != -1:                                       # An yparxei BOUNDS
        nextStop = indexBOUNDS
    else:                                                       # An den yparxei BOUNDS
        nextStop = indexENDATA

    r = [0 for i in range(len(rows[1]))]                        # Dhmiourgia pinaka r
    for i in range(indexRANGES + 1, nextStop):
        rowsIndex = rows[1].index(lines_list[i].split()[1])     # Pairnw th 8esh pou exei to onoma toy periorismoy sto rows
        r[rowsIndex] = float(lines_list[i].split()[2])          # Bazw to stoixeio ston pinaka r
        if len(lines_list[i].split()) > 3:                      # Antistoixa an exw parapanw sthles
            rowsIndex = rows[1].index(lines_list[i].split()[3])
            r[rowsIndex] = float(lines_list[i].split()[4])

    print("\nRANGES:")
    first = True                                                # Elegxos gia ka8e kainoourgia grammh

    for i in range(len(r)):
        if r[i] != 0:                                           # Gia ta mh mhdenika stoixeia tou r
            if (rows[0][i] == 1) or (rows[0][i] == 0 and r[i] > 0):     # An o periorismos einai G h E me prosimo +
                begin = b[i]
                end = b[i] + abs(r[i])
            elif (rows[0][i] == -1) or (rows[0][i] == 0 and r[i] < 0):  # An o periorismos einai L h E me prosimo -
                begin = b[i] - abs(r[i])
                end = b[i]
            print(begin, "<= ", end='')                          # Ektypwsh katw oriou
            for j in range(len(A[0])):
                if A[i][j] != 0:                                # Gia ta mh mhdenika stoixeia tou A
                    if first:                                   # To prwto ths ka8e grammhs
                        print(A[i][j], "*", x[j], end='')
                        first = False
                    else:                                       # Diaforetika
                        if A[i][j] < 0:                         # An einai arnhtiko den xreiazomaste symbolo prin
                            print("", A[i][j], "*", x[j], end='')
                        else:                                   # An einai 8etiko ektypwnw symbolo pros8eshs
                            print("+", A[i][j], "*", x[j], end='')
            print(" <=", end)                                    # Ektypwsh panw oriou
        first = True
    return r
