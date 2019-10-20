n = None
w = None
p = [None for x in range(100000)]

inputFile = open("alienin.txt", "r")
outputFile = open("alienout.txt", "w")

input_line = inputFile.readline().strip()
n, w = [int(x) for x in input_line.split()]

for i in range(0, n):
    p[i] = int(inputFile.readline().strip())

answer = 0
first = 0
last = 0

for last in range(n):
    while p[last]-p[first] >= w:
        first += 1
    if answer < last - first + 1:
        answer = last - first + 1

outputFile.write(str(answer))

inputFile.close()
outputFile.close()
