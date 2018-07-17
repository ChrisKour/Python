def readColumns(lines_list):                        # Diabasma onomatwn periorismwn
    indexRow = lines_list.index("ROWS")             # Pou ksekinaei to kommati ROWS
    indexCol = lines_list.index("COLUMNS")          # Pou ksekinaei to kommati COLUMNS
    rows = [[] for i in range(2)]                   # Dhmiourgia pinaka rows
    N = ''                                          # Onoma periorismou antikeimenikhs synarthshs

    for i in range(indexRow, indexCol):
        if lines_list[i].split()[0] == "L":         # An o periosmos einai <= tote apo8hkeuw -1 kai to onoma
            rows[0].append(-1)
            rows[1].append(lines_list[i].split()[1])
        elif lines_list[i].split()[0] == "G":       # An o periosmos einai = tote apo8hkeuw 0 kai to onoma
            rows[0].append(1)
            rows[1].append(lines_list[i].split()[1])
        elif lines_list[i].split()[0] == "E":       # An o periosmos einai >= tote apo8hkeuw 1 kai to onoma
            rows[0].append(0)
            rows[1].append(lines_list[i].split()[1])
        elif lines_list[i].split()[0] == "N":       # An petyxw to N apo8hkeuw to onoma toy periorismou
            N = lines_list[i].split()[1]

    return N, rows, indexCol

def readVariables(lines_list, indexCol, indexRHS):  # Gemisma tou pinaka me tis metablhtes
    x = []                                          # Dhmiourgia pinaka
    for i in range(indexCol + 1, indexRHS):
        if lines_list[i].split()[0] not in x:       # elegxos gia kainourgia metablhth
            x.append(lines_list[i].split()[0])      # Thn bazw ston pinaka
    return x

def read_arrays_a_c(lines_list, x, rows, indexCol, indexRHS, N):        # Gemisma twn pinakwn A, C
    c = [0 for i in range(len(x))]                                      # Dhmiourgia pinaka c
    A = [[0 for col in range(len(x))] for row in range(len(rows[0]))]   # Dhmiourgia pinaka A

    for i in range(indexCol + 1, indexRHS):
        if N in lines_list[i]:                                          # An petyxw to N (se opoiodhpote kommati ths grammhs)
            varIndex = x.index(lines_list[i].split()[0])                # Pairnw th 8esh ths metablhths
            costIndex = lines_list[i].split().index(N) + 1              # Pairnw th sthlh poy einai to stoixeio
            c[varIndex] = float(lines_list[i].split()[costIndex])       # Bazw to stoixeio ston C
        if lines_list[i].split()[1] in rows[1]:                         # Diaforetika an exw sthn deuterh sthlh periorismo
            varIndex = x.index(lines_list[i].split()[0])                # Pairnw th 8esh ths metablhths ston pinaka x
            rowsIndex = rows[1].index(lines_list[i].split()[1])         # Pairnw th 8esh pou exei to onoma toy periorismoy sto rows
            A[rowsIndex][varIndex] = float(lines_list[i].split()[2])    # Bazw to stoixeio ston A
        if len(lines_list[i].split()) > 3:                              # Antistoixa an exw perissoteres sthles
            if lines_list[i].split()[3] in rows[1]:
                varIndex = x.index(lines_list[i].split()[0])
                rowsIndex = rows[1].index(lines_list[i].split()[3])
                A[rowsIndex][varIndex] = float(lines_list[i].split()[4])
    return c, A

def read_array_b(lines_list, indexRANGES, indexBOUNDS, indexENDATA, rows, indexRHS):    # Gemisma tou pinaka b
    if indexRANGES != -1:               # Edw ginontai elegxoi an yparxoyn ta proeraitika kommatia
        nextStop = indexRANGES
    elif indexBOUNDS != -1:
        nextStop = indexBOUNDS
    else:
        nextStop = indexENDATA

    b = [0 for i in range(len(rows[0]))]                                # Dhmiourgia pinaka b
    for i in range(indexRHS + 1, nextStop):
        rowsIndex = rows[1].index(lines_list[i].split()[1])             # Pairnw th 8esh pou exei to onoma toy periorismoy sto rows
        b[rowsIndex] = float(lines_list[i].split()[2])                  # Bazw to stoixeio ston b
        if len(lines_list[i].split()) > 3:                              # Antistoixa an exw perissoteres sthles
            rowsIndex = rows[1].index(lines_list[i].split()[3])
            b[rowsIndex] = float(lines_list[i].split()[4])
    return b
