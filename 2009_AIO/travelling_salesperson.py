f = open("salesin.txt", "r")
a = sorted([int(f.readline()) for x in range(3)])
f.close()

f = open("salesout.txt", "w")
f.write(str(a[2] + a[1]))
f.close()
