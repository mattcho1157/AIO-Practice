# N is the number of letters in the snake's DNA.
N = None

# dna contains the snake's DNA
dna = [None for x in range(100005)]

answer = None

# Open the input and output files.
input_file = open("snakein.txt", "r")
output_file = open("snakeout.txt", "w")

# Read the values of N and the DNA sequence from the input file. 
N = int(input_file.readline().strip())
dna = input_file.readline().strip()

import math
c = dna.count("S")
answer = math.ceil(c/5)

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()
