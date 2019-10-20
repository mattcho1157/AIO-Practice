# N is the number of flowers.
N = None
a = None
b = None
c = None

# Open the input and output files.
input_file = open("vasesin.txt", "r")
output_file = open("vasesout.txt", "w")

# Read the value of N from the input file. 
N = int(input_file.readline().strip())

if N >= 6:
    a = 1
    b = 2
    c = N-3
else:
    a = 0
    b = 0
    c = 0
# Write the answer to the output file.
output_file.write("%d %d %d\n" % (a, b, c))

# Finally, close the input/output files.
input_file.close()
output_file.close()
