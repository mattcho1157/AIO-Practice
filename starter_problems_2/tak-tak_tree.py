import math

f = open("taktakin.txt", "r")
initial = f.readline()
initial = int(initial)
oldInitial = int(initial)
f.close()

if (initial-1) % 11 == 0:

    fullMoons = 0

else:

    while (initial-1) % 11 != 0:

        initial *= 2

        if (initial-1) % 11 == 0:

            fullMoons = int(math.log((initial/oldInitial),2))

f = open("taktakout.txt", "w")
f.write(str(fullMoons) + " " + str(initial) + "\n")
f.close()
