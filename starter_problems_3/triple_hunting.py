f = open("tripin.txt", "r")
triples_index = []
lines = int(f.readline())

for i in range(lines):
    if int(f.readline()) % 3 == 0:
        triples_index.append(i+1)
f.close()

length = len(triples_index)



f = open("tripout.txt", "w")
if length > 0:
    f.write(str(len(triples_index)) + "\n")
    for index in triples_index:
        f.write(str(index) + " ")
else:
    f.write("Nothing here!")
f.close()
