def printSynarthsh(c, x):                                   # Ektypwsh antikeimenikhs synarthshs
    print("min z = ", end='')                               # Ektypwsh arxhs
    first = True                                            # 8a mpei mono thn prwth fora

    for i in range(len(c)):
        if c[i] != 0:                                       # An exoume mh mhdenikh timh
            if first:
                print(c[i], "*", x[i], end='')              # Ektypwse to prwto
                first = False
            else:                                           # Diaforetika
                if c[i] < 0:                                # An einai arnhtiko den xreiazomaste symbolo prin
                    print("", c[i], "*", x[i], end='')
                else:                                       # An einai 8etiko ektypwnw symbolo pros8eshs
                    print(" +", c[i], "*", x[i], end='')
    print()                                                 # Allagh Grammhs


def printProblem(A, x, rows, b):                            # Ektypwsh pinakwn A, x, b
    print("s.t. ", end='')                                  # Ektypwsh arxhs
    first = True                                            # 8a mpei mono to prwto stoixeio ths ka8e grammhs

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] != 0:                                # An exoume mh mhdenikh timh
                if first:                                   # Ektypwse to prwto
                    print(A[i][j], "*", x[j], end='')
                    first = False
                else:                                       # Diaforetika
                    if A[i][j] < 0:                         # An einai arnhtiko den xreiazomaste symbolo prin
                        print("", A[i][j], "*", x[j], end='')
                    else:                                   # An einai 8etiko ektypwnw symbolo pros8eshs
                        print(" +", A[i][j], "*", x[j], end='')
        if not first:                                       # Elegxos an yphrxan mh mhdenika stoixeia sth grammh
            if rows[0][i] == -1:                            # An o periorismos einai L
                print(" <=", b[i])
            elif rows[0][i] == 0:                           # An o periorismos einai E
                print(" =", b[i])
            else:                                           # An o periorismos einai G
                print(" >=", b[i])
            print("     ", end='')                          # Ektypwsh ligo pio mesa gia thn epomenh grammh
        first = True
