import os.path
import sys
from read import readColumns, readVariables, read_arrays_a_c, read_array_b
from bounds import readBounds
from ranges import readRanges
from print import printProblem, printSynarthsh

filename = input("Enter a file name: ")  # o xrhsths dinei to onoma tou arxeiou(prepei na einai sto idio directory)

if not (os.path.isfile("./"+filename+".mps")):          # An den yparxei stamataei to programma
    print("There is no such file.")
    sys.exit(1)

lines_list = open(filename+".mps").read().splitlines()  # Lista me oles tis grammes
sys.stdout = open('output.txt', 'wt')                   # Ta apotelesmata pane sto output.txt

problem_name = lines_list[0].split()[1]                 # Onoma problhmatos
print("Problem Name:", problem_name)

N, rows, indexCol = readColumns(lines_list)             # Diabasma onomatwn periorismwn
indexRHS = lines_list.index("RHS")                      # Pou ksekinaei to kommati RHS

x = readVariables(lines_list, indexCol, indexRHS)       # Gemisma toy pinaka me tis metablhtes
c, A = read_arrays_a_c(lines_list, x, rows, indexCol, indexRHS, N)  # Gemisma twn pinakwn C, A
printSynarthsh(c, x)                                    # Ektypwse antikeimenikh synarthsh

indexRANGES = -1                                        # Elegxos an yparxei kommati RANGES
if 'RANGES' in lines_list:
    indexRANGES = lines_list.index("RANGES")

indexBOUNDS = -1                                        # Elegxos an yparxei kommati BOUNDS
if 'BOUNDS' in lines_list:
    indexBOUNDS = lines_list.index("BOUNDS")

indexENDATA = lines_list.index("ENDATA")                # Pou teleiwnoun ta dedomena

b = read_array_b(lines_list, indexRANGES, indexBOUNDS, indexENDATA, rows, indexRHS)  # Gemisma tou pinaka b
printProblem(A, x, rows, b)                             # Ektypwse Ax = b

if indexRANGES != -1:   # An yparxei to kommati ranges ektelese
    r = readRanges(lines_list, rows, indexRANGES, b, A, x, indexBOUNDS, indexENDATA)

if indexBOUNDS != -1:  # An yparxei to kommati bounds ektelese
    bounds = readBounds(lines_list, indexBOUNDS, indexENDATA, x)
