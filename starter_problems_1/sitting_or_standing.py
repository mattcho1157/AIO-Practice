f = open("sitin.txt", "r")
a = [int(x) for x in f.readline().split()]
b = int(f.readline())
f.close()

product = a[0]*a[1]
if product >= b:
    sit = b
    stand = 0
else:
    sit = product
    stand = b - sit

f = open("sitout.txt", "w")
f.write(str(sit) + " " + str(stand))
f.close()
