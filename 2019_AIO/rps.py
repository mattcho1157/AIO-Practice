# N is the number of rounds contested.
N = None

# Ra, Pa and Sa are the number of times your opponent will throw rock, paper,
# and scissors, respectively.
Ra = None
Pa = None
Sa = None

# Rb, Pb and Sb are the number of times you will throw rock, paper, and
# scissors, respectively.
Rb = None
Pb = None
Sb = None

answer = None

# Open the input and output files.
input_file = open("rpsin.txt", "r")
output_file = open("rpsout.txt", "w")

# Read the value of N from the input file. 
N = int(input_file.readline().strip())

# Read the value of Ra, Pa and Sa from the input file. 
input_line = input_file.readline().strip()
Ra, Pa, Sa = map(int, input_line.split())

# Read the value of Rb, Pb and Sb from the input file. 
input_line = input_file.readline().strip()
Rb, Pb, Sb = map(int, input_line.split())


W = min(Ra, Pb) + min(Pa, Sb) + min(Sa, Rb)
l, m, n = min(Ra, Pb), min(Pa, Sb), min(Sa, Rb)
Pb -= l
Sb -= m
Rb -= n

Ra -= l
Pa -= m
Sa -= n

D = min(Ra, Rb) + min(Pa, Pb) + min(Sa, Sb)
L = N - W - D
answer = W - L

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
