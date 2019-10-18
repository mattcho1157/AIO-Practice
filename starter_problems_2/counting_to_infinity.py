# opening file
f = open("countin.txt", "r")
number = f.readline()
f.close()

# calculating
f = open("countout.txt", "w")

for integer in range(1,int(number)+1):
    f.write(str(integer) + "\n")

f.close()
