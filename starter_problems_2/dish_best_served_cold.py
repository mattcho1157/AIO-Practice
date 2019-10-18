f = open("dishin.txt","r")
integers = []
for line in f:
    integers.append(int(line))

f.close()

integers = integers[1:]

mini = min(integers)
maxi = max(integers)
mean = int(sum(integers)/len(integers))

f = open("dishout.txt", "w")
f.write(str(mini) + " " + str(maxi) + " "  + str(mean) + "\n")
f.close()
