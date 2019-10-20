f = open("piratein.txt", "r")
data = list(map(int, f.readlines()))
f.close()

f = open("pirateout.txt", "w")
f.write(str(min(data[1]+data[2], 2*data[0]-data[1]-data[2])))
f.close()
